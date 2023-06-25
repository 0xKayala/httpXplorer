from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///target_domain.db'
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200))
    status_code = db.Column(db.Integer)
    tech = db.Column(db.String(200))
    cdn_name = db.Column(db.String(200))
    host = db.Column(db.String(200))

    def __init__(self, url, status_code, tech, cdn_name, host):
        self.url = url
        self.status_code = status_code
        self.tech = tech
        self.cdn_name = cdn_name
        self.host = host

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        json_data = request.files['json_data']
        data = json.load(json_data)

        with app.app_context():
            for entry in data:
                url = entry.get('url', 'NULL')
                status_code = entry.get('status_code', 0)
                tech = entry.get('tech', 'NULL')
                cdn_name = entry.get('cdn_name', 'NULL')
                host = entry.get('host', 'NULL')

                # Check if status_code is an integer
                if not isinstance(status_code, int):
                    status_code = 0

                # Convert tech list to a string
                tech = json.dumps(tech)

                existing_data = Data.query.filter_by(url=url).first()

                if existing_data:
                    existing_data.status_code = status_code
                    existing_data.tech = tech
                    existing_data.cdn_name = cdn_name
                    existing_data.host = host
                else:
                    new_data = Data(url=url, status_code=status_code, tech=tech, cdn_name=cdn_name, host=host)
                    db.session.add(new_data)

            db.session.commit()

    sort = request.args.get('sort', 'asc')
    with app.app_context():
        if sort == 'asc':
            all_data = Data.query.order_by(Data.status_code.asc()).all()
        elif sort == 'desc':
            all_data = Data.query.order_by(Data.status_code.desc()).all()
        else:
            all_data = Data.query.all()

    return render_template('index.html', all_data=all_data, sort=sort)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)


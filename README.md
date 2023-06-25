# httpXplorer
### httpXplorer is a powerful web-based application specifically designed for efficient URL management and analysis of the results obtained from projectdiscovery's httpx tools. It allows users to easily upload the httpx JSON output file containing URLs, analyze their status codes, web technologies, and explore other relevant information. With httpXplorer, you can sort the URLs based on their status codes, making it convenient to prioritize and focus on specific areas of interest.
### Whether you're a penetration tester or bug hunter, httpXplorer provides valuable insights into your target URLs, helping you identify potential issues and optimize your workflow. The user-friendly interface and intuitive features of httpXplorer enable seamless organization, sorting, and extraction of information from your URL data. Whether you have a large collection of URLs or need to make informed decisions based on the data, httpXplorer simplifies the process and enhances your productivity and you'll get comprehensive understanding of your target.

### With httpXplorer, you have a centralized platform to manage and analyze your URL data, saving you time and effort. The application's powerful features and intuitive interface make it easy for both beginners and experienced professionals to navigate and extract valuable insights from their URL datasets. Whether you are performing security assessments, bug hunting, or optimizing web applications, httpXplorer is your go-to tool for efficient URL management and analysis.

### Take your URL analysis to the next level with httpXplorer and unlock the full potential of your projectdiscovery's httpx tools results. Simplify your workflow, enhance your decision-making process, and stay ahead in the world of web application testing and security. Try httpXplorer today and experience the convenience, efficiency, and effectiveness it brings to your URL management and analysis tasks.
#
#

## Features
httpXplorer offers the following key features:

1. **URL Upload**: Upload a JSON file of the htpx output.
2. **Status Code Analysis**: Analyze the status codes of the URLs to identify errors, redirects, and successful responses.
3. **URL Sorting**: Sort the URLs based on their status codes in ascending or descending order.
4. **Data Update**: Easily update the latest data of the target. When upload latest json file, if any data (status codes, technologies, CDN names, and hosts) changes in the latest output file, the new data will be updated by replacing old data. 
5. **Copy URLs**: Copy a range of URLs by specifying the start and end index, making it convenient to share or export specific sets of URLs.
6. **User-Friendly Interface**: Enjoy a clean and intuitive user interface that simplifies the URL management and analysis process.
7. **Database Integration**: Utilize a database to store and retrieve the uploaded URLs and their associated data.
8. **Flexible Configuration**: Customize the application's database name and adapt it to your specific target domain and requirements.
9. **Easy Installation**: Follow the straightforward installation steps to quickly set up the httpXplorer application on your local machine.
10. **Centralized Database**: Create centralized local database of your target domains/subdomains.

## Installation

Follow these steps to install and set up the httpXplorer application on your local machine:

### Prerequisites

Make sure you have the following prerequisites installed:

- Python (version 3.6 or higher)
- pip (Python package installer)

### Installation Steps

1. **Clone the Repository**: Clone the httpXplorer repository to your local machine:

   ```shell
   git clone https://github.com/Abid-Ahmad/httpXplorer.git
   ```

2. **Navigate to the Project Directory**: Open a terminal and navigate to the project directory:

   ```shell
   cd httpXplorer
   ```

3. **Create a Virtual Environment (Optional)**: It is recommended to create a virtual environment to isolate the application's dependencies:

   ```shell
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**: Activate the virtual environment:

   - For Windows:

     ```shell
     venv\Scripts\activate
     ```

   - For macOS and Linux:

     ```shell
     source venv/bin/activate
     ```

5. **Install Dependencies**: Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

6. **Set up the Database**: The application uses SQLite by default. If you want to use a different database, update the `SQLALCHEMY_DATABASE_URI` configuration in the `app.py` file. By default, just install the SQLite in your local machine and change Database Name on `SQLALCHEMY_DATABASE_URI`.   

   ```shell
   app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///target_domain.db'
   
   ```

7. **Start the Application**: Start the application:

   ```shell
   flask run
   ```

8. **Access the Application**: Open your web browser and visit `http://localhost:5000` to access the httpXplorer application.

## Usage

Once the httpXplorer application is running, you

 can perform the following actions:

1. **Upload URLs**: Use the file upload form on the home page to upload a JSON file containing URLs and their associated data.
2. **Analyze Status Codes**: Analyze the status codes of the URLs to identify errors, redirects, and successful responses.
3. **Sort URLs**: Sort the URLs based on their status codes in ascending or descending order for better organization and analysis.
4. **Manipulate Data**: Easily manipulate and update the status codes, technologies, CDN names, and hosts of the URLs to reflect changes or corrections.
5. **Copy URLs**: Copy a range of URLs by specifying the start and end index, facilitating sharing or exporting of specific sets of URLs.
6. **Search and Filter**: Use the search functionality or apply filters to quickly find specific URLs or narrow down the displayed results.

## Troubleshooting

If you encounter any issues during the installation or usage of the httpXplorer application, please follow these steps:

1. **Check the Issue Tracker**: Check the project's issue tracker on GitHub for any known issues or resolutions.

2. **Open a New Issue**: If the issue persists or you have identified a new problem, open a new issue on the project's GitHub repository. Provide detailed information about the problem, including any error messages encountered.

3. **Seek Support**: Seek support from the project maintainers by contacting them via the contact details provided in the project's documentation or on the GitHub repository.

## License

The httpXplorer project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute the application as per the terms of the license.

```

You can copy and paste this enhanced Markdown documentation into your project's README.md file on GitHub. It provides a clear and concise overview of the httpXplorer application, its features, installation steps, usage instructions, troubleshooting guidance, and license information.

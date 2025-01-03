# API Request to GitHub

## Overview
This project is a Python-based application designed to interact with GitHub's API. It retrieves and displays all public repositories for a specified GitHub user. The project is implemented using Python and uses the `requests` library to send HTTP requests to the GitHub API.

## Features
- Connect to the GitHub API.
- Fetch and list all public repositories for a specific user.
- Display repository names and their corresponding URLs.

## Technologies Used
- **Python**: For scripting and API interaction.
- **GitHub**: The external application whose API is being consumed.
- **IntelliJ IDEA**: The integrated development environment (IDE) for project development.
- **Git**: For version control.

## Prerequisites
Before running this project, ensure you have the following installed:

1. **Python**: Version 3.6 or higher.
   - [Download Python](https://www.python.org/downloads/)
2. **pip**: Python package manager (comes pre-installed with Python).
3. **requests module**: Install using the command:
   ```bash
   pip install requests
   ```
4. **Git**: For version control.
   - [Download Git](https://git-scm.com/)

## Installation and Setup
   
1. Navigate to the project directory:
   ```bash
   cd api-request-github
   ```
2. Install the required Python module:
   ```bash
   pip install requests
   ```

## Usage
1. Run the script:
   ```bash
   python script_name.py
   ```
2. The script will display:
   - A list of all public repositories for the specified user.
   - The name and URL of each repository.


## Code Overview
```python
import requests

# Get repo list from GitHub
response = requests.get("https://api.github.com/users/irschad/repos")
my_repositories = response.json()

# Print the whole object list
print(my_repositories)
print(type(my_repositories))

# Print the names and URLs of repositories
for repo in my_repositories:
    print(f"Repository Name: {repo['name']}\nRepository URL: {repo['html_url']}\n")
```


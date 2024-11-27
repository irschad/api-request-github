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

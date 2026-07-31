import requests

BASE_URL = "https://api.github.com"


def fetch_repository(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    raise Exception(f"GitHub API Error: {response.status_code}")

def fetch_commits(owner, repo, per_page=100):
    url = f"{BASE_URL}/repos/{owner}/{repo}/commits"

    response = requests.get(url, params={"per_page": per_page})

    if response.status_code == 200:
        return response.json()

    raise Exception(f"GitHub API Error: {response.status_code}")

def fetch_contributors(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/contributors"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    raise Exception(f"GitHub API Error: {response.status_code}")


if __name__ == "__main__":
    repository = fetch_repository("microsoft", "vscode")

    print("Repository:", repository["full_name"])
    print("Stars:", repository["stargazers_count"])
    print("Forks:", repository["forks_count"])
    print("Language:", repository["language"])
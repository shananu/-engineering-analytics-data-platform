import requests
import os
from dotenv import load_dotenv

load_dotenv()

HEADERS = {
    "Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}",
    "Accept": "application/vnd.github+json"
}

BASE_URL = "https://api.github.com"


def fetch_repository(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()

    raise Exception(f"GitHub API Error: {response.status_code}")

def fetch_commits(owner, repo, max_pages=5):
    commits = []

    for page in range(1, max_pages + 1):
        url = f"{BASE_URL}/repos/{owner}/{repo}/commits"

        response = requests.get(
            url,
            headers=HEADERS,
            params={
                "per_page": 100,
                "page": page
            }
        )

        response.raise_for_status()

        batch = response.json()

        if not batch:
            break

        commits.extend(batch)
        print(f"Fetched page {page} ({len(batch)} commits)")

    return commits

def fetch_contributors(owner, repo):
    url = f"{BASE_URL}/repos/{owner}/{repo}/contributors"

    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()

    raise Exception(f"GitHub API Error: {response.status_code}")


if __name__ == "__main__":
    repository = fetch_repository("microsoft", "vscode")

    print("Repository:", repository["full_name"])
    print("Stars:", repository["stargazers_count"])
    print("Forks:", repository["forks_count"])
    print("Language:", repository["language"])
from extract import fetch_repository
from transform import transform_repository
from load import load_repository
from extract import fetch_repository, fetch_commits
from transform import transform_repository, transform_commits
from load import load_repository, load_commits

def main():
    owner = input("GitHub Owner: ")
    repo = input("Repository Name: ")

    raw_repo = fetch_repository(owner, repo)
    clean_repo = transform_repository(raw_repo)
    load_repository(clean_repo)

    print(f"✅ {owner}/{repo} loaded successfully!")


    commits = fetch_commits(owner, repo)
    clean_commits = transform_commits(commits, clean_repo["id"])
    load_commits(clean_commits)

    print(f"Loaded {len(clean_commits)} commits")

if __name__ == "__main__":
    main()
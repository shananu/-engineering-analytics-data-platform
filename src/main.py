from extract import fetch_repository, fetch_commits, fetch_contributors
from transform import transform_repository, transform_commits, transform_contributors
from load import load_repository, load_commits, load_contributors
import logging 

def main():
    owner = input("GitHub Owner: ")
    repo = input("Repository Name: ")

    raw_repo = fetch_repository(owner, repo)
    clean_repo = transform_repository(raw_repo)
    load_repository(clean_repo)

    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

    logging.info(f"{owner}/{repo} loaded successfully!")

    contributors = fetch_contributors(owner, repo)
    clean_contributors = transform_contributors(contributors)
    load_contributors(clean_contributors)

    logging.info(f"Loaded {len(clean_contributors)} contributors")


    commits = fetch_commits(owner, repo)
    clean_commits = transform_commits(commits, clean_repo["id"])
    load_commits(clean_commits)

    logging.info(f"Loaded {len(clean_commits)} commits")    


if __name__ == "__main__":
    main()
def transform_repository(repo):
    return {
        "id": repo["id"],
        "name": repo["name"],
        "full_name": repo["full_name"],
        "language": repo["language"],
        "stars": repo["stargazers_count"],
        "forks": repo["forks_count"],
        "open_issues": repo["open_issues_count"],
        "created_at": repo["created_at"]
    }

def transform_commits(commits, repository_id):
    transformed = []

    for commit in commits:
        transformed.append({
            "sha": commit["sha"],
            "repository_id": repository_id,
            "contributor_id": commit["author"]["id"] if commit["author"] else None,
            "message": commit["commit"]["message"],
            "commit_date": commit["commit"]["author"]["date"]
        })

    return transformed

def transform_contributors(contributors):
    transformed = []

    for contributor in contributors:
        transformed.append({
            "id": contributor["id"],
            "username": contributor["login"],
            "profile_url": contributor["html_url"]
        })

    return transformed
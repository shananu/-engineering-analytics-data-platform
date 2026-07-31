from database import get_connection

def load_repository(repo):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO repositories (
            id,
            name,
            full_name,
            language,
            stars,
            forks,
            open_issues,
            created_at
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        ON CONFLICT (id)
        DO UPDATE SET
            stars = EXCLUDED.stars,
            forks = EXCLUDED.forks,
            open_issues = EXCLUDED.open_issues;
    """, (
        repo["id"],
        repo["name"],
        repo["full_name"],
        repo["language"],
        repo["stars"],
        repo["forks"],
        repo["open_issues"],
        repo["created_at"]
    ))

    conn.commit()
    cur.close()
    conn.close()


def load_commits(commits):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO commits (
        sha,
        repository_id,
        contributor_id,
        message,
        commit_date
    )
    VALUES (%s,%s,%s,%s,%s)
    ON CONFLICT (sha) DO NOTHING;
    """

    for commit in commits:
        cur.execute(query, (
            commit["sha"],
            commit["repository_id"],
            commit["contributor_id"],
            commit["message"],
            commit["commit_date"]
        ))

    conn.commit()

    cur.close()
    conn.close()


def load_contributors(contributors):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO contributors (id, username, profile_url)
    VALUES (%s, %s, %s)
    ON CONFLICT (id) DO UPDATE
    SET
        username = EXCLUDED.username,
        profile_url = EXCLUDED.profile_url;
    """

    for contributor in contributors:
        cur.execute(query, (
            contributor["id"],
            contributor["username"],
            contributor["profile_url"]
        ))

    conn.commit()
    cur.close()
    conn.close()
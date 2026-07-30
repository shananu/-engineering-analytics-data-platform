CREATE TABLE IF NOT EXISTS repositories (
    id BIGINT PRIMARY KEY,
    name VARCHAR(255),
    full_name VARCHAR(255),
    language VARCHAR(100),
    stars INT,
    forks INT,
    open_issues INT,
    created_at TIMESTAMP
);

CREATE TABLE IF NOT EXISTS contributors (
    id BIGINT PRIMARY KEY,
    username VARCHAR(255),
    profile_url TEXT
);

CREATE TABLE IF NOT EXISTS commits (
    sha VARCHAR(100) PRIMARY KEY,
    repository_id BIGINT,
    contributor_id BIGINT,
    message TEXT,
    commit_date TIMESTAMP,
    FOREIGN KEY (repository_id) REFERENCES repositories(id),
    FOREIGN KEY (contributor_id) REFERENCES contributors(id)
);
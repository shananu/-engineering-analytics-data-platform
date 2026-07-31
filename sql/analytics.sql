-- Total repositories
SELECT COUNT(*) AS total_repositories
FROM repositories;

-- Repository details
SELECT
    name,
    language,
    stars,
    forks
FROM repositories;

-- Total commits
SELECT COUNT(*) AS total_commits
FROM commits;

-- Top 10 contributors by commits
SELECT
    c.username,
    COUNT(cm.sha) AS total_commits
FROM contributors c
JOIN commits cm
ON c.id = cm.contributor_id
GROUP BY c.username
ORDER BY total_commits DESC
LIMIT 10;

-- Commits per day
SELECT
    DATE(commit_date) AS day,
    COUNT(*) AS commits
FROM commits
GROUP BY DATE(commit_date)
ORDER BY day DESC;
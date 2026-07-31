# GitHub Engineering Analytics Platform

A Python-based ETL pipeline that extracts GitHub repository data using the GitHub REST API, transforms raw JSON into a relational format, and loads it into PostgreSQL for SQL-based engineering analytics.

---

## Features

- Extract repository information from the GitHub REST API
- Fetch repository contributors
- Fetch recent commits
- Transform raw API responses into structured data
- Store data in PostgreSQL
- Perform SQL analytics on engineering data
- Modular ETL architecture

---

## Tech Stack

- Python
- PostgreSQL
- GitHub REST API
- psycopg2
- requests
- python-dotenv
- SQL

---

## Project Structure

```
engineering-analytics-data-platform/
│
├── src/
│   ├── main.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── database.py
│
├── sql/
│   ├── schema.sql
│   └── analytics.sql
│
├── data/
├── .env
├── requirements.txt
└── README.md
```

---

## ETL Workflow

```
GitHub REST API
        │
        ▼
+----------------+
|   Extract      |
+----------------+
        │
        ▼
+----------------+
|  Transform     |
+----------------+
        │
        ▼
+----------------+
|     Load       |
+----------------+
        │
        ▼
 PostgreSQL Database
        │
        ▼
 SQL Analytics
```

---

## Database Schema

### repositories

| Column | Description |
|--------|-------------|
| id | Repository ID |
| name | Repository name |
| full_name | Full repository name |
| language | Primary language |
| stars | Stargazers count |
| forks | Fork count |
| open_issues | Number of open issues |
| created_at | Repository creation date |

### contributors

| Column | Description |
|--------|-------------|
| id | Contributor ID |
| username | GitHub username |
| profile_url | GitHub profile URL |

### commits

| Column | Description |
|--------|-------------|
| sha | Commit SHA |
| repository_id | Repository reference |
| contributor_id | Contributor reference |
| message | Commit message |
| commit_date | Commit timestamp |

---

## Setup

### Clone the repository

```bash
git clone <repository-url>
cd engineering-analytics-data-platform
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure environment variables

Create a `.env` file.

```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=github_analytics
DB_USER=postgres
DB_PASSWORD=your_password
```

### Create the database

```sql
CREATE DATABASE github_analytics;
```

### Create tables

```bash
psql -U postgres -d github_analytics -f sql/schema.sql
```

### Run the ETL pipeline

```bash
python src/main.py
```

---

## Sample Output

```
GitHub Owner: tensorflow
Repository Name: tensorflow

INFO - tensorflow/tensorflow loaded successfully!
INFO - Loaded 30 contributors
INFO - Loaded 100 commits
```

---

## Analytics

The project includes SQL queries for:

- Repository summary
- Total commits
- Top contributors
- Commits per day
- Repository statistics

Run:

```bash
psql -U postgres -d github_analytics -f sql/analytics.sql
```

---

## Future Improvements

- Incremental loading
- GitHub authentication token
- Docker support
- Apache Airflow scheduling
- Power BI dashboard
- Unit testing
- GitHub Actions CI/CD

---

## Author

Anushka Shanker
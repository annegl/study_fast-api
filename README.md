# Study FastAPI

This repository is created for following along and completing the exercises of the course **[FastAPI do Zero](https://fastapidozero.dunossauro.com/4.1/)** by Dunossauro.

## Purpose

The main goal of this repo is to:

- Learn FastAPI fundamentals.
- Practice building APIs from scratch.
- Complete the exercises proposed in the course.
- Explore testing, documentation, and deployment with FastAPI.

## Project Structure

```
study-fast-api/
├── src/            # Application source code
├── tests/          # Test cases for the project
├── pyproject.toml  # Project configuration and dependencies
├── .gitignore
└── README.md
```

## Setup

1. Clone the repository:

2. Install dependencies:

3. Run the FastAPI app locally:


## Testing



## Notes

This repo is meant purely for learning and practice purposes. All code is aligned with the course exercises and may not be production-ready.

## Useful commands

Alembic related commands:
- To generate a new migration script by comparing the current database schema with the Python models:
```alembic revision --autogenerate -m "description"```

- To apply all pending migrations to the database to bring it up to the latest version:
```alembic upgrade head```

- To revert the last applied migration, rolling back the database schema by one version:
```alembic downgrade -1```

- To visually inspect and verify that the Alembic migrations have correctly updated the database schema:
```uvx harlequin database.db```
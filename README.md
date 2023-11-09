# Interval Merger Service

## Description

This FastAPI web service merges a set of intervals considering exclusions and returns non-overlapping intervals in sorted order.

## Usage

1. Clone the repository.

```bash
git clone <repository_url>
cd <project_directory>
```
2. Build and run the Docker container.
```bash
docker-compose up --build
```

3. Access the service at http://localhost:8000/docs for Swagger documentation.

4. Use the /api/v1/merge_intervals endpoint to merge intervals.

# Example Request:

```json
{
    "includes": [{"start": 10, "end": 100}],
    "excludes": [{"start": 20, "end": 30}]
}
```
# Example Response:

```json
[
    {"start": 10, "end": 19},
    {"start": 31, "end": 100}
]
```

## Docker and Dependencies
Docker is used for containerization.
FastAPI and Uvicorn for the web service.
Pydantic for data validation.

## Project Structure
main.py: FastAPI application.
models.py: Pydantic models for data validation.
Dockerfile: Docker configuration file.
docker-compose.yml: Docker Compose configuration file.

## API Endpoint
POST /api/v1/merge_intervals: Accepts a set of intervals with exclusions and returns merged intervals.
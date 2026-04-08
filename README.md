# Docker Compose Nginx Flask Redis Project

This project demonstrates a multi-container application using Docker Compose, with Nginx as a reverse proxy, Flask as the backend application, Redis as the data store, and GitHub Actions for CI validation.

## Architecture

Browser → Nginx → Flask → Redis

## Skills Demonstrated

- Docker image creation with Dockerfile
- Multi-container orchestration with Docker Compose
- Reverse proxy setup with Nginx
- Service health checks
- Persistent data with named volumes
- Git and GitHub workflow
- Basic CI with GitHub Actions

## Run the project

```bash
docker compose up --build -d

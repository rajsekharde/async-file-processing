# Async Image/PDF Processing Application

## Architecture Diagram

![Architecture Diagram](media/architecture_diagram.png)

## Tech Stack

- **Traefik**: Routing, Automatic HTTPS
- **FastAPI**: Backend APIs
- **Nginx**: Static frontend hosting
- **Redis**: Job Queue
- **PostgreSQL**: Job/File Metadata
- **Worker**: Python
- **AWS S3**: File Storage
- **Docker, Docker compose**: Containerization

## Project Structure

```bash
├── backend
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── src
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── models
│   │   │   └── jobs.py
├── docker-compose.dev.yml
├── media
│   └── architecture_diagram.png
└── README.md
```

tree -L 4
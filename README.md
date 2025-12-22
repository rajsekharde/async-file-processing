# Async Image/PDF Processing Application

## Architecture Diagram

![Architecture Diagram](media/architecture_diagram.png)

---

## Tech Stack

- **Traefik**: Routing, Automatic HTTPS
- **FastAPI**: Backend APIs
- **Nginx**: Static frontend hosting
- **Redis**: Job Queue
- **PostgreSQL**: Job/File Metadata
- **Worker**: Python
- **AWS S3**: File Storage
- **Prometheus**: Metrics
- **Grafana**: Metrics Dashboard
- **Docker, Docker compose**: Containerization

---
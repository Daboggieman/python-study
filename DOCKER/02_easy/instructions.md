# Docker Level 2: Easy

Now that you know the basic idea, learn how to run Docker commands and build a simple image.

### Simple commands:
- `docker run hello-world` — run a basic container.
- `docker ps` — list running containers.
- `docker ps -a` — list all containers.
- `docker images` — list downloaded images.

### Build a Docker image:
A `Dockerfile` contains steps like:

```dockerfile
FROM python:3.11-slim
COPY app.py /app.py
CMD ["python", "/app.py"]
```

Then use:

```bash
docker build -t myapp .
docker run myapp
```

### What you learn here:
- The difference between building and running.
- How Docker reuses layers for faster builds.
- How a simple image is created from a Dockerfile.

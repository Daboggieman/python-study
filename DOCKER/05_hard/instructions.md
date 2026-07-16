# Docker Level 5: Hard

This level explains image optimization, build cache, and multi-stage builds.

### Image size and speed:
- Smaller images download and start faster.
- Use slim or alpine base images when possible.

### Build cache:
Docker reuses unchanged image layers to speed up rebuilds.

### Multi-stage builds:
Create one stage for building and another for shipping only the final result.

```dockerfile
FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

FROM python:3.11-slim
COPY --from=builder /app /app
CMD ["python", "/app/app.py"]
```

### Concepts covered:
- Efficient Dockerfiles
- Smaller production images
- Understanding how Docker layers work

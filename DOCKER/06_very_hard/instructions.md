# Docker Level 6: Very Hard

Now you learn about security, health checks, and runtime configuration.

### Security best practices:
- Avoid running containers as root when possible.
- Use trusted base images.
- Minimize the number of installed packages.

### Health checks:
Docker can verify whether a container is still healthy.

```dockerfile
HEALTHCHECK CMD curl --fail http://localhost:5000/health || exit 1
```

### Environment variables:
Pass configuration into containers without changing the image.

```bash
docker run -e APP_ENV=production myapp
```

### What to understand:
- Containers should be secure and minimal.
- Health checks help detect failures.
- Environment variables allow flexible behavior.

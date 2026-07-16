# Docker Level 7: Expert

This level covers advanced Docker usage in production-style environments.

### Image registries:
- Push and pull images from Docker Hub or private registries.
- Use `docker push <name>` and `docker pull <name>`.

### Deployment patterns:
- Build images with CI/CD pipelines.
- Use version tags like `myapp:1.0.0`.

### Advanced orchestration concepts:
- Docker is often a building block for Kubernetes.
- Containers should be stateless and replaceable.

### Expert habits:
- Keep Dockerfiles simple and reproducible.
- Test images locally before deployment.
- Monitor container health and logs.

### Example advanced workflow:
1. Build a tagged image.
2. Run tests inside a container.
3. Push the image to a registry.
4. Deploy in a controlled environment.

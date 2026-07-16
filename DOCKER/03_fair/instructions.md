# Docker Level 3: Fair

At this level, you learn how to organize containers and handle files inside them.

### Docker container basics:
- Containers can run in the background using `-d`.
- You can open a shell inside a running container with `docker exec -it <container> sh`.

### Working with files:
- Use `COPY` to add files into an image.
- Use `VOLUME` or `-v` for persistent data that stays after the container stops.

Example:
```dockerfile
FROM nginx:alpine
COPY website /usr/share/nginx/html
```

### Important details:
- Images are read-only once built.
- Containers can write to volumes and temporary file systems.
- Stopping a container does not delete its image.

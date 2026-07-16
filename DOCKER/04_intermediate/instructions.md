# Docker Level 4: Intermediate

This stage introduces networking, ports, and multi-container apps.

### Ports and networking:
- Use `-p 8080:80` to map a container port to your computer.
- Containers can talk to each other on a shared network.

Example:
```bash
docker run -p 5000:5000 myapp
```
This makes the app available at `http://localhost:5000`.

### Compose files:
Docker Compose lets you define multiple containers in one file.

```yaml
services:
  web:
    build: .
    ports:
      - "5000:5000"
  db:
    image: postgres
```

### Why this is useful:
- You can run web apps and databases together.
- You keep configuration in a simple text file.

# Docker Deployment Guide for EduFlow

This guide explains how to deploy the EduFlow Student Management System using Docker.

## 🐳 Docker Files Created

- **Dockerfile** - Main container configuration
- **docker-compose.yml** - Multi-service orchestration
- **nginx.conf** - Reverse proxy configuration
- **.dockerignore** - Build optimization

## 🚀 Quick Start

### Option 1: Simple Docker Deployment

```bash
# Build the Docker image
docker build -t eduflow .

# Run the container
docker run -d -p 5000:5000 --name eduflow-app eduflow
```

### Option 2: Docker Compose (Recommended)

```bash
# Build and run all services
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

## 📋 Prerequisites

- Docker Desktop (Windows/Mac) or Docker Engine (Linux)
- Docker Compose (for Option 2)

## 🔧 Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `FLASK_ENV` | `production` | Flask environment |
| `FLASK_APP` | `app.py` | Flask application file |
| `DOCKER_ENV` | `true` | Enable Docker-specific settings |

### Port Configuration

- **Direct Docker**: `http://localhost:5000`
- **Docker Compose**: `http://localhost:80` (via nginx)

## 📁 Docker Volumes

### Data Persistence

The application uses Docker volumes to persist data:

```yaml
volumes:
  - ./data:/app/data
```

This ensures your SQLite database survives container restarts.

## 🛠️ Build Process

### Multi-stage Build Optimization

1. **Base Image**: Python 3.11-slim for smaller size
2. **Dependencies**: Install requirements first for better caching
3. **Application Code**: Copy source code
4. **Security**: Run as non-root user
5. **Health Check**: Monitor application health

### .dockerignore

Excludes unnecessary files from build context:
- Git files
- Python cache
- Virtual environments
- IDE files
- Documentation

## 🔍 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Check what's using port 5000
   netstat -tulpn | grep :5000
   
   # Kill the process
   sudo kill -9 <PID>
   ```

2. **Permission Issues**
   ```bash
   # Fix permissions for data directory
   sudo chown -R $USER:$USER ./data
   ```

3. **Build Failures**
   ```bash
   # Clean build cache
   docker system prune -a
   
   # Rebuild without cache
   docker-compose build --no-cache
   ```

### Debug Mode

To run in debug mode:

```bash
# Set environment variable
export FLASK_ENV=development

# Or modify docker-compose.yml
environment:
  - FLASK_ENV=development
```

## 📊 Monitoring

### Health Checks

The container includes health checks:

```bash
# Check container health
docker ps
docker inspect eduflow-app | grep Health
```

### Logs

```bash
# View application logs
docker logs eduflow-app

# Follow logs in real-time
docker logs -f eduflow-app

# Docker Compose logs
docker-compose logs -f eduflow
```

## 🔄 Updates

### Updating the Application

```bash
# Pull latest changes
git pull

# Rebuild and restart
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

### Database Migrations

If you modify the database schema:

```bash
# Stop the container
docker-compose down

# Remove old database (WARNING: This deletes data!)
rm -f ./data/eduflow.db

# Restart with fresh database
docker-compose up -d
```

## 🌐 Production Deployment

### Security Considerations

1. **Change default secret key** in `app.py`
2. **Use HTTPS** with SSL certificates
3. **Implement authentication** for production use
4. **Regular security updates** for base images

### Scaling

```yaml
# Scale the application
docker-compose up -d --scale eduflow=3
```

### Backup Strategy

```bash
# Backup database
docker cp eduflow-app:/app/data/eduflow.db ./backup/

# Restore database
docker cp ./backup/eduflow.db eduflow-app:/app/data/
```

## 🎯 Performance Optimization

### Resource Limits

```yaml
# Add to docker-compose.yml
deploy:
  resources:
    limits:
      cpus: '0.5'
      memory: 512M
    reservations:
      cpus: '0.25'
      memory: 256M
```

### Caching

- Static files cached for 1 year
- Nginx reverse proxy for better performance
- Connection pooling in database

## 📞 Support

For Docker-specific issues:

1. Check container logs
2. Verify port availability
3. Ensure Docker is running
4. Review system resources

---

**EduFlow** - Containerized Student Management System 🐳

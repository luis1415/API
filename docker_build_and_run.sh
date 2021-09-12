docker build -f property_app.dockerfile -t api .
docker run --rm -d  -p 8000:8000/tcp api:latest

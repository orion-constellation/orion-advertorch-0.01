# Stage 1: Synthetic Traffic Generator
# Stage 1: API Server
FROM python:3.11-slim AS api-server

# Set the working directory in the container
WORKDIR /app/api

# Only copy the API server component from the previous stage
COPY . /app/api

# Install only the necessary packages for the API server
COPY ./requirements.txt /app/api
RUN pip install -r requirements.txt

# Expose the port the API server listens on
EXPOSE 8080

# Command to start the API server
CMD ["uvicorn", "server:main", "--host", "0.0.0.0", "--port", "8000"]

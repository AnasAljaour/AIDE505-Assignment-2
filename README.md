# Running Flask and Node.js Services with Docker Compose

This guide provides step-by-step instructions on how to build and run the Flask and Node.js services using Docker Compose.

---

## Prerequisites

Ensure you have the following installed on your system:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/install/)

To verify installation, run:

```sh
docker --version
docker-compose --version
```

---

## Building and Running the Services
###  Build and Start Containers
Run the following command in the project root:
```sh
docker-compose up --build
```
This will:
- Build the Flask API and Node.js server images.
- Start the containers for both services.

## Stopping the Services
### To stop all running services:
```sh
docker-compose down
```
---

## Note:
- Make sure Docker and Docker Compose are installed before proceeding.
- The Node.js server is running at https://localhost:3000.
- The Flask API is not directly accessible, as it is only communicating with the Node.js server.

# Interval Merger Service

## Description

This FastAPI web service merges a set of intervals considering exclusions and returns non-overlapping intervals in sorted order.

## Usage

1. Clone the repository.

```bash
git clone <repository_url>
cd <project_directory>
```
2. Build and run the Docker container.
```bash
docker-compose up --build backend-app
```

3. Access the service at http://localhost:8000/docs for Swagger documentation.

4. Use the /api/v1/merge_intervals endpoint to merge intervals.

# Example 1 Request:

```json
{
    "includes": [{"start": 10, "end": 100}],
    "excludes": [{"start": 20, "end": 30}]
}
```
# Example 1 Response:

```json
[
    [{"start": 10, "end": 19},
    {"start": 31, "end": 100}]
]
```

# Example 2 Request:

```json
{
    "includes": [{"start": 10, "end": 100}, {"start": 200, "end": 300}, {"start": 400, "end": 500}],
    "excludes": [{"start": 110, "end": 120}, {"start": 350, "end": 450}]
}
```
# Example 2 Response:

```json
[
    [{"start": 10, "end": 100}, {"start": 200, "end": 300}, {"start": 451, "end": 500}]
]
```

## Docker and Dependencies
Docker is used for containerization.
FastAPI and Uvicorn for the web service.
Pydantic for data validation.
PyTest for unit testing

## Project Structure
main.py: FastAPI application.
models/intervals.py: Pydantic models for data validation.
handlers/mergehandler.py: Handles the set differnece algorithm.
utils/transformers.py: Helper functions for data transformation.
deployment/Docker/backend-app-Dockerfile: Docker configuration file for application.
deployment/Docker/test-Dockerfile: Docker configuration file for application.
deployment/kubernetes/deployment.yml: K8s deployment configuration.
deployment/kubernetes/service.yml: K8s service configuration.
docker-compose.yml: Docker Compose configuration file.

## API Endpoint
`POST /api/v1/merge_intervals`: Accepts a set of intervals with exclusions and returns merged intervals.
`GET /api/healthchecker` : Indicating the the liveness of the web service.


# Running tests
To run unit test, we provide a Dockerfile and a docker compose service to set up test enviroment and start laucnhing test suits
```bash
docker compose up --build tests
```

# Deployment with Kubernetes

To deploy the Interval Merger Service on Kubernetes, we provide Kubernetes manifest files for the backend service.

## Prerequisites

Make sure you have [Minikube](https://minikube.sigs.k8s.io/docs/start/) and [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) installed on your machine.

## Start Minikube Cluster

```bash
minikube start
```

## Deployment

Apply the Kubernetes Deployment and Service manifest files:

### Deployment

```bash
cd deployment/kubernetes
kubectl apply -f='deployment/kubernetes/deployment.yml' 
```
### Service

```bash
cd deployment/kubernetes
kubectl apply -f='deployment/kubernetes/service.yml'
```
This will deploy the backend-app Service on your Minikube cluster.

## Accessing the Service

To access the service, you can use the Minikube IP and the NodePort allocated to the service. Retrieve the Minikube IP with:

```bash
minikube ip` 
```
Find the NodePort for the backend-app-service:

```bash
kubectl get services` 
```
## Using Docker image from Harbor
Latest image is available at [mtiraouidhia515/kub-backend-app](https://hub.docker.com/repository/docker/mtiraouidhia515/kub-backend-app/general)

Now, you can access the service at `http://<minikube_ip>:<backend-app-service_nodeport>/api/v1/merge_intervals` for Swagger documentation.
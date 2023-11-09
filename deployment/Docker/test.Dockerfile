FROM python:3.9-slim

WORKDIR /test-app

COPY deployment/Docker/test-requirements.txt .

RUN pip install --no-cache-dir -r test-requirements.txt

COPY src/ .
COPY tests/ .

ENV APP_ADDRESS=http://app:8000

CMD [ "pytest", "/test-app" ]

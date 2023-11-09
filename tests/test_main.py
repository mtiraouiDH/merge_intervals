import json
from fastapi.testclient import TestClient
from main import app
import os

app_address = os.environ['APP_ADDRESS']
client = TestClient(app)

def test_merge_intervals_Example_1():
    includes = [{"start": 10, "end": 100}]
    excludes = [{"start": 20, "end": 30}]
    payload = {"includes": includes, "excludes": excludes}

    response = client.post(app_address + "/api/v1/merge_intervals", json=payload)
    assert response.status_code == 200

    result = response.json()
    assert result == [{"start": 10, "end": 19}, {"start": 31, "end": 100}]

def test_merge_intervals_Example_2():
    includes = [{"start": 50, "end": 5000}, {"start": 10, "end": 100}]
    excludes = []
    payload = {"includes": includes, "excludes": excludes}

    response = client.post(app_address + "/api/v1/merge_intervals", json=payload)
    assert response.status_code == 200

    result = response.json()
    assert result == [{"start": 10, "end": 5000}]

def test_merge_intervals_Example_3():
    includes = [{"start": 200, "end": 300}, {"start": 50, "end": 150}]
    excludes = [{"start": 95, "end": 205}]
    payload = {"includes": includes, "excludes": excludes}

    response = client.post(app_address + "/api/v1/merge_intervals", json=payload)
    assert response.status_code == 200

    result = response.json()
    assert result == [{"start": 50, "end": 94}, {"start": 206, "end": 300}]

def test_merge_intervals_Example_4():
    includes = [{"start": 200, "end": 300}, {"start": 10, "end": 100}, {"start": 400, "end": 500}]
    excludes = [{"start": 410, "end": 420}, {"start": 95, "end": 205}, {"start": 100, "end": 150}]
    payload = {"includes": includes, "excludes": excludes}

    response = client.post(app_address + "/api/v1/merge_intervals", json=payload)
    assert response.status_code == 200

    result = response.json()
    assert result == [{"start": 10, "end": 94}, {"start": 206, "end": 300}, {"start": 400, "end": 409}, {"start": 421, "end": 500}]

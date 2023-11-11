import json
from fastapi.testclient import TestClient
from main import app
import os

app_address = os.environ['APP_ADDRESS']
client = TestClient(app)

def test_liveness():
    response = client.get(app_address + "/api/healthchecker")
    assert response.status_code == 200

    result = response.json()
    assert result == {"message": "The API is LIVE!!"}

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

def test_merge_intervals_Complex_1():
    includes = [{"start": 10, "end": 100}, {"start": 200, "end": 300}, {"start": 400, "end": 500}]
    excludes = [{"start": 110, "end": 120}, {"start": 350, "end": 450}]
    payload = {"includes": includes, "excludes": excludes}

    response = client.post(app_address + "/api/v1/merge_intervals", json=payload)
    assert response.status_code == 200

    result = response.json()
    assert result == [{"start": 10, "end": 100}, {"start": 200, "end": 300}, {"start": 451, "end": 500}]

def test_merge_intervals_Complex_2():
    includes = [{"start": 1, "end": 10}, {"start": 15, "end": 20}, {"start": 30, "end": 40}, {"start": 50, "end": 60}]
    excludes = [{"start": 12, "end": 18}, {"start": 25, "end": 35}, {"start": 42, "end": 55}]
    payload = {"includes": includes, "excludes": excludes}

    response = client.post(app_address + "/api/v1/merge_intervals", json=payload)
    assert response.status_code == 200

    result = response.json()
    assert result == [{"start": 1, "end": 10}, {"start": 19, "end": 20}, {"start": 36, "end": 40}, {"start": 56, "end": 60}]

def test_merge_intervals_Complex_3():
    includes = [{"start": 1, "end": 1000}]
    excludes = [{"start": 200, "end": 300}, {"start": 400, "end": 500}, {"start": 600, "end": 700}]
    payload = {"includes": includes, "excludes": excludes}

    response = client.post(app_address + "/api/v1/merge_intervals", json=payload)
    assert response.status_code == 200

    result = response.json()
    assert result == [{"start": 1, "end": 199}, {"start": 301, "end": 399}, {"start": 501, "end": 599}, {"start": 701, "end": 1000}]

def test_merge_intervals_Complex_4():
    includes = []
    excludes = [{"start": 200, "end": 300}, {"start": 400, "end": 500}, {"start": 600, "end": 700}, {"start": 900, "end": 950}]
    payload = {"includes": includes, "excludes": excludes}

    response = client.post(app_address + "/api/v1/merge_intervals", json=payload)
    assert response.status_code == 200

    result = response.json()
    assert result == []

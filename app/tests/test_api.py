from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_predict():
    response = client.post("/predict", json={
        "Pclass": 3,
        "Sex": 0,
        "Age": 22,
        "SibSp": 1,
        "Parch": 0,
        "Fare": 7.25,
        "Embarked": 0
    })
    assert response.status_code == 200
    assert response.json()["survived"] in [0, 1]
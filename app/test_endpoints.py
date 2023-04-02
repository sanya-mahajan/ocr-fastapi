#testin api endpts
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_home_view():
    response = client.get("/")  #requests.get like
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/html; charset=utf-8"
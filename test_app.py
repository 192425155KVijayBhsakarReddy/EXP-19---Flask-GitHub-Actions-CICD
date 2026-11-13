import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    """Test the root endpoint returns status 200 and correct JSON structure"""
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "healthy"
    assert "Flask CI/CD Microservice" in json_data["app"]

def test_status_endpoint(client):
    """Test the /api/status endpoint"""
    response = client.get('/api/status')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["environment"] == "Production"

def test_health_check(client):
    """Test health check route"""
    response = client.get('/health')
    assert response.status_code == 200


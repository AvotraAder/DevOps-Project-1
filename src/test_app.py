from fastapi.testclient import TestClient
from app import app 

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    
    assert "Déploiement Réussi" in response.text

def test_get_status():
    response = client.get("/api/status")
    assert response.status_code == 200
    
    assert response.json() == {"status": "online", "message": "L'API est prête à recevoir des requêtes JSON !"}

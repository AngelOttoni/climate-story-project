import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Testa a rota da página inicial"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'<!DOCTYPE html>' in response.data  # Checa se contém a tag HTML da página

def test_get_co2_data(client):
    """Testa a rota que retorna dados de CO2"""
    response = client.get('/api/co2data')
    assert response.status_code == 200
    assert b'CO2 data' in response.data

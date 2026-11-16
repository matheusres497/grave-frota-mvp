# Testes unitarios

from app import app, calcular_revisao

def test_config():
    assert app is not None

def test_calculo_revisao():
    assert calcular_revisao(150000, 144000) == True
    assert calcular_revisao(146000, 144000) == False

def test_rota_principal():
    response = app.test_client().get('/')
    assert response.status_code == 200

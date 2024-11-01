import pytest
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, MagicMock
from jarvas_api_discord.main import app, client 
from jarvas_api_discord.settings import load_config_general_id_channel

test_client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_discord_methods(mocker):
    mocker.patch.object(client, 'send_simple_message', new=AsyncMock(return_value=True))
    mocker.patch.object(client, 'send_embed_message', new=AsyncMock(return_value=True))
    # mocker.patch.object(client, 'wait_until_ready', new=AsyncMock())

def test_send_discord_message():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"detail": "Mensagem enviada com sucesso!"}
    client.send_simple_message.assert_called_once_with("a aplicação está em teste")

def test_send_custom_message():
    response = test_client.post(
        "/",
        json={
            "name": "Nome app de teste",
            "message": "essa é uma mensagem do app",
            "id_channel": load_config_general_id_channel()
        }
    )
    assert response.status_code == 200
    assert response.json() == {"detail": "Mensagem enviada com sucesso!"}

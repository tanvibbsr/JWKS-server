from fastapi.testclient import TestClient # type: ignore
from app import app

client = TestClient(app)


def test_jwks_returns_keys():
    r = client.get("/jwks")
    assert r.status_code == 200
    data = r.json()
    assert "keys" in data
    assert len(data["keys"]) >= 1


def test_auth_returns_token():
    r = client.post("/auth")
    assert r.status_code == 200
    assert "token" in r.json()


def test_auth_expired_returns_token():
    r = client.post("/auth?expired=true")
    assert r.status_code == 200
    assert "token" in r.json()


def test_jwks_only_active_keys():
    r = client.get("/jwks")
    keys = r.json()["keys"]
    for k in keys:
        assert "kid" in k
        assert k["kty"] == "RSA"

import time
import jwt # type: ignore
from fastapi import FastAPI, Query # type: ignore
from fastapi.responses import JSONResponse # type: ignore

from keys import generate_rsa_keypair, get_active_keys, get_expired_keys
from jwk_utils import public_key_to_jwk

app = FastAPI()

# Generate one valid + one expired key at startup
valid_key = generate_rsa_keypair(expiry_seconds=3600)
expired_key = generate_rsa_keypair(expiry_seconds=-3600)


@app.get("/jwks")
def jwks():
    active = get_active_keys()

    jwks_keys = [
        public_key_to_jwk(k["public_key"], k["kid"])
        for k in active
    ]

    return {"keys": jwks_keys}


@app.post("/auth")
def auth(expired: bool = Query(False)):
    if expired:
        key = get_expired_keys()[0]
    else:
        key = get_active_keys()[0]

    now = int(time.time())

    payload = {
        "sub": "fake-user",
        "iat": now,
        "exp": key["expiry"]
    }

    token = jwt.encode(
        payload,
        key["private_key"],
        algorithm="RS256",
        headers={"kid": key["kid"]}
    )

    return JSONResponse({"token": token})

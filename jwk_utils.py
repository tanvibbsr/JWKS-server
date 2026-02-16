import base64


def b64url_uint(val: int) -> str:
    data = val.to_bytes((val.bit_length() + 7) // 8, "big")
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def public_key_to_jwk(public_key, kid: str):
    numbers = public_key.public_numbers()

    return {
        "kty": "RSA",
        "use": "sig",
        "alg": "RS256",
        "kid": kid,
        "n": b64url_uint(numbers.n),
        "e": b64url_uint(numbers.e),
    }

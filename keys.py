import time
import uuid
from cryptography.hazmat.primitives.asymmetric import rsa # type: ignore

KEYS = []

def generate_rsa_keypair(expiry_seconds: int):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    kid = str(uuid.uuid4())
    expiry = int(time.time()) + expiry_seconds

    key_record = {
        "kid": kid,
        "private_key": private_key,
        "public_key": private_key.public_key(),
        "expiry": expiry
    }

    KEYS.append(key_record)
    return key_record


def get_active_keys():
    now = int(time.time())
    return [k for k in KEYS if k["expiry"] > now]


def get_expired_keys():
    now = int(time.time())
    return [k for k in KEYS if k["expiry"] <= now]

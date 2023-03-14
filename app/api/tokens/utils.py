import secrets
import string
import hashlib


def generate_unique_hash():
    letters = string.ascii_letters + "1234567890"
    rand_string = ''.join(secrets.choice(letters) for _ in range(20))
    hash_rand_string = hashlib.sha256(rand_string.encode("utf-8")).hexdigest()
    return hash_rand_string

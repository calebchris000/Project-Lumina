import bcrypt


async def hash_password(password: str):
    if not password:
        return None
    password_bytes = password.encode("utf-8")
    salt = bcrypt.gensalt(rounds=12)
    hashed_password = bcrypt.hashpw(password=password_bytes, salt=salt)

    return str(hashed_password)


async def verify_hash(password: str, hash: str):
    if not hash:
        return False

    password_bytes = password.encode("utf-8")
    match = bcrypt.checkpw(password=password_bytes, hashed_password=hash)
    return match

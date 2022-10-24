import hashlib

BLOCKSIZE = 4096

def get_sha256(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        for block in iter(lambda: f.read(BLOCKSIZE), b""):
            sha256.update(block)

    return sha256.hexdigest()


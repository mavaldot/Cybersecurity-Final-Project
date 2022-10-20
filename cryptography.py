
BLOCK_SIZE = 4096

def sha256(filepath):
    with open(filepath, 'rb') as f:
        block = f.read(BLOCK_SIZE)
        print(block)
        while block:
            block = f.read(BLOCK_SIZE)
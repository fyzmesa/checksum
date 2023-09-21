import hashlib

def calculate_checksum(filename, hash_algorithm='md5'):
    hash_func = getattr(hashlib, hash_algorithm)()
    with open(filename, 'rb') as file:
        for chunk in iter(lambda: file.read(4096), b''):
            hash_func.update(chunk)
    return hash_func.hexdigest()

filename = 'checksum.py'

checksum = calculate_checksum(filename)

print(f"Checksum of '{filename}' is: {checksum}")

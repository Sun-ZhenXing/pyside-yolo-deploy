from hashlib import sha256

res = sha256("hello world".encode())
print(res.hexdigest())

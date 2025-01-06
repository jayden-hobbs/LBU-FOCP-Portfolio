import hashlib

message = "jayden"
md5_hash = hashlib.md5(message.encode()).hexdigest()
print(message)
print(md5_hash)

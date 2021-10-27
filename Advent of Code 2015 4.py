import hashlib
text = "yzbqklnj"
hash_object = hashlib.md5(text.encode())
md5_hash = hash_object.hexdigest()
no = 0
howmany='000000'
while md5_hash.startswith(howmany)== False:
    hash_object = hashlib.md5((text+str(no)).encode())
    md5_hash = hash_object.hexdigest()
    no+=1


print(text+str(no-1))
print(md5_hash)
import rsa

public_key, private_key = rsa.newkeys(512)

print(public_key)
print(private_key)

file = open("myfile.txt", "r")
info = file.readlines()
file.close()

info = info.join()

cipher_text = rsa.encrypt(info.encode(), public_key)

file = open("myfile.txt", 'w')
file.write(info)
file.close()

print(cipher_text)

plain_text = rsa.decrypt(cipher_text, private_key)
print(plain_text)




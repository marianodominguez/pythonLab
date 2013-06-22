from string import maketrans, translate

decoded=""

f = open("ocr.txt")
for line in f:
    clean= "".join([c for c in line if c not in "!@#$%^&*()_+{}[]\n"])
    if clean != "": 
        decoded += clean;

print decoded

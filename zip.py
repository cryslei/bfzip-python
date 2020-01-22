import zipfile

nome  = 'senhassss.zip'
word = 'wordlist.txt'
wordlist = open(word,'r')
wordlist = wordlist.readlines()

zFile = zipfile.ZipFile(nome)
for w in wordlist:
    w = w.strip("\n")
    try:
        zFile.extractall(pwd=bytes(w,'utf-8')) 
    except RuntimeError:
        print("testando a senha: ", w)







'''
nome  = 'admincomp.zip'

while True:
    ar = zipfile.ZipFile(nome, mode='r')
    senha = ar.namelist()[0].split('.')[0]

    print(ar.namelist())

    zFile = zipfile.ZipFile(nome)
    zFile.extractall(pwd=bytes(senha,'utf-8'))
    nome = str(senha+'.zip')
'''

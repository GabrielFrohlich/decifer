import csv
from itertools import permutations

alpha = "abcdefghijklmnopqrstuvwxyz"
file = open('palavras.csv', 'r', encoding="UTF-8")
reader = csv.reader(file)

words = list()

for row in reader:
    words.append(row[0])

def caesar():
    encrypted = input("Digite a palavra codificada: ")

    for char_index in range(len(alpha)):
        decrypted = ''
        for index, character in enumerate(encrypted):
            alpha_index = alpha.find(character)
            decrypted += alpha[(alpha_index - char_index) % len(alpha)]
        if decrypted in words:
            print("Possível resultado: {} | Chave: {}".format(decrypted, char_index))

def decifra_vigenere(key, enc):
    final = ""
    for index in range(0,len(enc)):
        final += alpha[((alpha.index(enc[index]) - alpha.index(key[index])) + 26)%26]

    if final in words:
        print("Chave possível: {} Decifrado: {}".format(key[0:3], final))
        return final
    else:
        return 0

def vigenere():
    encrypted = input("Digite a palavra codificada: ")
    finded= 0
    
    for rnd_tpl in permutations(alpha, 3):
        rnd_str = ''.join(rnd_tpl)
        
        key = ""

        for enc_part in range(0, (len(encrypted)//3)+1):
            key += rnd_str
        
        key = "{s:.{size}}".format(s=key, size=len(encrypted))
        if('key' in key):
            print(key)
        result = decifra_vigenere(key, encrypted)

        if result != 0:
            finded += 1

    if finded == 0:
        print("Não foram encontradas chaves compatíveis com o texto inserido.")




print("""
______          _  __               
|  _  \        (_)/ _|              
| | | |___  ___ _| |_ _ __ ___ _ __ 
| | | / _ \/ __| |  _| '__/ _ \ '__|
| |/ /  __/ (__| | | | | |  __/ |   
|___/ \___|\___|_|_| |_|  \___|_|   
""")

print("""
..............................
: 1 - Decifrador de Caesar   :
: 2 - Decifrador de Vigenere :
:............................:
""")

option = input("Digite a opção desejada: ")

match option:
    case '1':
        caesar()
    case '2':
        vigenere()
    case other:
        print("Digite 1 ou 2!")
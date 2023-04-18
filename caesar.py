import csv
import os

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

def vigenere():
    print("Vigenere")



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
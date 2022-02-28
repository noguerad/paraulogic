#! /usr/bin/python3
import re
import requests

dicts = ["diccionari1.txt", "diccionari2.txt"]
obligatori = 'n'
lletres = ['t', 'ç', 'r', 'a', 'l', 'u', 'n']
netes = []
final = "final.txt"

def busca(arxiu):
    paraules = open(arxiu, "r")
    for x in paraules:
        paraula = re.sub('[^a-zA-Z]+', '', x)
        temp = 0
        if (obligatori in paraula):
            for i in paraula:
                if (i in lletres):
                    temp = temp + 1
                else:
                    temp = temp - 1
            if (temp == len(paraula)):
                netes.append(paraula)
    paraules.close()

for i in dicts:
    busca(i)

finals = list(dict.fromkeys(netes))

guarda = open(final, "a")
contador = 0
for i in finals:

    url = 'https://dlc.iec.cat/Results?DecEntradaText=' + i
    r = requests.get(url)
    web = r.text
    hies = web.find('0 registres')

    if (hies > 0):
        print(i, '-> No hi es')
    else:
        guarda.write(i + "\n")
        contador = contador + 1
guarda.close()

print("Total trobades: ", contador)

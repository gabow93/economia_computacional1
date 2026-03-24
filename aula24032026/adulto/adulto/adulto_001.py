""""
Programa adulto
Descricao: Este programa pergunta a idade de uma pessoa. Se a idade for maior do que 18 anos, o programa mprime na tela 'Oi, voce eh um adulto.'. Caso contrário, imprime: 'Oi, vc é menor de idade.'
Data: 24/03/2026
Versao: 0.0.1
"""


# Aloc de mem

age = 0
txt = ""




# Input

age = int(input('\n Qual a sua idade?'))




# Process. dados

if age >= 18:
    txt = 'Oi! Vc é um adulto'
else:
    txt = "Oi! Vc é menor de idade"




# Output

print(txt)

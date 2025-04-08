'''Crie um programa que leia o nome completo de uma pessoa e mostre:
    – O nome com todas as letras maiúsculas e minúsculas.
    – Quantas letras ao todo (sem considerar espaços).
    – Quantas letras tem o primeiro nome.
'''
# name = str(input("Digite seu nome: "))
# nameMin = name.lower()
# nameMax = name.upper()
# quantLetras = len(name.replace(" ", ""))
# #Troca o espaço (representado por " ") por um não espaço "", usado na função replace()
# firstName = len(name.split()[0])

# print(name)
# print(f"Seu nome todo em letras minúculas: {nameMin}.\nSeu nome em letras maiúsculas: {nameMax}.\nSeu nome {quantLetras} letras.\nSeu primeiro nome tem {firstName} letras.")

"""Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”"""
# cidade = str(input("Digite o nome da cidade: ")).strip()
# print(cidade[0:5].capitalize() == 'Santo') 

# Estou printando a afirmação de se as primeiras cinco letras da cidade digitada são as mesmas de Santo, ou seja, usando o ==, estou dizendo que este prnt será um boolean, retornando True ou False.


"""Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome. """
# fulano = str(input("Qual o seu nome? ")).strip()
# print(f"Seu nome possui Silva? {"Silva" in fulano.title()}")

'''Fazer um código que leia 4 nomes, coloque-os numa lista e selecione um deles aleatoriamente. Depois imprimir a chamada e imprimir uma versão aleatória dela'''
# import random
# first=input('Digite o primeiro nome: ')
# sec=input('Digite o segundo nome: ')
# ter=input('Digite o terceiro nome: ')
# qua=input('Digite o quarto nome: ')
# chamada=[first, sec, ter, qua]
# escolha=random.choice(chamada)
# print(f'\nO Nome escolhido foi {escolha}.')
# print(f'\nOrdem Digitada: {chamada}')
# random.shuffle(chamada)
# print(f'Ordem aleatória: {chamada}')

""" Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez."""

# frase = str(input("Digite sua frase: ")).strip().upper()
# quantA = frase.count("A")
# firstA = frase.find("A")+1 # Procura o primeiro elemento dentro da função find()
# lastA = frase.rfind("A")+1 # o rfind() lÊ a string da direita para a esquerda
# +1
# print(f"A letra A apareceu {quantA} vezes.\nEla apareceu pela primeira vez na posição {firstA}.\nEla aparceu pela última vez na posição {lastA}.")

""" Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente."""

# nome = str(input("Digite seu nome completo: ")).strip().title()
# slicedName = nome.split() # Função split() "fatia" o elemento pelos espaços que ele possui e cria um array. Exemplo prático: se eu escrevo João Pessoa, ele criará um array: slicedName = ['João', 'Pessoa']
# firstName = slicedName[0]
# lastName = slicedName[len(slicedName) -1] # último nome será o array slicedName, na posição de seu tamanho total -1. O motivo é que um array de três elementos possui as posições (0, 1, 2), mas seu tamanho sempre será 3; portanto, o nome estará na posição 2 (se for um nome com três elementos) e não na posição 3, sendo necessário colocar um -1.

# print(f"Olá {nome}\nSeu primeiro nome é {firstName}.\nSeu último nome é {lastName}")
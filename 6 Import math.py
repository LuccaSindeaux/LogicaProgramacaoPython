import math

'''AULA EM SI'''
# num = float(input("Digite um número: "))
# raiz=math.sqrt(num)
# fat=math.factorial(raiz)
# print(f"A raiz quadrada do número é {raiz:.2f}")
# print(f"O fatorial da raiz quadrada é {fat}")

'''EXERCÍCIO 16: Fazer um código que leia um número real qualquer e devolva sua versão inteira.'''
# x=float(input("Digite um número real: "))
# inteiro=math.trunc(x)
# print(f"A porção inteira deste nnúmero é: {inteiro}")

'''EXERCÍCIO 17: Fazer um programa que leia dois catetos de um triângulo retângulo hipotético e calcule sua hipotenusa.'''
# print("Considere que você quer descobrir o valor da hipotenusa de um trângulo retângulo qualquer, digite abaixo os valores dos catetos que este programa, ao ser executado, iurá lhe devolver o resultado da hipotenusa.")
# cat1=float(input("Digite o valor do primeiro cateto: "))
# cat2=float(input('Digite o valor do segundo cateto: '))
# hipo=math.sqrt((cat1**2 + cat2**2)) #OUTRO MÉTODO: hipo=math.hypot(cat1, cat2)
# print(f'A hipotenusa é: {hipo}')
'''EXERCÍCIO 18: Fazer um código que leia um valor de ângulo e que retorne seu seno, cosseno e tangente.'''
# ang=float(input("Digite um ângulo qualquer: "))
# rad=math.radians(ang)#o Python só fará o código se o valor do ângulo estiver em radianos, sendo necessário converter primeiro
# sen=math.sin(rad)
# cos=math.cos(rad)
# tan=math.tan(rad)
# print(f'O valores são:\n Seno: {sen:.2f}\n Cosseno: {cos:.2f}\n Tangente: {tan:.2f}')

'''EXERCÍCIO 19 e 20: Fazer um código que leia 4 nomes, coloque-os numa lista e selecione um deles aleatoriamente. Depois imprimir a chamada e imprimir uma versão aleatória dela'''
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

'''EXERCÍCIO 21: IMPORTANDO MÚSICA:
import pygame
pygame.init()
pygame.mixer.music.load('arquivo.mp3')
pygame.mixer.music.play()'''

'''EXERCÍCIO 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
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

'''EXERCÍCIO 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

# numero = int(input("Digite um número de 0 a 9999: "))
# unidade = numero % 10    # Lembarndo que % --> devolve o resto da divisão
# dezena = (numero // 10) % 10 # --> divide o num por 10, pega o resto, e o divide por 10, pegando o resto da divisão e atribuindo ele a variável dezena
# centena = (numero // 100) % 10 # --> Mesma lógica, porém com 100 já que busco a centena
# milhar = (numero // 1000) % 10

# print(f"Unidade: {unidade}")
# print(f"Dezena: {dezena}")
# print(f"Centena: {centena}")
# print(f"Milhar: {milhar}")

# Se colocar o número 1234, e pedir a centena, ele dividirá por 100, o que dará 12.34, consideremos 12, então subsquente,emte dividimos por 10, daria um resultado de divisão de 1 com resto 2, quando usamos o "%" estamos pegando justamente este resto. 

# Caso o número fosse um que não possui milhar, como 123, ele irá dividir por 1000, o que daria 0,1234, consideremos 0, já que estamos mexendo com inteiros neste código. 0 dividido por qualquer número é 0, o resultado da visão será 0 e seu resto também. 

"""EXERCÍCIO 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”"""
# cidade = str(input("Digite o nome da cidade: ")).strip()
# print(cidade[0:5].capitalize() == 'Santo') 

# Estou printando a afirmação de se as primeiras cinco letras da cidade digitada são as mesmas de Santo, ou seja, usando o ==, estou dizendo que este prnt será um boolean, retornando True ou False.


"""EXRCÍCIO 25: Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome. """
fulano = str(input("Qual o seu nome? ")).strip()
print(f"Seu nome possui Silva? {"Silva" in fulano.title()}")
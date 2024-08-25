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

'''IMPORTANDO MÚSICA:
import pygame
pygame.init()
pygame.mixer.music.load('arquivo.mp3')
pygame.mixer.music.play()'''



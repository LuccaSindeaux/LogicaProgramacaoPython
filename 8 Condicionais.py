"""Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""
# from time import sleep
# from random import randint

# print("=-"*20)
# print("           JOGO DE ADVINHAÇÃO")
# print("=-"*20)

# num = int(input("Digite um número inteiro entre 0 e 5! "))
# pcsChoice = randint(0,5)

# print("PENSANDO...")
# sleep(2) # slep da biblioteca time recebe um int que é a quantidade de segundos que o computador não lerá os códigos

# if num == pcsChoice:
#     print("PARABÉNS! Você me derrotou.")
# else:
#     print(f"Ooops, eu venci, minha escolha foi {pcsChoice}")

# """
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
# """

# velocidade = float(input("A quantos km/h está o carro? "))
# multa = (velocidade - 80) * 7
# if velocidade > 80:
#     print(f"Você receberá uma multa, no valor de {multa} reais.")
# else:
#     print("Não há com o que se preocupar, você estava dentro dos limites de velocidade.")

'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
first = int(input("Digite o primeiro número: "))
sec = int(input("Digite o segundo número: "))
third = int(input("Digite o terceiro número: "))

menor = first
if first > sec and third > sec:
    menor  = sec
if first > third and sec > third:
    menor = third

maior = first
if sec > first and sec > third:
    maior = sec
if third > first and third > sec:
    maior = third

print(f"O maior número digitado foi {maior}.\nO menor número digitado foi {menor}")
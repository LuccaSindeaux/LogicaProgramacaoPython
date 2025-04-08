"""Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu."""
from time import sleep
from random import randint

print("=-"*20)
print("           JOGO DE ADVINHAÇÃO")
print("=-"*20)

num = int(input("Digite um número inteiro entre 0 e 5! "))
pcsChoice = randint(0,5)

print("PENSANDO...")
sleep(2) # slep da biblioteca time recebe um int que é a quantidade de segundos que o computador não lerá os códigos

if num == pcsChoice:
    print("PARABÉNS! Você me derrotou.")
else:
    print(f"Ooops, eu venci, minha escolha foi {pcsChoice}")

"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""
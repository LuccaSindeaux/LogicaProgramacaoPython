""" Simulado treinando
Faça um algoritmo que leia vários números inteiros quaisquer entre 10 e 100.
Utilize as seguintes variáveis: listaA, listaB e listaC
Para cada número inteiro lido, verificar: 
Caso o número seja negativo, dar a seguinte mensagem: "Digite apenas números positivos" e ler o próximo.
Caso o número digitado seja 0(zero), ou a quantidade digitada seja 20 números, finalize a digitação e mostre o conteúdo das 3 listas, imprimindo os elementos de cada lista individualmente juntamente com sua posição na lista.
Caso o número seja positivo faça o seguinte:
- Se o número está entre 20 e 40 adicione esse número na listaA.
- Se o número está entre 50 e 70 adicione esse número na listaB.
- Se o número está entre 30 e 60 adicione esse número na listaC.
- Quando alguma das listas estiver com 5 elementos, apague todos os elementos desta lista específica.
"""
listaA=[]
listaB=[]
listaC=[]

interaction=0

while True:
    interaction+=1
    numero=int(input("Digite um número entre 10 e 100: "))
    if numero == 0 or interaction==20:
        interaction-=1
        break
    if numero<0:
        print("Digite apenas números positivos.")
        interaction-=1
        continue

    if numero >= 10 or numero <= 100:
        pass
        if numero>=20 and numero<=40:
            listaA.append(numero)
        
        if numero>=50 and numero<=70:
            listaB.append(numero)
        
        if numero>=30 and numero<=60:
            listaC.append(numero)
        
        if len(listaA)==5:
            listaA.clear() #função .clear apaga todos os elementos de uma lista 
        if len(listaB)==5:
            listaB.clear()
        if len(listaC)==5:
            listaC.clear()
    else:
        print("Favor digitar um número entre 10 e 100.")


print("lista A:")
for indice in range(len(listaA)):
    print(f"Indice: {indice} Elemento: {listaA[indice]}")
print("lista B: ")
for indice in range(len(listaB)):
    print(f"índice: {indice}, elemento: {listaB[indice]}")
print("lista C: ") 
for indice in range(len(listaC)):
    print(f"índice: {indice}, elemento: {listaC[indice]}")


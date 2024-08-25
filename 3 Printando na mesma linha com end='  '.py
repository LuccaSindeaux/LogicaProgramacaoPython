'''PRINTANDO NA MESMA LINHA'''
x=int(input("Digite um número: "))
y=int(input("Digite outro número: "))
z=(x+y)
print(f"O primeiro número é {x}", end=' ') #usandpo end=' ' depois de uma vírgula que finzaliza uma string, ele colocará o próximo print na mesma linha, este end poderia ser algo como end=>>>>
print(f"O segundo número é {y}", end=' ')
print(f"A soma entre os números é {z}")
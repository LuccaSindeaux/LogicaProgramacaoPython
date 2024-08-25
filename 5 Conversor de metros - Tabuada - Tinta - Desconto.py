'''Faça um código que leia um valor em metros e converta ele em Centímetros e Milimetros'''

# medida=float(input("Digite o valor em metros que você deseja convereter: "))
# cm=medida*100
# mm=medida*1000
# print(f"O valor em Centímetros é {cm}cm. \nO valor em milimetros é {mm}mm.")

#OUTRA FORMA DE RESOLVER 
# print(f"O valor em Centímetros é {medida*100}cm. \nO valor em milimetros é{medida*1000}mm.")

'''TABUADA'''
# num=int(input("Digite um número INTEIRO: "))
# print(f"A tabuada deste número é\n1) {num}\n2) {num*2}\n3) {num*3}") #código tá funcionando, é só seguir essa lógica até fecha 10. 

'''TINTAS:
Sabendo que um litro de tinta pinta uma área de 2m², faça um código que leia uma altura e a uma largura de uma parede e defina quantos litros o pintor vai usar para pintar tal parede.'''

# x=int(input("Qual é a largura em metros da parede? "))
# y=int(input('Qual é a altura em metros da parede? '))
# area=x*y
# print(f"A área da parede é {area}, serão necessários {area//2+area%2} litros de tinta.")

'''DESCONTO:
Uma loja está fazendo desconto de 5% de alguns produtos, fazer um código que leia um preço e devolva o valor dele com o desconto.'''
preco=float(input("Digite o preço do produto: "))
desc=(5*preco)/100
print(f"O valor do produto com o desconto de 5% é {preco-desc :.2f} reais.")
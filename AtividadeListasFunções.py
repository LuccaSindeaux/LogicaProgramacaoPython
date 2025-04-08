"""
Competências a serem avaliadas:
- Conhecer os comandos da linguagem
- Saber utilizar os comandos corretamente
- Desenvolver uma solução viável para a atividade proposta
- Códigos iguais = D

Faça um algoritmo que leia o nome, a idade e o genero
de pelo menos 5 pessoas.
OBS: para o gênero aceitar a digitação apenas de F ou M.

Armazene esses dados nas listas: lst_nome, lst_idade e lst_genero.
Encerre a digitação quando for digitado a palavra 'fim' no nome da
pessoa.
Após imprima as seguintes informações:
-> Média de idades das pessoas
-> Nome da pessoa mais velha
-> Percentual de pessoas do gênero Feminino

"""
def menu():
    lst_nome = []
    lst_genero = []
    lst_idade = []
    interaction = 0
    while True:
        nome = input("Digite seu nome: ")
        lst_nome.append(nome)
        
        idade = int(input("Digite sua idade: "))
        lst_idade.append(idade)
        
        while True:
            gen = input("Digite seu gênero [F/M]: ").upper()
            if gen == "M" or gen == "F":
                lst_genero.append(gen)
                break
            else:
                print("Favor digitar somente M ou F para identificar seu gênero.")

        interaction += 1
        
        if interaction >= 5:
            questao = input("Gostaria de encerrar o programa? (S/N) ").upper()
            if questao == "S":
                print(f"\nA lista de nomes é: {lst_nome}")
                print(f"A lista de idades é: {lst_idade}")
                print(f"Os gêneros são: {lst_genero}")

                def media_idade():
                    return sum(lst_idade) // len(lst_idade)
                
                print(f"A média das idades é {media_idade()}.")

                femeas = lst_genero.count("F")
                feminismo = femeas / len(lst_genero) * 100
                print(f"A porcentagem de mulheres é {feminismo:.2f}%.")

                veterano = max(lst_idade)
                posicao_veterano = lst_idade.index(veterano)
                print(f"A pessoa mais velha é {lst_nome[posicao_veterano]}!")
                break  # encerra o while True

menu()


# """LISTAS"""
# print(f"A lista de nomes é: {lst_nome}")
# print("")
# print(f"A lista de idades é: {lst_idade}")
# print("")
# print(f"Os gêneros são: {lst_genero}")
# print("")
# """MÉDIA DA IDADE"""
# def media_idade():
#     media_idade=sum(lst_idade)//len(lst_idade)
#     return media_idade

# print(f"A média das idades é {media_idade()}.")
# print("")

# """PORCENTAGEM DE MULHERES"""
# femeas=lst_genero.count("F")
# feminismo=femeas/len(lst_genero) * 100
# print(f"A porcentagem de mulheres é {feminismo}.")
# print("")

# """PESSOA MAIS VELHA DA LISTA"""
# veterano=max(lst_idade)
# posicao_veterano=lst_idade.index(veterano)
# print(f"A pessoa mais velha é {lst_nome[posicao_veterano]}!")
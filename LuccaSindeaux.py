"""
Enunciado:

Você foi selecionado para a próxima etapa de um processo de 
seleção para uma vaga de emprego.
Para conquistar a vaga você deverá desenvolver um código
seguindo as instruções abaixo:

Na opção 1, você deverá digitar os dados necessários para
 preencher as listas com nome do aluno, sua idade e seu curso.
 A idade mínima aceita deverá ser 16 anos
 O curso digitado deverá ser um dos cursos da lista lst_cursos_disponiveis
 
Na opção 2, você deverá imprimir um relatório geral para conferência,
 imprimindo o nome do aluno, sua idade e seu curso. 
 Imprima essas informações uma ao lado da outra.
 No final, mostre o total de alunos e quantos alunos estão na faixa etária entre 18 e 25 anos de idade
 
Na opção 3, você deverá possibilitar a troca de curso de um aluno.

Na opção 4, você deverá implementar a exclusão de um aluno da lista,
 retirando também os dados correspondentes a idade e curso deste aluno. 
"""
menu = """
    ================================
    0- Finaliza o código
    1- Adicionar dados
    2- Listar os dados
    3- Alterar o curso de um aluno
    4- Excluir um aluno
    ================================
"""
lst_cursos_diponiveis = ["RDS", "ADS", "PMM", "DADOS", "SPI"]
lst_aluno = []
lst_idade = []
lst_curso = []

def faixa_etaria():
    et=0
    for idade in lst_idade:
        if 18<= idade <=25:
            et +=1
    return et

while True:
    print(menu)
    while True:
        escolha=input("Escolha uma das alternativas: ")
        if escolha not in ["0","1","2","3","4"]:
            print("ERRO!!! Por favor escolher um número válido!")
        else:
            break
#QUEBRA DO PROGRAMA
    if escolha == "0":
        break
#PREENCHIMENTO DOS DADOS DO ALUNO
    if escolha == "1":
        nome=input("Digite o nome do aluno: ")
        lst_aluno.append(nome)
        while True:
            idade=int(input("Digite a idade do aluno: "))
            if idade >=16:
                lst_idade.append(idade)
                break
            else:
                print("O aluno deve ter no mínimo 16 anos de idade.")
        while True:
            curso=input(f"Escolha um dos cursos entre: {lst_cursos_diponiveis}. ").upper()
            if curso in lst_cursos_diponiveis:
                lst_curso.append(curso)
                break
            else:
                print("ERRO!! Curso não identificado...")
#RELATÓRIO
    if escolha == "2":
        for dados in range(len(lst_aluno)):
            print(f"Aluno: {lst_aluno[dados]} Idade: {lst_idade[dados]} Curso: {lst_curso[dados]}")

        print("\nA quantidade alunos incritos é: ", len(lst_aluno))
        print("\nA quantidade de alunos entre 18 e 25 anos é: ", faixa_etaria())
#ALTERAÇÃO DE UM CURSO
    if escolha == "3":
        print(lst_aluno)
        alterar=input("Digite o nome de um dos alunos: ")
        if alterar in lst_aluno:
            while True:
                alt_curso=input(f"Qual novo curso desejado? {lst_cursos_diponiveis}").upper()
                if alt_curso in lst_cursos_diponiveis:
                    new=lst_aluno.index(alterar)
                    lst_curso[new]=alt_curso
                    break
                else:
                    print("ERRO!! Escolha um curso disponível na lista.")
#EXCLUSÃO DE UM ALUNO DA LISTA DE MATRICULADOS
    if escolha == "4":
        print(lst_aluno)
        exclusao=input("Digite o nome do Aluno que deseja que seja excluído: ")
        if exclusao in lst_aluno:
            excluir=lst_aluno.index(exclusao)
            lst_aluno.pop(excluir)
            lst_idade.pop(excluir)
            lst_curso.pop(excluir)
            print(f"O incrito {exclusao} foi removido(a) da lista de inscritos com sucesso.")
        else:
            print("ERRO!! Nome digitadi inválido...")

#MOSTRANDO TODAS AS LISTAS APÓS A DIGITAÇãO DE ZERO NO WHILE 
print("\nListas dos dados:")
print(f"\nAlunos incritos: {lst_aluno}")
print(f"\nIdades dos incritos: {lst_idade}")
print(f"\nCursos escolhidos pelos alunos: {lst_curso}")
opcoes='''
========================
        Opções:
    1- Adicionar algo
    2- Sair
'''

def menu():
    while True:
        print(opcoes)
        escolha=input('Escolha uma opção: ')
        if escolha == '1':
            algo=input('Digite algo: ')
            print(algo)
        elif escolha =='2':
            print('Fazendo Lofoff...')
            break

administradores=['Fábio', 'Lucca', 'Lisiane', 'Butiá', 'Murilin', 'Gugu', 'Ninaya']
senha=['POO', '0409', 'Java', 'minha_terra', 'planeta', 'ohmeu', 'kirby']


def login():
    while True:
        admin=input('Administrador: ')
        if admin in administradores:
            posicao_admin=administradores.index(admin)
            passcode=input('Senha: ')
            if passcode==senha[posicao_admin]:
                print('Login realizado com sucesso!')
                return True
            else:
                print('Senha está incorreta.')
        else:
            print('Administrador não encontrado.')

if login():
    menu()
'''CENTRALIZAÇÃO COM FORMAT'''
nome=input("Qual é seu nome? ")
print('Prazer em te conhecer {:^20}!'.format(nome)) #Printando nome entre 20 espaços
print('Prazer em te conhecer {:=^20}!'.format(nome)) #Printando nome entre 20 espaços com um símbolo no meio
# O : é o caracter a ser impresso e o ^ é a quantidade de vezes que ele será impresso.
# Nom primeiro exemplo não há caracter, e no segundo o caracter é '='.
print('Prazer em te conhecer {:-^20}!'.format(nome))
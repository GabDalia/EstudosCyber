# 1. Sistema de cadastro de clientes + login
# Cadastrar nome, CPF, e-mail 
# Criar usuário e senha
# Fazer login
# Salvar os dados em arquivo
# Não salvar a senha em texto puro ( usar hash )


import bcrypt
from dataclasses import dataclass
#dados do cadatro:
@dataclass
class Cliente:
    nome: str
    cpf: str #para nao perder o 0 do inicio de alguns cpfs
    email: str
    senha: bytes

print('\n......M E N U......\n\n[1] Login\n[2] Criar conta')
while True:
    try:
        opcao=int(input(""))
        if opcao>0 and opcao<3:
            break
        else:
            print('Opção inválida, digite novamente')
    except ValueError:
        print('Opção inválida, digite novamente')
if opcao == 2:
    nome = input('Digite o seu nome: ')
    cpf = input('Digite o seu CPF: ')
    email = input('Digite o seu E-mail: ')#essas variaveis serao usadas como argumento
    while True:
        senha = input('Digite a sua senha: ')
        confirmaSenha = input('Digite sua senha novamente: ')
        if (senha == confirmaSenha):
            print('Cadastro finalizado')
            break
        print('As senhas não coicidem.')

    senha_hash = bcrypt.hashpw(
        senha.encode(),
        bcrypt.gensalt()
    )

    cliente = Cliente(nome,cpf,email,senha_hash)
    with open('clientes.txt', 'a') as arquivo:
        arquivo.write(f'{cliente.nome};{cliente.cpf};{cliente.email};{cliente.senha}\n')

elif opcao == 1:
    digitaCpf = input('Digite o seu CPF: ')
    digitaSenha = input('Digite a sua Senha: ')


    with open('clientes.txt' , 'r') as arquivo:
        encontrou = False
        for linha in arquivo:
            dados = linha.strip().split(';')
            cpf = dados[1]
            if cpf == digitaCpf:
                encontrou = True
                senha_hash = dados[3]
                if bcrypt.checkpw(digitaSenha.encode(),senha_hash.encode()):
                    print('Login realizado com sucesso!')
                else:
                    print('Senha incorreta ')
                break
        if (encontrou == False):
            print('Cpf inválido')

###Adicionar depois: medidor de segurança da senha, cpf inválido(cálculo de cpf), cpf já cadastrado, bloquear temporariamente depois de várias tentativas erradas, registrar tentativas de login
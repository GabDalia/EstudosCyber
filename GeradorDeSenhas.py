import random
import string
print("--------Gerador de senhas--------")
tam = int(input("Escolha o tamanho da senha:\n"))
simb = input("A senha terá símbolos?(S/N)\n").upper()
num = input("A senha terá números?(S/N)\n").upper()


def gerar_senha(tam,simb,num):
  caracteres = string.ascii_letters  #letras
  if (num == 'S'):
    caracteres += string.digits #números
  if (simb == 'S'):
    caracteres += string.punctuation #símbolos  
  senha = " "
  for i in range(0,tam):
    senha += random.choice(caracteres)            
  print ("A senha gerada foi:", senha)   

gerar_senha(tam,simb,num)

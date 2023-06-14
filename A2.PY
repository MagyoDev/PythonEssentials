# Condicionais
# if, else e  elif(else if)

# Transforme essa interação em uma condição

'''
E ae Alan, bora dar uma saida hoje?
Se eu terminar meu trabalho aqui, eu consigo.
'''
terminado = True #Troque para False para ver o que acontece
if terminado == True:
    print("Opa!Bora")
else:
    print("Não posso sair agora")
    
'''
Eu cheguei atrasado posso entrar?
Se essa não for sua terceira vez chegando atrasado, então pode sim, caso o contrário irá tomar suspensão 
'''    
atrasos = int(input("Quantas vezes você se atrasou? "))
num_max = 2
if atrasos <= num_max:
    print("Pode entrar")
else:
    print("Passe na diretoria")

# Encontre o maior entre 2 números
p1 = int(input("Digite o primeiro valor: "))
p2 = int(input("Digite o segundo valor: "))

if p1 > p2:
    print("Primeiro Valor maior que o Segundo Valor")
else:
    print("Segundo Valor maior que o Primeiro Valor")
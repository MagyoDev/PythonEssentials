# Laços de Repetição + Listas

'''
for item in coleção:
    expressão
'''

# EXEMPLOS
'''
for item in range(1,20):
    print(item)

for item in range(1,20,2):
    print(item)

nomes = ["Alan","Nair","Rafael","Edward","Arthur","Andrew","Wendell"]
for nome in nomes:
    print(nome)
'''

# Imprima os valores de 1 a N

valor_max = int(input("Digite o Valor máximo: "))
valor_inicial = 1

for numero in range(valor_inicial,valor_max + 1):
    print(numero)
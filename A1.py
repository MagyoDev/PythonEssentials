# VARIAVEIS
# Números
"int"
"float"
# Booleans
"True"
"False"
# Strings
''' nome = input("Qual seu nome? ") '''
# Problema 1 - Valor por hora
# Crie um programa que retorne o valor hora do funcionário com base no seu sálario mensal e horas trabalhadas no mês com o tipo de variaveis listado a cima

SalMensal = float(input("Qual o seu Salário Mensal? "))
HrTrabMes = int(input("Quantas horas trabalha por mês? "))
    
valorHora = SalMensal / HrTrabMes
print (valorHora)
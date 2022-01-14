ATALHOS P/ Programar

CTRL + SETA = PULA PALAVRA POR PALAVRA
CTRL + HOME/END = PULA A LINHA INTEIRA
CTRL + SHIFT + SETA -> ou <- = SELESIONA PALAVRA POR PALAVRA
CTRL + BACK = APAGA PALAVRA POR PALAVRA
CTRL + ";" PONTO E VIRGULA = COMENTAR O QUE FOI MARCADO
ALT = MOVER O QUE FOI MARCADO
SHIFT = IDENTA O QUE FOI MARCADO
SHIFT + TAB = REMOVE IDENTAÇÃO DO QUE FOI MARCADO




# Comentario
# OPERADORES RELACIONAIS
# == igualdade
# > maior que
# < menor que
# != diferente 
# >= maior ou igual a
# <= menor ou igual a
# Comparaçoes relacional True ou False

val1 = 2
val2 = 3

print(val1>val2)
print(val1<val2)
print(val1==val2)
print(val1!=val2)
print(val1>=val2)
print(val1<=val2)


n4 = input("Qual o seu nome")
print(n4)


# OPERADORES LÓGICOS
# not negação 
# and conjunção
# or disjunção

aprovado1 = True
aprovado2 = False
print(aprovado1 and aprovado2)
print(aprovado1 or aprovado2)



nome = input("Qual o seu nome? ")
media = int(input("Qual sua média final?: "))

print("Sejá bem-vindo " + nome + "Sua media é:" + str(media))

final = media + 1

print(type(nome))
print(type(media))





nota1 = 8.0
nota2 = 6.0

media = (nota1 + nota2)/2

if (media >= 6.0):
    print("Aprovado")
else:   
    print("Reprovado")




nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2  

if(media >=6.0):
    print("Aprovado com %f de nota"%media)
else:
    print("reprovado com %f de nota"%media)


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2  

if(media >=6.0):
    print("Aprovado com %f de nota"%media)
else:
    print("reprovado com %f de nota"%media)



media = 6.0
if media >= 4.0:




    if media >= 6.0:
        print("Aprovado")
    else:
        print("Recuperação")
else:
    print("Reprovado")




opc = 3

if opc == 1:
    print("um")
elif opc == 2:
    print("dois")
elif opc == 3:
     print("três")

    





print(not aprovado1)
print(not aprovado2)



#1.Faça um Programa que peça dois números e imprima o menor deles.

num1 = int(input("Entre com o primeiro número: "))
num2 = int(input("Entre com o segundo número: "))

if num1 > num2:
    print('Esse é o numero menor: %d' %num2)
else:
    print('Esse é o numero menor: %d' %num1)



#5

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/ 2

if media == 10:
    print("Aprovado com Distinção")
    
elif media >= 6:
    print("Aprovado")
    
else:
    print("Reprovado")
    






#2

valor = int(input("Digite a primeira nota: "))

if valor > 0 :
    print("Valor positivo")
elif valor < 0:
    print("Valor negativo")




cont = 0
while cont < 10:
    cont += 1
    print("%d - cont"%cont)









info = 'Escreva algo: '
info += "\nDigite 'sair' para finalizar: "

mensagem = ''

while mensagem != 'sair':
    mensagem = input(info)
    print(mensagem)




=====================================================================================


##1 - Faça um Programa que peça dois números e imprima o menor deles.

n1 = input("Digite um número: ")
n2 = input("Digite outro número: ")

if n1 > n2:
    print("O primeiro número digitado é maior")
else:
    print("O segundo número digitado é maior")



"""2 - Faça um Programa que peçaum valor e mostre na 
       tela se o valor é positivo ou negativo."""

num = int(input("Digite um número para saber se é positivo ou não:"))

if num > 0:
    print("Seu número é positivo")
else:
    print("Seu número é negativo")






"""3 - Faça um Programa que peça um número inteiro e determine se ele
   é par ou ímpar. Dica: utilize o operador módulo (resto da divisão)."""

num = int(input("Digite um número para saber se é impar ou não:"))

if num %2 == 0:
    print("Seu número é par")
else:
    print("Seu número é impar")






"""4 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
   Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido 
   (Utilize elif)."""

genero = str(input("Digite 'M' p/ masculino ou 'F' p/ feminino: "))

if genero == 'M' or genero == 'm':
    print("Masculino!")
elif genero == 'F' or genero == 'f':
    print("Feminino!")
else:
    print("Sexo invalido")


'''5 - Faça um programa para a leitura de duas notas parciais de um aluno.
   O programa deve calcular a média alcançada por aluno e apresentar:'''

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2  


if media == 10:
    print("Aprovado com Distinção: nota 10.00!!")
elif media >= 6:
    print("Aprovado com %.2f de nota"%media)
elif media < 6:
    print("reprovado com %.2f de nota"%media)






##6 - Faça um Programa que leia três números e mostre o maior e o menor deles.

n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))
n3 = int(input("Digite o 3° número: "))

if n1 > n2 and n1 > n3: ## Primeiro é maior
    print("O primeiro número digitado é o maior!!")
elif n2 > n1 and n2 > n3: ## segundo é maior
    print("O segundo número digitado é o maior!!")
elif n3 > n1 and n3 > n2: ## terceiro é maior
    print("O terceiro número digitado é o maior!!")



'''7 - As Organizações Tabajara resolveram dar um aumento de salário
   aos seus colaboradores e lhe contraram'''

##o salário antes do reajuste;
##o percentual de aumento aplicado;
##o valor do aumento;
##o novo salário, após o aumento.


novoSalario = 0
porcentagem = 0
quantAumento = 0
salarioAtual = float(input("Digite seu salario: "))


if salarioAtual <= 280.00:
    quantAumento = salarioAtual * 0.20
    porcentagem = 20
    
elif salarioAtual <= 700.00:
    quantAumento = salarioAtual * 0.15
    porcentagem = 15

elif salarioAtual <= 1500.00:
    quantAumento = salarioAtual * 0.10
    porcentagem = 10

elif salarioAtual > 1500.00:
    quantAumento = salarioAtual * 0.05
    porcentagem = 5

novoSalario = salarioAtual + quantAumento

print("O salario antes do aumento: %.2f"%salarioAtual)
print("O salario pós aumento: %.2f"%novoSalario)
print("A quantidade de aumento: %.2f"%quantAumento)
print("A porcentagem do aumento: %d"%porcentagem)










##8 - faça um Programa que leia um número e exiba o dia correspondente da semana.
##(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido

diaSemana = int(input("Digite o dia da semana: "))

if diaSemana == 1:
    print("Domingo!!")
    
elif diaSemana == 2:
    print("Segunda!!")

elif diaSemana == 3:
    print("Terça!!")

elif diaSemana == 4:
    print("Quarta!!")
    
elif diaSemana == 5:
    print("Quinta!!") 
    
elif diaSemana == 6:
    print("Sexta!!")

elif diaSemana == 7:
    print("Sabado!!")
    
else:
    print("Dia invalido!!")
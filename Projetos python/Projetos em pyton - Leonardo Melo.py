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
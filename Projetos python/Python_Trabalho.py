#Primeiro Programa: 
NomeAlunos = []
notas = []
aprovados = []
reprovados = []
continuar ='S';
cont = 0 

while continuar.upper() =='S':
    cont+=1
    NomaAluno = input("Digite o nome do aluno: ")
    NomeAlunos.append(NomaAluno)
    nota=int(input("Digite a nota do aluno: "))
    notas.append(nota)
    if(nota<6):
        reprovados.append(NomaAluno)
    else:
        aprovados.append(NomaAluno)
    continuar=input("Deseja digitar a noda de outro aluno?  ('S' para sim): ")

print("\nTodos os alunos cadastrados:")
for i in range(len(NomeAlunos)):
    print("%s: %s"%(NomeAlunos[i],notas[i]))

print('\nMedia da turma: ',sum(notas)/cont)
print("\nAprovados:")
for i in aprovados:
    print(i)
print("\nReprovados:")

for i in reprovados:
    print(i)



================================================================================================================
#Segundo Programa: 
nomeCandidato = []
numeroCandidato = []
partidoCandidato = []
cont = 0
continuar = 's'

while continuar.upper() == 'S':
    cont += 1
    nomeCandidato.append(input("Entre com o nome do candidato: "))
    numeroCandidato.append(int(input("Entre com o número do candidato: ")))
    partidoCandidato.append(str(input("Entre com o partido do candidato: ")))
    continuar = str(input("Deseja cadastrar outro candidato? ('S' para sim)"))
    
print("\n")
print("Tablela de candidatos: ")
for i in range(cont):
    print("Candidato -", nomeCandidato[i], "- Número", numeroCandidato[i], "Partido", partidoCandidato[i])

alterarCandidato = str(input("Deseja alterar o nome de algum candidato? ('S' para sim): "))

if alterarCandidato.upper() == 'S':
    buscaCandidato = int(input("Digite o número do candidato que deseja alterar o nome: "))
    novoNomeCandidato = str(input("Digite o novo nome do candidato: "))
    
    nomeCandidato.insert(numeroCandidato.index(buscaCandidato), novoNomeCandidato)
        
    print('\n')
    print("Nova tablela de candidatos: ")
    for y in range(cont):
        print("Candidato -", nomeCandidato[y], "- Número", numeroCandidato[y], "Partido", partidoCandidato[y])

===================================================================================================================
#Projeto Livre
#Programa para fazer compras no super mercado: o o programa deve permitir que o usuario escolha
#itens e suas quantidades, e mostrar o valor total da compra.


itens = ['Farinha','Arroz','Carne','Alface','Tomate','Abobora','Danone','Suco','Peixe','Coxinha']
CodItens = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
valorItens = [3.20,5.60,12.99,2.00,6.00,4.90,6.50,9.00,11.86,2.50]
carrinho = 0
valorCompra = 0
posicaoItens = 0
continuar = 's'
quantItens = 0

print("Os itens disponiveis no mercado são: ",itens)
print("E seus respectivos codigos são: ",CodItens)
print("Tabela de preços: ",valorItens)
while continuar.upper() == 'S':
    carrinho = (int(input("Digite o codigo do iten a ser comprado: ")))
    quantItens = (float(input("Quantidade do respectivo iten: ")))
    posicaoItens = CodItens.index(carrinho)
    valorCompra += valorItens[posicaoItens] * quantItens
    continuar = str(input("Deseja incluir mais itens? ('S' para sim)"))

print("Sua compra ficou no valor de: ",valorCompra)
====================================================================================================================
#Ex 1:
import random as rd
par = []
impar = []
mediaPar = 0
madiaImpar = 0
somaPar = 0
somaImpar = 0
contPar = 0
contImpar = 0

for i in range(1,21):
    numero = rd.randint(10,30)
    if (numero % 2) == 0:
        contPar += 1
        somaPar += numero
        par.append(numero)
    else:
        contImpar += 1
        somaImpar += numero
        impar.append(numero)
        
mediaPar = somaPar/contPar
madiaImpar = somaImpar/contImpar

print("Os números pares são = ",par)
print("Os números imapares são = ",impar)
print("A media dos números pares é: ",mediaPar)
print("A media dos números impares é: ",madiaImpar)
=====================================================================================
#Ex: 2
perguntas = ["Telefonou para a vítima?: ","Esteve no local do crime?: ","Mora perto da vítima?: ","Devia para a vítima?: ","Já trabalhou com a vítima?: "]
suspeito = 0
resposta = 'S'

for i in range(5):
    reposta = input(perguntas[i])

    if resposta == 's':
        suspeito += 1

if suspeito == 1 or suspeito == 0:
    print("Individuo inocente")
        
if suspeito == 2:
    print("Individuo suspeito")
      
if suspeito == 3 and suspeito == 4:
    print("Individuo cúmplice")
      
if suspeito == 5:
    print("Individuo assassino")

#Não conseguimos achar o erro deste, porem acreditamos que a logica esta correta.
===============================================================================================
#Ex: 3
notas = []
cont = 0
ok = 0
somaNotas = 0.0
acimaMedia = 0
acimaSete = 0

while ok == 0:
    cont += 1
    notas.append(float(input("Digite sua nota ou '-1' para encerrar: ")))
    somaNotas += notas[cont-1] 
    if (notas[cont-1] == -1):
        ok += 1
        notas.pop(cont-1)
        
somaNotas += 1
mediaNotas = somaNotas/(cont-1)

print("a) A quantidade de valores lidos é: ",cont-1)
print("b) ",notas)
print("c) ",notas[::-1])
print("d) Soma: ",somaNotas)
print("e) media: ",mediaNotas)

for i in range(cont-1):
    if notas[i] > mediaNotas:
        acimaMedia += 1
        
for i in range(cont-1):
    if notas[i] > 7:
        acimaSete += 1

print("f) Acima da media: ",acimaMedia)
print("g) Acima de 7: ",acimaSete)
print("h) Deus nos ajude na prova!!")
==================================================================================================



      

    
    
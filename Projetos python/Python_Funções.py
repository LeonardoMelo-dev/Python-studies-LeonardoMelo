def somar(num1, num2):
    result = num1 + num2
    return result

s = somar(5,4)
print(s)
print(somar(5,4))

retorno = 9
	  9
=====================================
def somar(num1, num2, num3):
    result = num1 + num2 + num3
    return result

s = somar(5,4,6)
print(s)
print(somar(5,4,6))

retorno = 15
	  15
=====================

def mensagem():
    print("Mensagem quaquer")
    
mensagem()

retorno = Mensagem quaquer






def somar(val1,val2):
    return val1+val2

print(somar(5,4))




def mensagemVisitante(nome):
    print("Bem vindo "+nome)
    
nome = input("Digite seu nome: ")
mensagemVisitante(nome)


def mensagemVisitante(nome="Visitante", sobrenome=''):
    print("Bem-vindo, "+nome+" "+sobrenome)
    
mensagemVisitante(nome="Léo",sobrenome="Melo")




def mensagemVisitante(nome="Visitante", sobrenome=''):
    print("Bem-vindo, "+nome+" "+sobrenome)
    
n = input("Digite seu nome: ")
b = input("Digite seu sobrenome: ")
    
mensagemVisitante(nome=n,sobrenome=b)





def mensagemVisitante(nome="Visitante", sobrenome=''):
    print("Bem-vindo, "+nome+" "+sobrenome)
    
mensagemVisitante()






def mensagemVisitante(nome="Visitante", sobrenome=''):
    print("Bem-vindo, "+nome+" "+sobrenome)
    
n = input("Digite seu nome: ")
b = input("Digite seu sobrenome: ")
    
mensagemVisitante(nome=n,sobrenome=b)




def mensagemVisitante(nome="Visitante"):
    return [nome,len(nome)]


print(mensagemVisitante("Léo")[0][1])




nome = 'leonardo'
def mensagemVisitante(nome="Visitante"):
    return [nome,len(nome)]

print(mensagemVisitante("leonardo")[0])




lista = [7,8,9,4,5,6]
print(lista[1:5])
print(lista)


#numero indeterminado de ingrediente/ parametros na função
def sanduiche(*ingredientes):
    print(ingredientes)

sanduiche('[Queijo','tomate','Alface','Frango]')



def somar(*val):
    acumulador = 0
    for i in val:
        acumulador += i
    return acumulador
res = somar(8,9,2,4,3,2)
print(res)



def somar(*val):
    acumulador = 1
    for i in val:
        acumulador *= i
    return acumulador
res = somar(2,6,2)
print(res)



def somar(*val):
    acumulador = 1
    for i in val:
        acumulador = acumulador**i
    return acumulador
res = somar(4,2)                        
print(res)

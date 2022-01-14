import random as rd
num = rd.random()
print(num)


import random as rd
num = rd.random()
num2 = rd.randint(10,30)
print(num)
print(num2)



for i in (1,2,3,11):
    print(i)




for i in range(10):
    print(i)



for i in range(5,20,2):
    print(i)



import random as rd
num = int(input("Digite um núemro: "))
for i in range(num):
    num = rd.randint(1,10)
    print(num)
    soma += num
        
print("A sima dos numeros digitados é: %d"%soma)
    
    




inicio = int(input("Digite o valor inicial: "))
fim = int(input("Digite o valor final: "))
for i in range(inicio,fim+1):
    print(i)



lista = [1,3,4,5,4]

print(lista)

tamanho = len(lista)

print(tamanho)

print(len(lista))




lista2 = [5, 9, 'Pyton',8.7,3.0,True]
print(lista2)
print(lista2[2])




lista3 = [7,[9,7,8],0,3,['Arroz','Feijão','Farinha'],True]
print(lista3)
print(lista3[1])
print(lista3[4])
print(lista3[1][2])
print(lista3[4][2])
print(lista3[4][2][0])
print("\n\n")

for i in lista3:
    print(i)





lista4 = [1,1.5,3,7.2]
for i in lista4:
    r= i - int(i)
    if r > 0:
        print(i)
        
print(type(lista4[1]))




curso = 'PROGRAMAÇÃO'
print(len(curso))

for c in curso:
    print(c)




lista5 = [1,8,9,7,3,6,5]
print(lista5)
print(len(lista5))




lista5.append(2)
print(lista5)



lista6 = []
lista6.append(6)
print(lista6)



lista6 = []
for i in range (3):
    lista6.append(input("Digie 3 números: "))
print(lista6)
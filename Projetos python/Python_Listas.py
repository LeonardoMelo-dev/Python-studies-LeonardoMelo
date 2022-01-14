lista = [8,4,5,6,3,7,4,1]
print(lista)
for i in lista:
    print(i)



lista.sort() ##ordenagem
print(lista)



lista.append(9) ##cria um contador até o número dentro dos parenteses
print(lista)





lista2 = []
lista2.append(1)
lista2.append(3)
lista2.append(6)
print(lista2)




print(len(lista2))



lista2.insert(0,2)
print(lista2)


lista2[0] = 5
print(lista2)


lista2.insert(2,9) ###adiciona um valor na posição dos parenteses
print(lista2)



valor = lista2.pop() ##remove um valor na posição dos parenteses
print(valor)
print(lista2)



valor = lista2.pop(2)
print(valor)
print(lista2)



lista_orig = [1,2,3,4,5] 
lista_copia = lista_orig ##Não funciona para criar copias
print(lista_orig)


lista_copia[0] = 0
print(lista_copia)
print(lista_orig)


lista_orig = [1,2,3,4,5] 
lista_copia = lista_orig[:] ##funciona p/ criar copias
lista_copia[0] = 0
print(lista_copia)
print(lista_orig)


compras = ['Arroz','Feijão','Farinha','Leite']
item = compras.index('Farinha') ##puxa um elemento do vetor
print(item) ##posição
print(compras[item]) 
print(item,compras[item])


compras.sort()
print(compras)



print("%s - %s"%(item,compras[iten]))



nome = ['Rosenilson','Jostrebaldo','Gestrudes']
RA = [123, 874, 987]
setor = ['Manutenção','Segurança','Suporte']

busca = int(input("Entre com o RA do funcionario: ")) ##busca = RA

indice = RA.index(busca) 

print("O funcionario %s (RA: %s) trabalha no setor de %s"%(nome[indice],RA[indice],setor[indice]))






notas = [8.0, 5.0, 7.0, 6.0, 4.0, 10.0]

# Menor número
menor = notas[0]
maior = notas[0]
soma = 0
cont = 0

for i in notas:
    cont += 1
    soma += i
    if i<menor:
        menor = i
    if i>maior:
        maior = i
print(menor)
print(maior)
print(soma)
print("Media: ", soma/cont)






menor = min(notas)
maior = max(notas)

print("Menor nota: ",min(notas))
print("Maior nota: ",max(notas))
print(soma)
print("Media: ", sum(notas)/len(notas))
print("TAmanho: ",len(notas))


item = compras.index('Farinha') ##puxa um elemento do vetor

lista.append(9) ##cria um contador até o número dentro dos parenteses



# Fatiamento de listas (slice)

lista1 = [1,2,3,4,5,6,7,8,9,10]
lista2 = lista1[2:5]
print(lista2)

retorno = [3, 4, 5]



========
lista3 = lista1[:6]
print(lista3)

retorno = [1, 2, 3, 4, 5, 6]





=================================
lista4 = lista1[4:]
print(lista4)

retorno = [5, 6, 7, 8, 9, 10]
===================================

lista5 = lista1[:8:2]
print(lista5)

retorno = [1, 3, 5, 7]

===========================================
lista = [1,2,3,4,5,6,7,8,9,10]
print(lista)
print(lista[0:10])
print(lista[:10])
print(lista[:])


retorno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

==================================================
lista6 = lista[::-1]
print(lista6)

retorno = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

======================================================

listaA = [1,2,3,4,5,6,7,8,9,10]
listaB = [11,12,13,14,15,16,17,18,19,20]
meuSlice = slice(2,7)
print(listaA[meuSlice])
print(listaB[meuSlice])

retorno = [3, 4, 5, 6, 7]
          [13, 14, 15, 16, 17]

======================================================

nome = 'Leonardo Melo'
print(nome[:5])

retorno = Leona
=====================================================




nome = 'Leonardo Melo'
print(nome[:5])

for i in range(len(nome)+1):
    print(nome[:i])


retorno = Leona

L
Le
Leo
Leon
Leona
Leonar
Leonard
Leonardo
Leonardo 
Leonardo M
Leonardo Me
Leonardo Mel
Leonardo Melo

===============================================



































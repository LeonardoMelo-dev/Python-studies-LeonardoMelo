!!LISTA É APENAS O NOME DA VARIAVEL ENTÃO PODE SER QUALQUER UMA!!▓▓
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓

#juntando listas
lista = [1,2,3,4,5]
lista2 = [6,7,8,9]
list(lista + lista2)
retorno = [1, 2, 3, 4, 5, 6, 7, 8, 9]
====================================================
#repetindo listas
list(lista2 * 5)
retorno = [6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9, 6, 7, 8, 9]
======================================================
#procurar valor dentro da lista

<valor> in lista

EXEMPLOS:
2 in lista
7 in lista
7 in lista2

retorno = TRUE OR FALSE
=====================================================
#imprime os itens dentro da lista

for i in lista:
     print(i)

retorno = 1
          2
          3
          4
	  5
======================================================
#append = acrecenta elementos a lista

lista.append(10) - #Adiciona o número 10 na ultima posição do vetor

retorno = [1, 2, 3, 4, 5, 10]
==================================================================
#insert = subistitui um elemento na posição de escolha e manda os seguintes para frente

NomeVariavel.insert(POSIÇÃO, NOVO_NUMERO)

EXEMPLOS:
lista.insert(3,12) = [1, 2, 3, 12, 4, 5, 10]

lista.insert(4,13) = [1, 2, 3, 12, 13, 4, 5, 10]
===================================================
#index = busca de posição por valor

NomeVariavel.index(?)

EXEMPLOS:
lista = [1, 2, 3, 12, 13, 4, 5, 10]

lista.index(12)
retorno = 3

lista.index(13)
retorno = 4
======================================================================================================
#count = exibe quantas vezes o número aparece dentro do vetor

EXEMPLOS:
lista = [1, 2, 3, 12, 13, 4, 5, 10, 2, 2, 2, 2]

lista.count(2)
retorno = 5

lista.count(13)
retorno = 1

========================================================================================
#sort = Ordenar lista

EXEMPLO:
lista = [1,6,3,7,2,9,4,5,10,8]
lista.sort()
print(lista)
retorno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


========================================================================================
#reverse = reverter a lista
========================================================================================
#remove = remove a primeira ocorrencia do iten
========================================================================================
#pop = remove inten na posição de indice especificada
========================================================================================
#del
========================================================================================
#
========================================================================================
#
========================================================================================
#
========================================================================================
#














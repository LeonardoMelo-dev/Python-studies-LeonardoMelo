# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 19:20:00 2020

@author: PC
"""

arquivo = open('meuArquivo.txt', 'w')
arquivo.write('Cruando um arquivo de texto\n')
arquivo.write('Leonardo Felicio de Melo\n')
arquivo.write('Outras informações...')
arquivo.close()

#arquivo2 = open('meuArquivo2.txt' , 'a')
#texto = input('Digite um texto para adicionar ao arquivo: \n')
#arquivo2.write(texto+"\n")
#arquivo2.close()

arquivo2 = open('meuArquivo2.txt','r')
for linha in arquivo2:
    print(linha)
arquivo2.close()


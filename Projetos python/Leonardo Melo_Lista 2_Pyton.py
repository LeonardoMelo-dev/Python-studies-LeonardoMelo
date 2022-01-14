##Ex: 1
ok = 0
while(ok == 0):
    nota = int(input("Digite sua nota: "))
    if(nota >= 0 and nota <= 10):
        print("Sua nota é: %d"%nota)
        ok += 1
    else:
        print("Nota invalida, digite novamente!!")


##Ex: 2
media = 0
soma = 0
for i in range(5):
    num = float(input("Digite um número: "))
    soma += num
media = (soma/5)
print("A media dos números digitados é: %f"%media)


##Ex: 3 
x = int(input("Digite um número: "))
y = int(input("Digite um número: "))

if x < y:
    for i in range(x,y):
        print(i)
if y < x:    
    for i in range(y,x):
        print(i)


##Ex: 4
b = int(input("Digite o valor da base: "))
c = int(input("Digite o valor da expoente: "))
a = 1
for i in range(c): ## a = b * b * b... por c vezes
    a *= b 
print(a)


##Ex: 5
par = 0
impar = 0
for i in range(0,20):
    num = int(input("Digite um número: "))
    if num %2 == 0:
        par += 1
    else:
        impar += 1
    
print("Dos 20 números digitados %d são pares "%par)
print("E %d são impares"%impar)


##Ex: 6
x = int(input("Digite um número para receber o fatorial: "))
fator = 1
i = 2
while i<=x:
    fator = fator*i
    i=i+1
print(fator)


##Ex: 7
x = int(input("Digite o valor x: "))
y = int(input("Digite o valor y: "))

if(x<y):
    for i in range(x,y):
        if(i %2 == 1):
            print(i)
if(y<x):
    for i in range(y,x):
        if(i %2 == 1):
            print(i)


Ex: 8:
tabuada = [[0,1,2,3,4,5,6,7,8,9,10],
           [0,1,2,3,4,5,6,7,8,9,10],
           [0,1,2,3,4,5,6,7,8,9,10],
           [0,1,2,3,4,5,6,7,8,9,10],
           [0,1,2,3,4,5,6,7,8,9,10],
           [0,1,2,3,4,5,6,7,8,9,10],
           [0,1,2,3,4,5,6,7,8,9,10],
           [0,1,2,3,4,5,6,7,8,9,10],
           [0,1,2,3,4,5,6,7,8,9,10],
           [0,1,2,3,4,5,6,7,8,9,10],
           [0,1,2,3,4,5,6,7,8,9,10]]
     
i = 1
j = 1
for i in range (1,11):
    for j in range (1,11):
        tabuada[i][j] = i*j
        
for i in range (1,11):
    print("Tabuada do %d"%i)
    for j in range (1,11):
        print(i,"x",j,"=",tabuada[i][j])
    print("\n")   
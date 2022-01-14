#Retornando mais de um parametros em uma função
def getNome(nome):
    return nome, len(nome), 0

resNome, resLen, zero = getNome("Leonardo")

print(resNome)
print(resLen)
print(zero)


============================================================


# Orientação a objeto
# Cachorro

class Cachorro():
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def sentar(self):
        print(self.nome + " está sentado.")
    
    def latir(self):
        print(self.nome +" latiu.")
        
meuCachorro = Cachorro("Totó", 2)
meuCachorro.sentar()
meuCachorro.latir()

seuCachorro = Cachorro("Spyke", 5)
seuCachorro.latir()

dog1 = Cachorro("SemNome", 58)
dog1.sentar()




===============================================================

# Orientação a objeto
# Cachorro

class Cachorro():
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def sentar(self):
        print(self.nome + " está sentado.")
    
    def latir(self):
        print(self.nome +" latiu.")
        
meuCachorro = Cachorro("Totó", 2)
seuCachorro = Cachorro("Spyke",5)

meuCachorro.sentar()
meuCachorro.latir()

print("O nome do cachorro é "+meuCachorro.nome+" e ele tem " + str(meuCachorro.idade) + " anos de idade")
print("O nome do cachorro é "+seuCachorro.nome+" e ele tem " + str(seuCachorro.idade) + " anos de idade")


=================================================================

#Orientação a objeto
#Carro

class Carro:
    
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        
    def getDescricao(self):
        desc = self.marca + ' ' + self.modelo + ' ' + self.ano + ' ' + self.cor
    
Carro = Carro("BMW","X1", 2020, "Preto")

descricao = carro.getDescricao()

class Pessoa:
    especie = 'humana'
    def __init__(self,entrada1,entrada2,e3,e4,e5):
        self.nome = entrada1 
        self.idade = entrada2
        self.peso = e3
        self.altura = e4
        self.sexo = e5
    
    def saudar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade}")
    
    def descrever(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos, peso {self.peso} kilos, tenho {self.altura} metros de altura e sou do sexo {pessoa.sexo}")

    def envelhecer(self):
        self.idade += 1
    
    def comparar_idades(self, zezao ):
        if self.idade > zezao.idade:
            print("A pessoa é mais nova que voce")
        elif self.idade == zezao.idade:
            print("A pessoa tem a mesma idade que voce")
        else: 
            print("A pessoa é mais velha que voce")
        

pessoa = Pessoa("Marcos", 30, 80, 1.74, "Masculino")
pessoa2 = Pessoa("Zeazo", 25, 55, 1.80, "Masculino" )
pessoa.saudar()

print(pessoa.peso)
print(pessoa.altura)
print(pessoa.sexo)

#print(pessoa.especie)
#pessoa.solteira = True
#print(pessoa.solteira)

pessoa.descrever()
pessoa.envelhecer()
print(pessoa.idade)
pessoa.comparar_idades(pessoa2)

pessoa3 = Pessoa("Livia", 40, 50, 1.65, "Feminino")
lista = [pessoa,pessoa2,pessoa3]
for pessoa in lista:
    print(f"{pessoa.nome} tem {pessoa.idade} anos")

class Veiculo:
     def __init__(self,marca,modelo,ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
     def info(self):
        print(f"Caro {self.modelo} da marca {self.marca} do ano {self.ano}")

     def atualizar_ano(self, novoano):
         self.ano = novoano

 
Brasilia = Veiculo("Brasilia", "Volkswagen", "1974")
Brasilia.info()
Brasilia.atualizar_ano("1978")
Brasilia.info()
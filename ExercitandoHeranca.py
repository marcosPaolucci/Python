class Funcionario:
    def __init__(self,nome,salario):
        self.nome = nome
        self.salario = salario

    def info(self):
        print(f"O Funcionário {self.nome} tem salário de {self.salario}")
    
class Gerente(Funcionario):
    def __init__(self, nome, salario, setor):
        super().__init__(nome, salario)
        self.setor = setor

    def info(self):
        print(f"O Gerente {self.nome} do setor {self.setor} tem salário de {self.salario}")

    def aumentarSalario(self, porcentagem):
        self.salario = self.salario * (1 + float(porcentagem))
        print(f"O novo salário do Gerente é {self.salario}")
        
Steve = Funcionario("Steve", 5000)
Steve.info()

Meg = Gerente("Meg", 10000, "Financeiro")
Meg.info()
Meg.aumentarSalario(0.1)


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Aluno(Pessoa):
    def __init__(self, nome, idade, nota=None):
        super().__init__(nome, idade)
        self.nota = nota

class Professor(Pessoa):
    def __init__(self, nome, idade, disciplina):
        super().__init__(nome, idade)
        self.disciplina = disciplina

    def adicionar_nota_aluno(self, aluno, nota):
        aluno.nota = nota
        print(f"Nota {nota} adicionada para o aluno {aluno.nome} na disciplina {self.disciplina}")

# Criando um aluno
aluno1 = Aluno("João", 20)

# Criando um professor
professor1 = Professor("Maria", 35, "Matemática")

# Adicionando nota para um aluno pelo professor
professor1.adicionar_nota_aluno(aluno1, 9.0)
print(aluno1.nota)

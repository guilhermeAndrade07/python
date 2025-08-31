# Sistema Escolar

class Escola():
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 

    def apresentar(self):
        print(f'Meu nome é {self.nome}')

class Aluno(Escola):
    def __init__(self, nome, idade, escolaridade):
        super().__init__(nome, idade)
        self.escolaridade = escolaridade

    def apresentar(self):
        print(f'Meu nome é {self.nome}, tenho {self.idade} anos de idade.')

class Professor(Escola):
    def __init__(self, nome, idade, materia):
        super().__init__(nome, idade)
        self.materia = materia

class Assistente(Escola):
    def __init__(self, nome, idade, bloco):
        super().__init__(nome, idade)
        self.bloco = bloco

a1 = Aluno('Guilherme', 14, 8)
p1 = Professor('Claudia', 40, 'Português')
as1 = Assistente('Carlos', 20, 'Bloco C')

a1.apresentar()
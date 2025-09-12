class Estudante:
    def __init__(self, matricula, nome, sexo):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo

    def __repr__(self):
        return f"Estudante({self.matricula}, {self.nome}, {self.sexo})"
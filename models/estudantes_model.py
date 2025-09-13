class Estudante:
    def __init__(self, matricula, nome, sexo, nota1=None, nota2=None, media=None, status=None):
        self.matricula = matricula
        self.nome = nome
        self.sexo = sexo
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = media
        self.status = status

    def __repr__(self):
        return f"Estudante({self.matricula}, {self.nome}, {self.sexo}, {self.nota1}, {self.nota2}, {self.media}, {self.status})"
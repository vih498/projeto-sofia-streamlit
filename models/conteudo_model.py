class Conteudo:
    def __init__(self, id, titulo, descricao):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao

    def __repr__(self):
        return f"Conteudo({self.id}, {self.titulo}, {self.descricao})"
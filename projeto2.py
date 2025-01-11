class Projeto:
    def __init__(self,codigo,vagas,nota_minima):
        self.codigo = codigo
        self.vagas = vagas
        self.nota_minima = nota_minima
        self.alunos_selecionados = []

class Aluno:
    def __init__(self,nome,nota,preferencias):
        self.nome = nome
        self.nota = nota
        self.preferencias = preferencias
        self.alocado = None
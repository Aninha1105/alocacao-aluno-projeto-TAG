class Projeto:
    def __init__(self, codigo, vagas, nota_minima):
        self.codigo = codigo
        self.vagas = vagas
        self.nota_minima = nota_minima
        self.alunos_selecionados = []

class Aluno:
    def __init__(self, nome, nota, preferencias):
        self.nome = nome
        self.nota = nota
        self.preferencias = preferencias
        self.alocado = None

def processarLinhaProjeto(linha, projetos):
    linha = linha.strip("()")  # Remove parênteses no início e no fim da linha.
    codigo, vagas, nota_minima = linha.split(", ")  # Divide a linha em três partes com base na vírgula e espaço.
    # Adiciona um novo projeto ao dicionário 'projetos' usando o código como chave.
    projetos[codigo.strip()] = Projeto(  
        codigo = codigo.strip(),
        vagas = int(vagas.strip()),
        nota_minima = int(nota_minima.strip())
    )

def processarLinhaAluno(linha, alunos):
    linha = linha.strip("()")  # Remove parênteses no início e no fim da linha.
    nome, infos = linha.split("):")  # Divide a linha no código e nas informações com base no "):".
    nome = nome.strip()  # Remove espaços extras do código.
    preferencias_raw, nota_raw = infos.split(") (")  # Divide as preferências e a nota com base em ") (".
    preferencias = [projeto.strip() for projeto in preferencias_raw.strip("(").split(", ")]  # Remove o "(" inicial, separa projetos por vírgulas e remove espaços extras.
    nota = int(nota_raw.strip(")"))  # Remove o ")" final e converte a nota para inteiro.
    # Cria um objeto Aluno e o adiciona à lista 'alunos'.
    alunos.append(Aluno(
        nome = nome,
        nota = nota,
        preferencias = preferencias
    ))

def lerArquivo(caminho_arquivo):
    projetos = {}  # Inicializa um dicionário vazio para armazenar os projetos.
    alunos = []  # Inicializa uma lista vazia para armazenar os alunos.
    cont = 0  # Contador para o número de linhas processadas.
    with open(caminho_arquivo, 'r') as arquivo:  # Abre o arquivo no modo de leitura.
        for linha in arquivo:  # Itera por cada linha do arquivo.
            linha = linha.strip()  # Remove espaços em branco no início e no fim da linha.
            if linha.startswith("//") or not linha:  # Ignora linhas de comentário ("//") ou linhas vazias.
                continue
            
            cont += 1  # Incrementa o contador de linhas.
            if cont <= 55:  # As primeiras 55 linhas são processadas como projetos.
                processarLinhaProjeto(linha, projetos)
            elif cont <= 255:  # As linhas de 56 a 255 são processadas como alunos.
                processarLinhaAluno(linha, alunos)
    return projetos, alunos  # Retorna os dicionários e projetos e alunos.


caminho_arquivo = "proj2-tag.txt"
projetos, alunos = lerArquivo(caminho_arquivo)

""" Debug leitura de arquivo
print("Projetos:")
for codigo, projeto in projetos.items():
    print(f"{projeto.codigo}, {projeto.vagas}, {projeto.nota_minima}")
print("Alunos:")
for aluno in alunos:
    print(f"{aluno.nome}, {aluno.nota}, {aluno.preferencias}, {aluno.alocado}")
"""
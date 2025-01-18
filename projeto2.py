import random

class Projeto:
    def __init__(self, codigo, vagas, nota_minima):
        self.codigo = codigo
        self.vagas = vagas
        self.nota_minima = nota_minima
        self.alunos_selecionados = []

    def temVaga(self):
        return len(self.alunos_selecionados) < self.vagas
    
    def adicionaAluno(self, aluno):
        self.alunos_selecionados.append(aluno)

    def removeAluno(self, aluno):
        if aluno in self.alunos_selecionados:
            self.alunos_selecionados.remove(aluno)

    def qtdAlunos(self):
        return len(self.alunos_selecionados)

class Aluno:
    def __init__(self, nome, nota, preferencias):
        self.nome = nome
        self.nota = nota
        self.preferencias = preferencias
        self.alocado = None
        self.next_p = 0

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
    alunos[nome] = Aluno(
        nome = nome,
        nota = nota,
        preferencias = preferencias
    )

def lerArquivo(caminho_arquivo):
    projetos = {}  # Inicializa um dicionário vazio para armazenar os projetos.
    alunos = {}  # Inicializa uma lista vazia para armazenar os alunos.
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

def gale_shapley_iterativo(projetos, alunos, num_iteracoes=10):
    # Filtra os alunos candidatos (com base em suas preferências e notas mínimas dos projetos)
    alunos_candidatos = []
    for aluno in alunos.values():
        for p in aluno.preferencias:
            if aluno.nota >= projetos[p].nota_minima:
                alunos_candidatos.append(aluno)
                break

    for iteracao in range(num_iteracoes):
        print(f"\nIteração {iteracao + 1}:")

        # Reseta as alocações antes de cada iteração
        for projeto in projetos.values():
            projeto.alunos_selecionados.clear()
        for aluno in alunos.values():
            aluno.alocado = None

        # Permuta os alunos aleatoriamente
        lista_alunos = alunos_candidatos[:]
        random.shuffle(lista_alunos)  # Embaralha os alunos

        livres = lista_alunos  # Lista de alunos a serem processados

        while livres:
            aluno = livres.pop(0)

            for projeto in aluno.preferencias:
                if aluno.alocado is not None:
                    break

                projeto_atual = projetos[projeto]
                if aluno.nota >= projeto_atual.nota_minima:
                    if projeto_atual.temVaga():
                        projeto_atual.adicionaAluno(aluno)
                        aluno.alocado = projeto_atual.codigo
                    else:
                        # Re-alocação forçada
                        pior_aluno = min(projeto_atual.alunos_selecionados, key=lambda a: a.nota)
                        if aluno.nota > pior_aluno.nota:
                            projeto_atual.removeAluno(pior_aluno)
                            pior_aluno.alocado = None
                            livres.append(pior_aluno)
                            projeto_atual.adicionaAluno(aluno)
                            aluno.alocado = projeto_atual.codigo

        # Exibe o estado do emparelhamento após a iteração
        contador = 0
        for projeto in projetos.values():
            print(f"{projeto.codigo}: {[a.nome for a in projeto.alunos_selecionados]}")
            contador += projeto.qtdAlunos()
        print(f"Total de alunos alocados: {contador}")

    # Retorna o emparelhamento final
    emparelhamento = {projeto.codigo: [a.nome for a in projeto.alunos_selecionados] for projeto in projetos.values()}
    return emparelhamento


caminho_arquivo = "proj2-tag.txt"
projetos, alunos = lerArquivo(caminho_arquivo)
emparelhamento_maximo_estavel = gale_shapley_iterativo(projetos, alunos)
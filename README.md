# Alocação Aluno-Projeto TAG

## Descrição do Problema

Este projeto aborda o problema de emparelhamento máximo e estável entre alunos e projetos oferecidos por uma universidade. 

- **Projetos**: 55 projetos financiados com até 74 vagas no total. Cada projeto possui requisitos de nota mínima e limitações de vagas.
- **Alunos**: 200 alunos que podem indicar até 3 projetos em ordem de preferência. Suas notas variam de 3 (suficiente) a 5 (excelente).
- **Objetivo**: Maximizar o número de projetos realizados e garantir estabilidade no emparelhamento, respeitando os critérios definidos.

## Solução

A implementação utiliza uma variação iterativa do algoritmo **Gale-Shapley** para alcançar um emparelhamento máximo e estável.

### Principais Funcionalidades

1. **Leitura de Arquivo de Entrada**:
   - Processa informações de projetos e alunos a partir do arquivo (`proj2-tag.txt`).

2. **Estruturas de Dados**:
   - **Projeto**: Contém o código, número de vagas, nota mínima e alunos selecionados.
   - **Aluno**: Armazena nome, nota, preferências e estado de alocação.

3. **Execução Iterativa**:
   - Realiza até 10 iterações para ajustar alocações.
   - Embaralha a ordem dos alunos a cada iteração para maior diversidade.
   - Realiza **re-alocação forçada** para substituir alunos com notas mais baixas em projetos com a capacidade preechida, se necessário.
   - Atualiza as alocações e exibe o estado atual do emparelhamento após cada iteração.

## Execução

### Requisitos
- Python 3.10 ou superior.

### Passos para Rodar
1. Na pasta do projeto, execute o script `projeto2.py` no terminal:
   ```bash
   python3 projeto2.py
   ```

## Estrutura do Código
- `Projeto`: Classe que representa um projeto e suas características.
- `Aluno`: Classe que representa um aluno, sua nota e preferências.
- `processarLinhaProjeto(linha, projetos)`: Função auxiliar da leitura de arquivo.
- `processarLinhaAluno(linha, alunos)`: Função auxiliar da leitura de arquivo.
- `lerArquivo(caminho_arquivo)`: Função que processa o arquivo de entrada.
- `gale_shapley_iterativo(projetos, alunos, num_iteracoes)`: Função principal que realiza o emparelhamento iterativo.

## Resultado

Após a execução de 10 iterações do algoritmo iterativo baseado no Gale-Shapley, o emparelhamento máximo e estável alcançado alocou 56 alunos. Este emparelhamento respeita os limites de vagas de cada projeto e as preferências dos alunos, garantindo a estabilidade na alocação.

### Emparelhamento Máximo e Estável obtido

- **P1**: ['A2', 'A1']  
- **P2**: ['A32']  
- **P3**: ['A147', 'A33']  
- **P4**: ['A34']  
- **P5**: ['A35', 'A85']  
- **P6**: ['A8']  
- **P7**: ['A117', 'A187']  
- **P8**: ['A18', 'A62']  
- **P9**: ['A99', 'A23']  
- **P10**: ['A200']  
- **P11**: []  
- **P12**: ['A31']  
- **P13**: []  
- **P14**: ['A43', 'A151']  
- **P15**: ['A135', 'A154']  
- **P16**: ['A42']  
- **P17**: ['A181']  
- **P18**: ['A157']  
- **P19**: []  
- **P20**: ['A132']  
- **P21**: ['A177']  
- **P22**: ['A144']  
- **P23**: []  
- **P24**: ['A114']  
- **P25**: ['A184']  
- **P26**: ['A48', 'A93']  
- **P27**: ['A83', 'A81']  
- **P28**: ['A137']  
- **P29**: ['A129']  
- **P30**: ['A64']  
- **P31**: ['A127']  
- **P32**: []  
- **P33**: []  
- **P34**: ['A25']  
- **P35**: ['A55']  
- **P36**: ['A128', 'A92']  
- **P37**: ['A61']  
- **P38**: ['A100']  
- **P39**: ['A63']  
- **P40**: ['A84']  
- **P41**: ['A197', 'A107']  
- **P42**: []  
- **P43**: ['A153']  
- **P44**: ['A82']  
- **P45**: ['A53']  
- **P46**: []  
- **P47**: ['A96']  
- **P48**: ['A188']  
- **P49**: ['A159']  
- **P50**: []  
- **P51**: []  
- **P52**: []  
- **P53**: ['A95', 'A60']  
- **P54**: []  
- **P55**: ['A26']  

**Total de Alunos Alocados**: 56  

# Sistema de Gerenciamento de Notas

## Descricao

O projeto é um sistema de gerenciamento acadêmico desenvolvido em Python. Seu objetivo é administrar o fluxo de informações entre alunos e professores, englobando o registro e consulta de notas, controle de turmas, gerencia de disciplinas e calculo de frequências.

## Tecnologias e Ferramentas Utilizadas

* Python 3: Linguagem principal do desenvolvimento.
* FreeSimpleGUI: Biblioteca utilizada para a construcao das interfaces graficas do sistema, isolando a interação do usuário das regras de negócio.
* Pickle: Modulo nativo do Python utilizado para a serializacao de objetos em tempo de execução e persistencia de dados em arquivos binarios.

## Arquitetura

O sistema foi estruturado seguindo o padrao de projeto MVC (Model-View-Controller). Esse padrão separa a interface de usuario, a logica de controle e a modelagem dos dados de forma independente. O sistema também implementa o padrao DAO (Data Access Object) para abstrair e gerenciar o armazenamento e a recuperacao das informacoes das entidades de forma centralizada utilizando caches em memória e atualizações atreladas aos arquivos físicos.

## Funcionalidades

### Modulo do Aluno

* Cadastro e autenticação no sistema.
* Busca e vinculação de turmas e disciplinas a partir da matrícula.
* Consulta de notas consolidadas e boletim.
* Calculo e analise de frequencia especifica por turma vinculada.

### Modulo do Professor

* Cadastro e autenticacao no sistema.
* Inscricao como professor regente de disciplinas especificas.
* Insercao e matricula de alunos nas respectivas disciplinas e turmas.
* Lancamento, leitura e atualizacao das notas dos alunos.
* Registro de frequencia e presenca nas turmas sob sua gerência.

## Estrutura do Projeto

A organizacao de diretorios reflete a divisao de responsabilidades imposta pela arquitetura MVC e camadas de acesso a dados:

* `main.py`: Arquivo principal responsável por instanciar o controlador central e dar inicio a execucao do sistema.
* `controlador/`: Contem as classes que orquestram as operacoes do sistema e intermedeiam View e Model. Exemplo: `ControladorSistema`, `ControladorAluno`, `ControladorProfessor`, `ControladorNota`, `ControladorTurma` e `ControladorFrequencia`.
* `entidade/`: Define os modelos de dados do dominio e regras de negocio, englobando herança estrutural nas classes `Aluno` e `Professor` através da superclasse `Pessoa`, bem como as estruturas para `Disciplina`, `Turma`, `Nota` e `Frequencia`.
* `limite/`: Agrupa as classes de interface com o usuario construidas através do FreeSimpleGUI. Implementa janelas e botões de rádio para captar fluxos de decisão.
* `dao/`: Concentra a logica de persistencia, fornecendo uma classe abstrata `DAO` contendo operações genéricas de CRUD (`add`, `update`, `get`, `remove`, `get_all`) e implementacoes especificas para as entidades manipularem os arquivos `.pkl` independentemente.
* `exception/`: Modulo destinado ao tratamento de excecoes personalizadas de operação, bloqueando anomalias estruturais como o cadastro duplicado de alunos ou professores no banco de dados.

## Como Executar

1. Certifique-se de possuir o Python 3.x instalado em sua máquina.
2. Instale os requisitos da interface grafica através do gerenciador de pacotes pip:
```bash
pip install FreeSimpleGUI

```


3. Acesse o diretorio raiz do repositorio clonado via terminal e inicialize o programa:
```bash
python main.py

```

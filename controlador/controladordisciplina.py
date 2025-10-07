from entidade.disciplina import Disciplina
from teladisciplina import TelaDisciplina
from entidade.aluno import Aluno

class ControladorDisciplina():
    def __init__(self):
        self.__disciplinas = []

    def cadastrar_disciplina(self):
        dados_disciplina = self.__pega_dados_disciplina()
        disciplina = Disciplina(dados_disciplina["nome"], dados_disciplina["codigo"])
        self.__disciplinas.append(disciplina)

        return (f"{disciplina.nome} cadastrada com sucesso!")

    
    def cadastrar_aluno(self):
        dados_aluno = self.__pega_dados_aluno()
        aluno = Aluno(dados_aluno["nome"], dados_aluno["matricula"], dados_aluno["disciplina"])
        self

          
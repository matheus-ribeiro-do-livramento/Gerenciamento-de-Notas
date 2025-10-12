from entidade.nota import Nota
from entidade.turma import Turma
#from entidade.aluno import Aluno
from entidade.alunojamatriculado import AlunoJaMatriculado


class Disciplina:
    def __init__(self, nome: str, codigo: str):
        self.__nome = None
        self.__codigo = None
        self.__turma = []
        self.__nota = []
        self.__alunos = []

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(codigo, str):
            self.__codigo = codigo


    @property
    def nome(self):
        return self.__nome

    @property
    def codigo(self):
        return self.__codigo

    @property
    def nota(self):
        return self.__nota

    @property
    def alunos(self):
        return self.__alunos[:]

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, str):
            self.__codigo = codigo

    def matricular_aluno(self, aluno):
        if aluno not in self.__alunos:
                self.__alunos.append(aluno)
        else:
            raise Exception("Aluno já matriculado nesta disciplina")
             
    
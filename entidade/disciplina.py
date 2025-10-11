from nota import Nota
from turma import Turma
from aluno import Aluno
from alunojamatriculado import AlunoJaMatriculado


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

    def matricular_aluno(self, aluno: Aluno):
        if not isinstance(aluno, Aluno):
            raise TypeError("O objeto a ser matriculado deve ser do tipo Aluno.")
        if aluno in self.__alunos:
            raise AlunoJaMatriculado(aluno.nome, self.nome)
        else:
            self.__alunos.append(aluno)
            return True
    
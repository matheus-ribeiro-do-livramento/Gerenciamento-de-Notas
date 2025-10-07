from nota import Nota
from turma import Turma
from aluno import Aluno

class Disciplina:
    def _init_(self, nome: str, codigo: str, turma: Turma, nota: Nota, alunos: Aluno):
        self.__nome = None
        self.__codigo = None
        self.__turma = []
        self.__nota = []
        self.__alunos = []

        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(codigo, str):
            self.__codigo = codigo
        if isinstance(turma, Turma):
            self.__turma.append(Turma(turma))
        if isinstance(nota, Nota):
            self.__nota.append(nota)
        if isinstance(alunos, Aluno):
            self.__aluno.append(Aluno)

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
        return self.__alunos

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, str):
            self.__codigo = codigo


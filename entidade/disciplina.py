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
        self.__professor = None  # professor responsável pela disciplina

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
    def turmas(self):
        return self.__turma

    @property
    def alunos(self):
        return self.__alunos[:]

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, professor):
        self.__professor = professor

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, str):
            self.__codigo = codigo

    def matricular_aluno(self, aluno):
   #     if not isinstance(aluno, Aluno):
     #       raise TypeError("O objeto a ser matriculado deve ser do tipo Aluno.")
        if aluno in self.__alunos:
                raise AlunoJaMatriculado(aluno.nome, self.nome)
        else:
            self.__alunos.append(aluno)
            return True

    def adicionar_turma(self, turma: Turma):
        self.__turma.append(turma)
    
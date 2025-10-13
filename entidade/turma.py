from typing import List

class Turma():
    def __init__(self, sala: str, numero: int, semestre: str):
        self.__sala = sala
        self.__numero = numero
        self.__semestre = semestre
        self.__alunos = []

    @property
    def sala(self):
        return self.__sala
    
    @sala.setter
    def sala(self, sala):
        self.__sala = sala

    @property
    def numero(self):
        return self.__numero
    
    @numero.setter
    def numero(self, numero):
        self.__numero = numero

    @property
    def semestre(self):
        return self.__semestre
    
    @semestre.setter
    def semestre(self, semestre):
        self.semestre = semestre

    @property
    def alunos(self):
        return self.__alunos[:] # Retorna uma cópia para proteger a lista
    
    @alunos.setter
    def alunos(self, alunos):
        self.__alunos = alunos

    def matricular_aluno(self, aluno):
        if aluno not in self.__alunos:
            self.__alunos.append(aluno)
            return True
        return False # Aluno já matriculado
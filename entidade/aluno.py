from entidade.pessoa import Pessoa
from entidade.disciplina import Disciplina
from typing import List

class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: int):
        super().__init__(nome, matricula)
        self.__disciplinas = []

    @property
    def nome(self):
        return self._Pessoa__nome

    @property
    def matricula(self):
        return self._Pessoa__matricula

    @nome.setter
    def nome(self, nome: str):
        self._Pessoa__nome = nome

    @matricula.setter
    def matricula(self, matricula: int):
        self._Pessoa__matricula = matricula


    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

    @property
    def disciplinas(self):
        return self.__disciplinas[:]
    
    @disciplinas.setter
    def disciplinas(self, disciplinas):
        if isinstance(disciplinas, List[Disciplina]):
            self.__disciplinas = disciplinas

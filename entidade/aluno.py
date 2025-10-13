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
    def disciplina(self, disciplinas):
        if isinstance(disciplinas, List[Disciplina]):
            self.__disciplina = disciplinas

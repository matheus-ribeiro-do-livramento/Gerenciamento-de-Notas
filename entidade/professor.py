from entidade.disciplina import Disciplina
from entidade.pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome: str, matricula: int):
        super().__init__(nome, matricula)
        self.__disciplina = None

    @property
    def nome(self):
        return self._Pessoa__nome

    @property
    def matricula(self):
        return self._Pessoa__matricula


from entidade.pessoa import Pessoa
from entidade.disciplina import Disciplina

class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: int):
        super().__init__(nome, matricula)
        self.__senha = ""
        self.__disciplinas = []


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







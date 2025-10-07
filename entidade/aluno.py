from pessoa import Pessoa
from disciplina import Disciplina

class Aluno(Pessoa):
    def __init__(self, nome: str, matricula: int, senha: str, disciplina: Disciplina):
        super().__init__(nome, matricula)
        self.__senha = []
        self.__disciplina = None


        if isinstance(senha, str):
            self.__senha = []
        
        if isinstance(disciplina, Disciplina):
            self.__disciplina = disciplina

    @property
    def senha(self):
        return self.__senha
    
    @senha.setter
    def senha(self, senha):
        self.__senha = []

    @property
    def disciplina(self):
        return self.__disciplina
    
    @disciplina.setter
    def disciplina(self, disciplina):
        if isinstance(disciplina, Disciplina):
            self.__disciplina = Disciplina







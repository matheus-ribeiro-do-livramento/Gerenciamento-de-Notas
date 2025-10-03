from disciplina import Disciplina
class Professor:
    def _int_(self, nome: str, disciplina: Disciplina, matricula: int, senha: str):
        super().__init__(nome, matricula)
        self.__nome = None
        self.__disciplina = None
        self.__matricula = None
        self.__senha = None


        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(disciplina, Disciplina):
            self.__disciplina = disciplina
        if isinstance(matricula, int):
            self.__matricula = matricula
        if isinstance(senha, str):
            self.__senha = senha

    @property
    def nome(self):
        return self.__nome
    @property
    def disciplina(self):
        return self.__disciplina
    @property
    def matricula(self):
        return self.__matricula
    @property
    def senha(self):
        return self.__senha
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @disciplina.setter
    def disciplina(self, disciplina):
        self.__disciplina = disciplina
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula
    @senha.setter
    def senha(self, senha):
        self.__senha = senha

     
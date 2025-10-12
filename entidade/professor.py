from entidade.disciplina import Disciplina
class Professor:
    def _int_(self, nome: str, matricula: int):
        super().__init__(nome, matricula)
        self.__nome = None
        self.__disciplina = None
        self.__matricula = None


        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(matricula, int):
            self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome
    @property
    def matricula(self):
        return self.__matricula
    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

     
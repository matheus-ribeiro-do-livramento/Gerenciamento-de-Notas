class Nota:
    def __init__(self, valor: float):
        self.__valor = None
        self.__aluno = None
        if isinstance(valor, float):
            self.__valor = valor
  

    @property
    def valor(self):
        return self.__valor

    @property
    def aluno(self):
        return self.__aluno

    @valor.setter
    def valor(self, valor):
        self.__valor = valor
    @aluno.setter
    def aluno(self, aluno):
        self.__aluno = aluno
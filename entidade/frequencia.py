from turma import Turma

class Frequencia():
    def __init__(self, turma: Turma):
        self.__turma = None
        self.__hitorico_frequencia  = {}

        if isinstance(turma, Turma):
            self.__turma = turma

        
    @property
    def turma(self):
        return self.__turma
    
    @turma.setter
    def turma(self, turma):
        self.__turma = turma
        
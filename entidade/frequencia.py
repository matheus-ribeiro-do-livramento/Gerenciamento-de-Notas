from entidade.turma import Turma

class Frequencia():
    def __init__(self, turma: Turma):
        self.__turma = None
        # Formato: { "DD/MM/YYYY": { matricula_aluno: 'P' ou 'F' } }
        self.__historico_frequencia  = {}

        if isinstance(turma, Turma):
            self.__turma = turma

        
    @property
    def turma(self):
        return self.__turma
    
    @turma.setter
    def turma(self, turma):
        self.__turma = turma

    @property
    def historico(self):
        return self.__historico_frequencia
        
    def registrar_frequencia(self, data: str, frequencia_alunos: dict):
        self.__historico_frequencia[data] = frequencia_alunos
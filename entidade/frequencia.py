

class Frequencia():
    def __init__(self, turma):
        self.__turma = turma
        self.__historico_frequencia  = {}

        #if isinstance(turma, Turma):
            #self.__turma = turma

        
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

    def editar_frequencia_aluno(self, data: str, matricula_aluno: int, novo_status: str):
        if data in self.__historico_frequencia and matricula_aluno in self.__historico_frequencia[data]:
            self.__historico_frequencia[data][matricula_aluno] = novo_status
            return True
        return False

    def excluir_frequencia_aluno(self, data: str, matricula_aluno: int):
        if data in self.__historico_frequencia and matricula_aluno in self.__historico_frequencia[data]:
            del self.__historico_frequencia[data][matricula_aluno]
            if not self.__historico_frequencia[data]:
                del self.__historico_frequencia[data]
            return True
        return False
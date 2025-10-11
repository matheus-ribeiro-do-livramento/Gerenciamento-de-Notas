from entidade.aluno import Aluno

class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__controlador_sistema = controlador_sistema
        
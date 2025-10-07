from controlador.controladorprofessor import ControladorProfessor
from controlador.controladoraluno import ControladorAluno
from controlador.controledisciplina import 

class ControladorSistema:
    def __init__(self):
        self.__controlador_professor = ControladorProfessor(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__cont
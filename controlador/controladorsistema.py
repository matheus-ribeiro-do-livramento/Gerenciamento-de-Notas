from controlador.controladorprofessor import ControladorProfessor
from controlador.controladoraluno import ControladorAluno
from controlador.controladordisciplina import ControladorDisciplina
from limite.telasistema import TelaSistema

class ControladorSistema:
    def __init__(self):
        self.__controlador_professor = ControladorProfessor(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_disciplina = ControladorDisciplina(self)
        self.__tela_sistema = TelaSistema() 
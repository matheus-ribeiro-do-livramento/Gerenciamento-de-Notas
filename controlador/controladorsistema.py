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
    
    @property
    def controladorprofessor(self):
        return self.__controlador_professor
    
    @property
    def controladoraluno(self):
        return self.__controlador_aluno
    
    @property
    def controladordisciplina(self):
        return self.__controlador_disciplina
    
    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_professor(self):
        self.__controlador_professor.abre_tela_cadastro()
    
    def abre_tela(self):
        opcoes_lista = {1: self.cadastra_professor}

        while True:
            oppcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = oppcao_escolhida[oppcao_escolhida]
            funcao_escolhida()

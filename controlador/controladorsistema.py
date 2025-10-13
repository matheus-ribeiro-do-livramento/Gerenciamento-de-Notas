from controlador.controladorprofessor import ControladorProfessor
from controlador.controladoraluno import ControladorAluno
from controlador.controladordisciplina import ControladorDisciplina
from limite.telasistema import TelaSistema
from controlador.controladornota import ControladorNota
from time import sleep

class ControladorSistema:
    def __init__(self):
        self.__controlador_professor = ControladorProfessor(self)
        self.__controlador_aluno = ControladorAluno(self)
        self.__controlador_disciplina = ControladorDisciplina(self)
        self.__controlador_nota = ControladorNota(self)
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
    
    @property
    def controladornota(self):
        return self.__controlador_nota
    
    def inicializa_sistema(self):
        self.abre_tela()

    def cadastra_professor(self):
        self.__controlador_professor.abre_tela_opcoes()

    def cadastrar_aluno(self):
        self.__controlador_aluno.abre_tela_opcoes()

    def encerrar_sistema(self):
        self.__tela_sistema.mostrar_msg('Encerrando sistema...')
        sleep(1)
        exit(0)
    
    def abre_tela(self):
        opcoes_lista = {0: self.encerrar_sistema, 1: self.cadastra_professor, 2: self.cadastrar_aluno}

        while True:
            opcao_escolhida = self.__tela_sistema.tela_opcoes()
            funcao_escolhida = opcoes_lista[opcao_escolhida]
            funcao_escolhida()

    def buscar_notas_do_aluno(self, matricula: int) -> list | None:
        """Repassa a solicitação de BUSCA para o controlador de notas."""
        return self.__controlador_nota.buscar_notas_do_aluno(matricula)
    

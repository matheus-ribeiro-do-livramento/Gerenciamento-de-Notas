from limite.telaprofessor import TelaProfessor
from controlador.controladorsistema import ControladorSistema

class ControladorProfessor:
    def __init__(self, controladorsistema):
        self.__professor = []
        self.__controlador_sistema = ControladorSistema
        self.__tela_professor = TelaProfessor()
    
    def abre_tela_login(self):
        while True:
            self.__tela_professor.tela_login()
            
        
    def abre_tela_cadastro(self):
        while True:
            self.__tela_professor.tela_cadastro()

    def abre_tela_opcoes(self):
        dados_cadastro = self.__tela_professor.tela_cadastro()
        dados_login = self.__tela_professor.tela_login()
        if dados_cadastro['matricula']['senha'] == dados_login['matricula']['senha']:
            while True:
                pass

    def guardar_matricula(self):
        pass
        
    



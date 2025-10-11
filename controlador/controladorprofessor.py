from limite.telaprofessor import TelaProfessor

class ControladorProfessor:
    def __init__(self, controladorsistema):
        self.__professor = []
        self.__controlador_sistema = controladorsistema
        self.__tela_professor = TelaProfessor()
    
    def abre_tela_login(self):
        return self.__tela_professor.tela_login()
    
    def abre_tela_cadastro(self):
        return self.__tela_professor.tela_cadastro()

    def abre_tela_opcoes(self):
        dados_cadastro = self.abre_tela_cadastro()
        dados_login = self.abre_tela_login()

        if dados_cadastro['matricula'] == dados_login['matricula'] and dados_cadastro['senha'] == dados_login['senha']:
            # credenciais conferem — aqui você pode setar estado ou chamar outra tela
            return True
        return False

    def guardar_matricula(self, dados):
        self.__professor.append(dados)
        return True
        
    



from limite.telaprofessor import TelaProfessor

class ControladorProfessor:
    def __init__(self, controladorsistema):
        self.__professor = []
        self.__controlador_sistema = controladorsistema
        self.__tela_professor = TelaProfessor()
    
    def buscar_professor_por_matricula(self, matricula):
        for professor in self.__professor:
            if professor[2] == matricula:
                return professor 
        return None

    def abre_tela_login(self):
        login = self.__tela_professor.tela_login()
        professor = self.buscar_professor_por_matricula(login)
        
        if professor is None:
            self.__tela_professor.mostrar_msg('Matrícula não cadastrada')
        else:
            self.abre_tela_funcao(professor[0])  
    
    def abre_tela_cadastro(self):
        cadastro = self.__tela_professor.tela_cadastro()
        if cadastro == 0:  
            return
        if self.buscar_professor_por_matricula(cadastro[2]):
            self.__tela_professor.mostrar_msg('Matrícula já cadastrada')
            return
        self.__professor.append(cadastro)
        self.__tela_professor.mostrar_msg('Cadastro realizado com sucesso!')
    

    def abre_tela_opcoes(self):
        lista_opcoes = {1: self.abre_tela_login, 2: self.abre_tela_cadastro, 0: self.voltar}
        
        while True:
            opcao = self.__tela_professor.tela_opcoes()
            if opcao == 0:
                break
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
        
    def abre_tela_funcao(self, nome_professor):
        lista_opcao = {1: self.adicionar_nota, 2: 'nada', 3: 'nada', 4: 'nada', 5: 'nada', 0: self.voltar}

        while True:
            opcao = self.__tela_professor.tela_funcoes(nome_professor)  # passa o nome do professor
            if opcao == 0:
                break
            if opcao in lista_opcao:
                lista_opcao[opcao]()

    def voltar(self):
        return True 

    def adicionar_nota(self):
        self.__controlador_sistema.controlador_nota.adicionar_nota()
        
    



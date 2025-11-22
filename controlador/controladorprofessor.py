from limite.telaprofessor import TelaProfessor
from entidade.professor import Professor
from dao.professor_dao import ProfessorDao

class ControladorProfessor:
    def __init__(self, controladorsistema):
        self.__professor_DAO = ProfessorDao()
        self.__controlador_sistema = controladorsistema
        self.__tela_professor = TelaProfessor()
    
    def buscar_professor_por_matricula(self, matricula):
        try:
            matricula_int = int(matricula)
        except ValueError:
            return None 
        for professor in self.__professor_DAO.get_all():
            if professor.matricula == matricula_int:
                return professor 
        return None

    def abre_tela_login(self):
        login = self.__tela_professor.tela_login()
        professor = self.buscar_professor_por_matricula(login)
        
        if professor is None:
            self.__tela_professor.mostrar_msg('Matrícula não cadastrada')
        else:
            self.abre_tela_funcao(professor)
    
    def abre_tela_cadastro(self):
        cadastro = self.__tela_professor.tela_cadastro()
        if cadastro == 0:  
            return
        if self.buscar_professor_por_matricula(cadastro[1]):
            self.__tela_professor.mostrar_msg('Matrícula já cadastrada')
            return
        novo_professor = Professor(cadastro[0], cadastro[1])
        self.__professor_DAO.add(novo_professor)
        self.__tela_professor.mostrar_msg('Cadastro realizado com sucesso!')
    

    def abre_tela_opcoes(self):
        lista_opcoes = {1: self.abre_tela_login, 2: self.abre_tela_cadastro, 0: self.voltar}
        
        while True:
            opcao = self.__tela_professor.tela_opcoes()
            if opcao == 0:
                break
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
        
    def abre_tela_funcao(self, professor_logado: Professor):
        lista_opcao = {1: self.opcoes_disciplina,
                      2: lambda: self.vincular_disciplina(professor_logado),
                      3: self.opcoes_turma,
                      4: self.opcoes_alunos,
                      5: self.opcoes_nota,
                      6: self.opcoes_frequencia,
                      7: self.listar_status_alunos,
                      0: self.voltar}

        while True:
            opcao = self.__tela_professor.tela_funcoes(professor_logado.nome)
            if opcao == 0:
                break
            if opcao in lista_opcao:
                lista_opcao[opcao]()

    def opcoes_disciplina(self):
        lista_opcoes = {1: self.criar_disciplina,
                        2: self.__controlador_sistema.controladordisciplina.alterar_disciplina,
                        3: self.__controlador_sistema.controladordisciplina.excluir_disciplina,
                        4: self.__controlador_sistema.controladordisciplina.listar_disciplina,
                        0: self.voltar
                            }
        
        while True:
            opcao = self.__tela_professor.tela_opcoes_disciplina()
            if opcao == 0:
                break
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
        
    def opcoes_nota(self):
        lista_opcoes = {1: self.cadastrar_nota,
                        2: self.editar_nota,
                        3: self.excluir_nota,
                        4: self.ver_nota,
                        0: self.voltar}
        
        while True:
            opcao = self.__tela_professor.tela_opcoes_nota()
            if opcao == 0:
                break
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
        
    def opcoes_alunos(self): 
        lista_opcoes = {1: self.matricular_aluno,
                        2: self.__controlador_sistema.controladoraluno.alterar_aluno,
                        3: self.__controlador_sistema.controladoraluno.excluir_aluno,
                        4: self.__controlador_sistema.controladoraluno.listar_alunos,
                        0: self.voltar}
        
        while True:
            opcao = self.__tela_professor.tela_opcoes_aluno()
            if opcao == 0:
                break
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()

    def opcoes_frequencia(self):
        lista_opcoes = {1: self.lancar_frequencia,
                        2: self.editar_frequencia,
                        3: self.excluir_frequencia,
                        4: self.listar_frequencia,
                        0: self.voltar}
        
        while True:
            opcao = self.__tela_professor.tela_opcoes_frequencia()
            if opcao == 0:
                break
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()
    
    def opcoes_turma(self):
        lista_opcoes = {1: self.__controlador_sistema.controladorturma.criar_turma,
                        2: self.__controlador_sistema.controladorturma.editar_turma,
                        3: self.__controlador_sistema.controladorturma.excluir_turma,
                        4: self.__controlador_sistema.controladorturma.listar_turma,
                        0: self.voltar}
        
        while True:
            opcao = self.__tela_professor.tela_opcoes_turma()
            if opcao == 0:
                break
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()

    def voltar(self):
        return True 

    def cadastrar_nota(self):
        self.__controlador_sistema.controladornota.adicionar_nota()
        
    def vincular_disciplina(self, professor: Professor):
        if not professor:
            self.__tela_professor.mostrar_msg("Erro ao identificar professor!")
            return
        
        self.__controlador_sistema.controladordisciplina.listar_disciplina()
    
        codigo_disciplina = self.__tela_professor.pegar_codigo_disciplina()
        if not codigo_disciplina:
            return
            
        disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
        if not disciplina:
            self.__tela_professor.mostrar_msg("Disciplina não encontrada!")
            return

        if disciplina.professor is not None:
            self.__tela_professor.mostrar_msg("Esta disciplina já possui um professor!")
            return
            
        disciplina.professor = professor
        self.__tela_professor.mostrar_msg(f"Professor {professor.nome} vinculado com sucesso à disciplina {disciplina.nome}!")
    
    def criar_disciplina(self):
        disciplina = self.__controlador_sistema.controladordisciplina.cadastrar_disciplina()

    def matricular_aluno(self):
        aluno = self.__controlador_sistema.controladordisciplina.matricular_aluno()

    def criar_turma(self):
        self.__controlador_sistema.controladorturma.criar_turma()

    def lancar_frequencia(self):
        self.__controlador_sistema.controladorfrequencia.lancar_frequencia()

    def ver_nota(self):
        notas = self.__controlador_sistema.controladornota.consultar_notas()
    
    def editar_nota(self):
        self.__controlador_sistema.controladornota.editar_nota()
    
    def excluir_nota(self):
        self.__controlador_sistema.controladornota.excluir_nota()
    
    def editar_frequencia(self):
        self.__controlador_sistema.controladorfrequencia.editar_frequencia()

    def excluir_frequencia(self):
        self.__controlador_sistema.controladorfrequencia.excluir_frequencia()
    
    def listar_frequencia(self):
        frequencia = self.__controlador_sistema.controladorfrequencia.listar_frequencia()

    def listar_status_alunos(self):
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if not disciplina:
            return

        dados_para_tela = []

        for turma in disciplina.turmas:
            for aluno in turma.alunos:
                media, notas = self.__controlador_sistema.controladornota.calcular_media_aluno(
                    disciplina.codigo, aluno.matricula
                )


                frequencia = self.__controlador_sistema.controladorfrequencia.calcular_frequencia_aluno(
                    turma, aluno
                )

                dados_para_tela.append({
                    "disciplina": disciplina.nome,
                    "nome": aluno.nome,
                    "matricula": aluno.matricula,
                    "media": media,
                    "notas": notas,
                    "frequencia": frequencia
                })
        

        self.__tela_professor.mostra_status_alunos(dados_para_tela)
    

    
    

from limite.telaprofessor import TelaProfessor

class ControladorProfessor:
    def __init__(self, controladorsistema):
        self.__professor = []
        self.__controlador_sistema = controladorsistema
        self.__tela_professor = TelaProfessor()
    
    def buscar_professor_por_matricula(self, matricula):
        for professor in self.__professor:
            if professor[1] == matricula:
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
        if self.buscar_professor_por_matricula(cadastro[1]):
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
        lista_opcao = {1: self.cadastrar_nota, 
                      2: lambda: self.vincular_disciplina(nome_professor),
                      3: self.criar_disciplina, 
                      4: self.matricular_aluno,
                      5: self.ver_nota,
                      6: self.criar_turma,
                      7: self.editar_nota,
                      8: self.lancar_frequencia,
                      9: self.excluir_nota,
                      10: self.listar_status_alunos,
                      0: self.voltar}

        while True:
            opcao = self.__tela_professor.tela_funcoes(nome_professor)
            # O '0' para sair é tratado no 'break'
            if opcao == 0:
                break
            if opcao in lista_opcao:
                lista_opcao[opcao]()

    def voltar(self):
        return True 

    def cadastrar_nota(self):
        self.__controlador_sistema.controladornota.adicionar_nota()
        
    def vincular_disciplina(self, nome_professor):
        # Pega a matrícula do professor logado
        professor = None
        for prof in self.__professor:
            if prof[0] == nome_professor:
                professor = prof
                break
                
        if not professor:
            self.__tela_professor.mostrar_msg("Erro ao identificar professor!")
            return
            
        # Pega o código da disciplina que o professor quer vincular
        codigo_disciplina = self.__tela_professor.pegar_codigo_disciplina()
        if not codigo_disciplina:
            return
            
        # Busca a disciplina no controlador de disciplinas
        disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
        if not disciplina:
            self.__tela_professor.mostrar_msg("Disciplina não encontrada!")
            return
            
        # Verifica se a disciplina já tem professor
        if disciplina.professor is not None:
            self.__tela_professor.mostrar_msg("Esta disciplina já possui um professor!")
            return
            
        # Vincula o professor à disciplina
        disciplina.professor = professor
        self.__tela_professor.mostrar_msg(f"Professor {nome_professor} vinculado com sucesso à disciplina {disciplina.nome}!")
    
    def criar_disciplina(self):
        disciplina = self.__controlador_sistema.controladordisciplina.cadastrar_disciplina()

    def matricular_aluno(self):
        aluno = self.__controlador_sistema.controladordisciplina.cadastrar_aluno()

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
    
    def listar_status_alunos(self):
        # 1. Selecionar a disciplina
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if not disciplina:
            return

        dados_para_tela = []

        # 2. Percorrer as turmas da disciplina
        for turma in disciplina.turmas:
            # 3. Percorrer os alunos da turma
            for aluno in turma.alunos:
                # 4. Calcular a média das notas
                media = self.__controlador_sistema.controladornota.calcular_media_aluno(
                    disciplina.codigo, aluno.matricula
                )

                # 5. Calcular a frequência
                frequencia = self.__controlador_sistema.controladorfrequencia.calcular_frequencia_aluno(
                    turma, aluno
                )

                dados_para_tela.append({
                    "disciplina": disciplina.nome,
                    "nome": aluno.nome,
                    "matricula": aluno.matricula,
                    "media": media,
                    "frequencia": frequencia
                })
        
        # 6. Exibir os dados
        self.__tela_professor.mostra_status_alunos(dados_para_tela)
    

    
    

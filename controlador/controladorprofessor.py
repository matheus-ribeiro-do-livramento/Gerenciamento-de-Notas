from limite.telaprofessor import TelaProfessor
from entidade.professor import Professor

class ControladorProfessor:
    def __init__(self, controladorsistema):
        self.__professores = []
        self.__controlador_sistema = controladorsistema
        self.__tela_professor = TelaProfessor()
    
    def buscar_professor_por_matricula(self, matricula):
        try:
            matricula_int = int(matricula)
        except ValueError:
            return None # Retorna None se a matrícula não for um número válido
        for professor in self.__professores:
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
        self.__professores.append(novo_professor)
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
        lista_opcao = {1: self.criar_disciplina,
                      2: lambda: self.vincular_disciplina(professor_logado),
                      3: self.criar_turma,
                      4: self.matricular_aluno,
                      5: self.cadastrar_nota,
                      6: self.editar_nota,
                      7: self.excluir_nota,
                      8: self.lancar_frequencia,
                      9: self.editar_frequencia,
                      10: self.excluir_frequencia,
                      11: self.listar_status_alunos,
                      12: self.ver_nota,
                      0: self.voltar}

        while True:
            opcao = self.__tela_professor.tela_funcoes(professor_logado.nome)
            if opcao == 0:
                break
            if opcao in lista_opcao:
                lista_opcao[opcao]()

    def voltar(self):
        return True 

    def cadastrar_nota(self):
        self.__controlador_sistema.controladornota.adicionar_nota()
        
    def vincular_disciplina(self, professor: Professor):
        if not professor:
            self.__tela_professor.mostrar_msg("Erro ao identificar professor!")
            return
            
    
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
    

    
    

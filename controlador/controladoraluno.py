from entidade.aluno import Aluno
from limite.telaaluno import TelaAluno

class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_aluno = TelaAluno()

    
    def pega_aluno_matricula(self, matricula):
        for a in self.__alunos:
            if (a.matricula == matricula):
                return a
        return None

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()

        try:
            self.pega_aluno_matricula(dados_aluno["matricula"])
            self.__tela_aluno.mostrar_msg("O Aluno já está cadastrado")
        except KeyError:
            self.__tela_aluno.mostrar_msg("Dados do Aluno incompletos")
        except Exception as erro_busca: 
            try:
                aluno =Aluno(dados_aluno["nome"], dados_aluno["matricula"])
                self.__alunos.append(aluno)
                self.__tela_aluno.mostrar_msg("Aluno incluido com sucesso")
            except Exception as erro_cadastro:
                self.__tela_aluno.mostrar_msg(f"Falha desconhecida {erro_cadastro}")

    def alterar_aluno(self):
        self.listar_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_matricula(matricula_aluno)

        if (aluno is not None):
            novos_dados = self.__tela_aluno.pega_dados_aluno()
            aluno.nome = novos_dados["nome"]
            aluno.matricula = novos_dados["matricula"]
            self.listar_alunos()
        else:
            self.__tela_aluno.mostrar_msg("Erro: Aluno não existe")

    def listar_alunos(self):
        for a in self.__alunos:
            self.__tela_aluno.mostra_aluno({"nome": a.nome, "matricula": a.matricula})

    def excluir_aluno(self):
        self.listar_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_matricula(matricula_aluno)

        if (aluno is not None):
            self.__alunos.remove(aluno)
            self.listar_alunos()
        else:
            self.__tela_aluno.mostrar_msg("Erro: Aluno não existe")

    def sair(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        list_opcoes = {1: self.incluir_aluno, 2: self.listar_alunos, 3: self.alterar_aluno, 4: self.excluir_aluno, 5: self.sair}

        continua = True
        while continua:
            list_opcoes[self.__tela_aluno.tela_opcoes()]


    def abre_tela_login(self):
        login = self.__tela_aluno.tela_login()
        aluno = self.pega_aluno_matricula(login)

        if (aluno is not None):
            self.__tela_aluno.mostrar_msg('Matrícula não cadastrada')
        else:
            self.abre_tela_funcao()

    def abre_tela_crud(self):
        self.abre_tela()

    def abre_tela_opcoes(self):
        lista_opcoes = {1: self.abre_tela_login,
                        2: self.abre_tela_crud,
                        0: self.voltar}
        
        while True:
            opcao = self.__tela_aluno.tela_opcoes_login_cadastro()
            if opcao == 0:
                break
            if opcao in lista_opcoes:
                lista_opcoes[opcao]()

    def abre_tela_funcao(self):
        lista_opcao = {1: self.abre_tela, 2: 'nada', 3: 'nada', 4: 'nada', 5: 'nada', 0: self.voltar}

        while True:
            opcao = self.__tela_professor.tela_funcoes(nome_professor)  # passa o nome do professor
            if opcao == 0:
                break
            if opcao in lista_opcao:
                lista_opcao[opcao]()
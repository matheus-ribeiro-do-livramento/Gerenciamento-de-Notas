from entidade.aluno import Aluno
from limite.telaaluno import TelaAluno

class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_aluno = TelaAluno()
        self.__aluno_logado = None

    def pega_aluno_matricula(self, matricula):
        try:
            matricula_int = int(matricula)
        except ValueError:
            return None # Retorna None se a matrícula não for um número válido
        for a in self.__alunos:
            if (a.matricula == matricula_int):
                return a
        return None

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        if dados_aluno is None:
            self.__tela_aluno.mostrar_msg("Operação cancelada.")
            return None

        matricula = dados_aluno["matricula"]
        
        aluno_existente = self.pega_aluno_matricula(matricula)
        if aluno_existente:
            self.__tela_aluno.mostrar_msg("Aluno com esta matrícula já cadastrado. Utilizando aluno existente.")
            return aluno_existente

        aluno_novo = Aluno(dados_aluno["nome"], matricula)
        self.__alunos.append(aluno_novo)
        self.__tela_aluno.mostrar_msg("Aluno incluído com sucesso!")
        return aluno_novo

    def alterar_aluno(self):
        self.listar_alunos()
        if not self.__alunos: return

        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_matricula(matricula_aluno)

        if (aluno is not None):
            novos_dados = self.__tela_aluno.pega_dados_aluno()
            if novos_dados is None: return

            outro_aluno = self.pega_aluno_matricula(novos_dados["matricula"])
            if outro_aluno and outro_aluno != aluno:
                self.__tela_aluno.mostrar_msg("Erro: A nova matrícula já pertence a outro aluno.")
                return

            aluno.nome = novos_dados["nome"]
            aluno.matricula = novos_dados["matricula"]
            self.__tela_aluno.mostrar_msg("Aluno alterado com sucesso!")
        else:
            self.__tela_aluno.mostrar_msg("Erro: Aluno não existe")

    def listar_alunos(self):
        if not self.__alunos:
            self.__tela_aluno.mostrar_msg("\nNenhum aluno cadastrado.")
            return
        
        dados_para_mostrar = []
        for a in self.__alunos:
            dados_para_mostrar.append({"nome": a.nome, "matricula": a.matricula})
        self.__tela_aluno.mostra_aluno(dados_para_mostrar)

    def excluir_aluno(self):
        self.listar_alunos()
        if not self.__alunos: return

        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_matricula(matricula_aluno)

        if (aluno is not None):
            self.__alunos.remove(aluno)
            self.__tela_aluno.mostrar_msg("Aluno removido com sucesso!")
        else:
            self.__tela_aluno.mostrar_msg("Erro: Aluno não existe")

    def sair(self):
        self.__controlador_sistema.abre_tela()
    
    def logout(self):
        self.__aluno_logado = None
        self.__tela_aluno.mostrar_msg("Você saiu do seu login.")

    def abre_tela(self):
        list_opcoes = {1: self.incluir_aluno, 2: self.alterar_aluno, 3: self.listar_alunos, 4: self.excluir_aluno} 
        while True:
            opcao = self.__tela_aluno.tela_opcoes()
            if opcao == 0:
                break
            
            opcao_escolhida = list_opcoes.get(opcao)
            if opcao_escolhida:
                opcao_escolhida()
            else:
                self.__tela_aluno.mostrar_msg("Opção Inválida")

    def abre_tela_login(self):
        login = self.__tela_aluno.tela_login()
        aluno = self.pega_aluno_matricula(login)

        if (aluno is not None):
            self.__aluno_logado = aluno
            self.abre_tela_funcao_logado()
        else:
            self.__tela_aluno.mostrar_msg("Matrícula não cadastrada")

    def abre_tela_cadastro(self):
        dados_cadastro = self.__tela_aluno.tela_cadastro()

        if not dados_cadastro:
            return

        nome, matricula = dados_cadastro
        
        if self.pega_aluno_matricula(matricula):
            self.__tela_aluno.mostrar_msg('Matrícula já cadastrada')
            return

        novo_aluno = Aluno(nome, matricula)
        self.__alunos.append(novo_aluno)
        self.__tela_aluno.mostrar_msg('Cadastro realizado com sucesso!')

    def voltar(self):
        return True

    def abre_tela_opcoes(self):
        lista_opcoes = {1: self.abre_tela_login,
                        2: self.abre_tela_cadastro,
                        3: self.voltar}
        
        while True:
            opcao = self.__tela_aluno.tela_opcoes_login_cadastro()
            if opcao == 0:
                break
            if opcao in lista_opcoes:
                funcao_escolhida = lista_opcoes[opcao]
                if funcao_escolhida():
                    break

    def abre_tela_funcao_logado(self):
        lista_opcao = {
            1: self.ver_minhas_notas,
            2: lambda: self.__tela_aluno.mostrar_msg("Funcionalidade 'Ver Disciplinas' ainda não implementada."),
            0: self.logout
        }

        while self.__aluno_logado:
            opcao = self.__tela_aluno.tela_funcoes_aluno_logado(self.__aluno_logado.nome)
            
            if opcao == 0:
                self.logout()
                break

            funcao_escolhida = lista_opcao.get(opcao)
            if funcao_escolhida:
                funcao_escolhida()
            else:
                self.__tela_aluno.mostrar_msg("Opção inválida, tente novamente.")

    def ver_minhas_notas(self):
        if self.__aluno_logado is None:
            self.__tela_aluno.mostrar_msg("Erro: Nenhum aluno está logado.")
            return

        matricula_aluno_logado = self.__aluno_logado[1]
        
        notas_do_aluno = self.__controlador_sistema.buscar_notas_do_aluno(matricula_aluno_logado)

        self.__controlador_sistema.controladornota.exibir_notas_para_aluno(notas_do_aluno)
from entidade.aluno import Aluno
from limite.telaaluno import TelaAluno

class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_aluno = TelaAluno()
        self.__aluno_logado = None

    def pega_aluno_matricula(self, matricula):
        for a in self.__alunos:
            if (a[1] == matricula):
                return a
        return None

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        matricula = dados_aluno["matricula"]
        
        aluno_existente = self.pega_aluno_matricula(matricula)
        if aluno_existente:
            self.__tela_aluno.mostrar_msg("Aluno com esta matrícula já cadastrado. Utilizando aluno existente.")
            return aluno_existente

        aluno_novo = Aluno(dados_aluno["nome"], matricula)
        self.__alunos.append(aluno_novo)
        self.__tela_aluno.mostrar_msg("Aluno incluido com sucesso!")
        return aluno_novo

    def alterar_aluno(self):
        self.listar_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_matricula(matricula_aluno)

        if (aluno is not None):
            novos_dados = self.__tela_aluno.pega_dados_aluno()
            index_aluno = self.__alunos.index(aluno)
            self.__alunos[index_aluno] = (novos_dados["nome"], novos_dados["matricula"])
            self.listar_alunos()
        else:
            self.__tela_aluno.mostrar_msg("Erro: Aluno não existe")

    def listar_alunos(self):
        if not self.__alunos:
            self.__tela_aluno.mostrar_msg("Nenhum aluno cadastrado")
            return
        for a in self.__alunos:
            self.__tela_aluno.mostra_aluno({"nome": a[0], "matricula": a[1]})

    def excluir_aluno(self):
        if not self.__alunos:
            self.__tela_aluno.mostrar_msg("Nenhum aluno cadastrado")
            return

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
    
    def logout(self):
        self.__aluno_logado = None
        self.__tela_aluno.mostrar_msg("Voce saiu do seu login")

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
                self.__tela_aluno.mostrar_msg("Opcao Invalida")

    def abre_tela_login(self):
        login = self.__tela_aluno.tela_login()
        aluno = self.pega_aluno_matricula(login)

        if (aluno is not None):
            self.__aluno_logado = aluno
            self.abre_tela_funcao_logado()
        else:
            self.__tela_aluno.mostrar_msg("Matricula não cadastrada")

    def abre_tela_cadastro(self):
        dados_cadastro = self.__tela_aluno.tela_cadastro()

        if not dados_cadastro:
            return

        nome, matricula = dados_cadastro
        
        if self.pega_aluno_matricula(matricula):
            self.__tela_aluno.mostrar_msg('Matrícula já cadastrada')
            return

        self.__alunos.append(dados_cadastro)
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
            opcao = self.__tela_aluno.tela_funcoes_aluno_logado(self.__aluno_logado[0])
            
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
            # Reutiliza o método mostrar_msg da tela do aluno
            self.__tela_aluno.mostrar_msg("Erro: Nenhum aluno está logado.")
            return

        # Pega a matrícula da tupla do aluno logado ('Nome', matricula)
        matricula_aluno_logado = self.__aluno_logado[1]
        
        # 1. Pede ao ControladorSistema as notas, passando a matrícula.
        #    O ControladorSistema vai repassar a chamada para o ControladorNota.
        notas_do_aluno = self.__controlador_sistema.buscar_notas_do_aluno(matricula_aluno_logado)

        # 2. Pede para a TELA DE NOTAS exibir o resultado.
        #    Note que o ControladorAluno pede ajuda à TelaNota, via ControladorSistema.
        self.__controlador_sistema.controladornota.exibir_notas_para_aluno(notas_do_aluno)
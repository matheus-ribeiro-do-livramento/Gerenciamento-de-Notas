from entidade.aluno import Aluno
from limite.telaaluno import TelaAluno
from dao.aluno_dao import AlunoDAO
from exception.alunoexistenteException import AlunoExistenteException

class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__aluno_DAO = AlunoDAO()
        self.__controlador_sistema = controlador_sistema
        self.__tela_aluno = TelaAluno()
        self.__aluno_logado = None

    @property
    def tela_aluno(self):
        return self.__tela_aluno
    
    def pega_aluno_matricula(self, matricula):
        try:
            matricula_int = int(matricula)
        except ValueError:
            return None
        for a in self.__aluno_DAO.get_all():
              if a.matricula == matricula_int:
                return a
        return None

    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        if dados_aluno is None:
            return None
        
        try:
            matricula = dados_aluno["matricula"]
        
            aluno_existente = self.pega_aluno_matricula(matricula)
            if aluno_existente:
                raise AlunoExistenteException()
            
            aluno_novo = Aluno(dados_aluno["nome"], matricula)
            self.__aluno_DAO.add(aluno_novo)
            self.__tela_aluno.mostrar_msg("Aluno incluído com sucesso!")
            return aluno_novo
        
        except AlunoExistenteException:
            self.__tela_aluno.mostrar_msg('Já existe aluno com essa matricula')
            return None

    def alterar_aluno(self):
        self.listar_alunos()
        if not self.__aluno_DAO.get_all(): 
            self.__tela_aluno.aluno_nao_cadastrado()
            return
        else:
            matricula_aluno = self.__tela_aluno.seleciona_aluno()
            if matricula_aluno is None:
                return
            aluno = self.pega_aluno_matricula(matricula_aluno)

            if (aluno is not None):
                novos_dados = self.__tela_aluno.pega_dados_aluno()
                if novos_dados is None: 
                    return
                try:
                    outro_aluno = self.pega_aluno_matricula(novos_dados["matricula"])
                    if outro_aluno and outro_aluno != aluno:
                       raise AlunoExistenteException()
            

                    aluno.nome = novos_dados["nome"]
                    aluno.matricula = novos_dados["matricula"]
                    self.__aluno_DAO.update(aluno)
                    self.__tela_aluno.mostrar_msg("Dados alterados com sucesso")

                except AlunoExistenteException:
                    self.__tela_aluno.mostrar_msg('Já existe Outro aluno com essa matricula')
                    
            else:
                self.__tela_aluno.mostrar_msg("Erro: Aluno não existe")

    def listar_alunos(self):
        if not self.__aluno_DAO.get_all():
            self.__tela_aluno.aluno_nao_cadastrado()
            return
        
        else:
            dados_para_mostrar = []
            for a in self.__aluno_DAO.get_all():
                dados_para_mostrar.append({"nome": a.nome, "matricula": a.matricula})
            self.__tela_aluno.mostra_aluno(dados_para_mostrar)

    def excluir_aluno(self):
        self.listar_alunos()
        if not self.__aluno_DAO.get_all():
            self.__tela_aluno.aluno_nao_cadastrado()
            return
        else:
            matricula_aluno = self.__tela_aluno.seleciona_aluno()
            if matricula_aluno is None:
                return
            aluno = self.pega_aluno_matricula(matricula_aluno)

            if (aluno is not None):
                self.__aluno_DAO.remove(aluno)
                self.__tela_aluno.mostrar_msg("Aluno excluído com sucesso!")
            else:
                self.__tela_aluno.mostrar_msg("Erro: Aluno não existe")
    
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
        try:
            nome, matricula = dados_cadastro
        
            if self.pega_aluno_matricula(matricula):
                raise AlunoExistenteException()
    
            novo_aluno = Aluno(nome, matricula)
            self.__aluno_DAO.add(novo_aluno)
            self.__tela_aluno.mostrar_msg('Cadastro realizado com sucesso!')
            
        except AlunoExistenteException:
            self.__tela_aluno.mostrar_msg('Já existe aluno com essa matricula')
        except ValueError:
            self.__tela_aluno.mostrar_msg('Dados invalidos')

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
            2: self.ver_minhas_disciplinas,
            3: self.ver_minha_frequencia,
            4: self.ver_boletim,
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

        matricula_aluno_logado = self.__aluno_logado.matricula
        

        notas_do_aluno = self.__controlador_sistema.buscar_notas_do_aluno(matricula_aluno_logado)

        self.__controlador_sistema.controladornota.exibir_notas_para_aluno(notas_do_aluno)

    def ver_minhas_disciplinas(self):
        if self.__aluno_logado is None:
            self.__tela_aluno.mostrar_msg("Nenhum aluno logado")
            return
        
        matricula = self.__aluno_logado.matricula
        disciplina_obj = self.__controlador_sistema.buscar_disciplina_por_aluno(matricula)
        para_mostrar = []
        if disciplina_obj:
            for d in disciplina_obj:
                para_mostrar.append({'nome': d.nome, 'codigo': d.codigo})
        self.__tela_aluno.mostra_disciplina(para_mostrar)

    def ver_minha_frequencia(self):
        if self.__aluno_logado is None:
            self.__tela_aluno.mostrar_msg("Nenhum aluno logado")
            return
    
        disciplina_aluno = self.__controlador_sistema.buscar_disciplina_por_aluno(self.__aluno_logado.matricula)

        if not disciplina_aluno:
            self.__tela_aluno.mostrar_msg("Você não está matriculado em nenhuma disciplina")
            return
        
        resultado_frequencia = []
        
        for disciplina in disciplina_aluno:
            turma = self.__controlador_sistema.buscar_turma_do_aluno_na_disciplina(self.__aluno_logado, disciplina)

            if turma:
                percentual = self.__controlador_sistema.calcular_frequencia_aluno_na_turma(turma, self.__aluno_logado)
                resultado_frequencia.append({"disciplina": disciplina.nome, "percentual": percentual})

        self.__tela_aluno.mostra_frequencia(resultado_frequencia)

    def ver_boletim(self):
        if self.__aluno_logado is None:
            self.__tela_aluno.mostrar_msg("Nenhum aluno logado.")
            return

        matricula_aluno = self.__aluno_logado.matricula
        disciplinas_do_aluno = self.__controlador_sistema.buscar_disciplina_por_aluno(matricula_aluno)

        if not disciplinas_do_aluno:
            self.__tela_aluno.mostrar_msg("Você não está matriculado em nenhuma disciplina.")
            return

        boletim_data = []
        for disciplina in disciplinas_do_aluno:
            media, notas = self.__controlador_sistema.controladornota.calcular_media_aluno(
                disciplina.codigo, matricula_aluno)

            turma = self.__controlador_sistema.buscar_turma_do_aluno_na_disciplina(self.__aluno_logado, disciplina)
            frequencia = None
            if turma:
                frequencia = self.__controlador_sistema.calcular_frequencia_aluno_na_turma(turma, self.__aluno_logado)

            professor_nome = "Não definido"
            if disciplina.professor:
                professor_nome = disciplina.professor.nome

            boletim_data.append({
                "nome_disciplina": disciplina.nome,
                "codigo_disciplina": disciplina.codigo,
                "professor_nome": professor_nome,
                "notas": notas if notas else [],
                "media": media,
                "frequencia": frequencia
            })
        
        self.__tela_aluno.mostra_boletim(boletim_data)

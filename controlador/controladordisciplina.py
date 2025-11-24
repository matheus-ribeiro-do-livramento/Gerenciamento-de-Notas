from entidade.disciplina import Disciplina
from limite.tela_disciplina import TelaDisciplina
from entidade.aluno import Aluno
from dao.disciplina_dao import DisciplinaDAO

class ControladorDisciplina():
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__disciplina_dao = DisciplinaDAO()
        self.__tela_disciplina = TelaDisciplina()
    
    @property
    def tela_disciplina(self):
        return self.__tela_disciplina

    def abre_tela(self):
        list_opcoes = {1: self.matricular_aluno,
                       2: self.cadastrar_disciplina,
                       3: self.listar_disciplina,
                       4: self.alterar_disciplina,
                       5: self.excluir_disciplina,
                       6: self.listar_aluno, 
                       7: self.sair}

        continua = True
        while continua:
            opcao_escolhida = self.__tela_disciplina.tela_opcoes()
            if opcao_escolhida  == 7:
                continua = False
            elif opcao_escolhida in list_opcoes:
                list_opcoes[opcao_escolhida]()
                
            else:
                self.__tela_disciplina.mostrar_msg("Opção invalidade tente novamente")
            
    def cadastrar_disciplina(self):
        dados_disciplina = self.__tela_disciplina.pega_dados_disciplina()
        if dados_disciplina is None:
            self.__tela_disciplina.mostrar_msg("Cadastro cancelado.")
            return

        nome = dados_disciplina['nome'].strip()
        if not nome:
            self.__tela_disciplina.mostrar_msg("Erro: O nome da disciplina não pode ser vazio.")
            return

        try:
            codigo = int(dados_disciplina['codigo'])
        except (ValueError, TypeError):
            self.__tela_disciplina.mostrar_msg("Erro: O código da disciplina deve ser um número inteiro.")
            return

        if self.pega_disciplina_codigo(codigo):
            self.__tela_disciplina.mostrar_msg(f"Erro: Já existe uma disciplina com o código {codigo}.")
            return

        nome = dados_disciplina['nome']
        disciplina = Disciplina(nome, codigo) 
        self.__disciplina_dao.add(disciplina)

        self.__tela_disciplina.mostrar_msg(f"{disciplina.nome} cadastrada com sucesso!")

    def pega_disciplina_codigo(self, codigo: int):
        return self.__disciplina_dao.get(codigo)

    def listar_disciplina(self):
        lista_disciplinas = self.__disciplina_dao.get_all()
        if not lista_disciplinas:
            return
        para_mostrar = []
        for d in lista_disciplinas:
            para_mostrar.append({'nome': d.nome, 'codigo': d.codigo})

        self.__tela_disciplina.mostra_disciplina(para_mostrar)

    def obter_codigo(self):
        disciplina = self.selecionar_disciplina()
        if disciplina:
            return disciplina.codigo
        return None

    def matricular_aluno(self):
        disciplina = self.selecionar_disciplina()

        if disciplina:
            if not disciplina.turmas:
                self.__tela_disciplina.mostrar_msg(f"A disciplina {disciplina.nome} não possui turmas. Crie uma turma primeiro.")
                return

            turma = self.__controlador_principal.controladorturma.selecionar_turma_de_disciplina(disciplina)
            if not turma:
                return

            aluno = self.__controlador_principal.controladoraluno.incluir_aluno()
            if aluno is None:
                self.__tela_disciplina.mostrar_msg("Matrícula de aluno cancelada.")
                return
            
            try:
                if turma.matricular_aluno(aluno):
                    disciplina.matricular_aluno(aluno)
                
            except Exception as e:
                self.__tela_disciplina.mostrar_msg(f"Erro: {e}")

        elif disciplina is not None:
            self.__tela_disciplina.mostrar_msg("Erro: Disciplina não encontrada.")

    def alterar_disciplina(self):
        disciplina_a_alterar = self.selecionar_disciplina()
        if disciplina_a_alterar:
            nova_disciplina = self.__tela_disciplina.pega_dados_disciplina()
            if nova_disciplina is None:
                self.__tela_disciplina.mostrar_msg("Alteração cancelada.")
                return
            disciplina_a_alterar.nome = nova_disciplina["nome"]
            disciplina_a_alterar.codigo = int(nova_disciplina["codigo"])
            self.__disciplina_dao.update(disciplina_a_alterar)
            self.__disciplina_dao.update(disciplina_a_alterar)
            self.__tela_disciplina.mostrar_msg("Disciplina Alterada com Sucesso!")
            self.listar_disciplina()
        else:
            self.__tela_disciplina.mostrar_msg("Erro: A disciplina não existe")

    def excluir_disciplina(self):
        disciplina = self.selecionar_disciplina()

        if disciplina:
            self.__disciplina_dao.remove(disciplina.codigo)
            self.__tela_disciplina.mostrar_msg("Disciplina removida com sucesso!")
            self.listar_disciplina()
        else:
            self.__tela_disciplina.mostrar_msg("Erro: Disciplina não existe")

    def listar_aluno(self):
        if not self.__disciplina_dao.get_all():
            self.__tela_disciplina.mostrar_msg("Não existe nenhuma disciplina cadastrada")
            return
        self.listar_disciplina()
        codigo = self.obter_codigo()
        disciplina = self.pega_disciplina_codigo(codigo)

        if disciplina:
            alunos_disciplina = disciplina.alunos
            para_mostra = []

            if alunos_disciplina:
                self.__tela_disciplina.mostrar_msg(f"----Alunos Matriculados em: {disciplina}----")
                for aluno in alunos_disciplina:
                        para_mostra.append({"nome": aluno.nome, "matricula": aluno.matricula})

                self.__tela_disciplina.mostra_aluno(para_mostra)

            else:
                self.__tela_disciplina.mostrar_msg("Está disciplina não possui alunos matriculados")

        else:
            self.__tela_disciplina.mostrar_msg("Codigo da disciplina incorreto")         

    def sair(self):
        self.__controladorsistema.abre_tela()

    def selecionar_disciplina(self):
        disciplinas = self.__disciplina_dao.get_all()
        if not disciplinas:
            self.__tela_disciplina.mostrar_msg("Nenhuma disciplina cadastrada.")
            return None
        
        disciplina_selecionada = self.__tela_disciplina.seleciona_disciplina(list(disciplinas))
        return disciplina_selecionada

    def buscar_disciplina_por_aluno(self, matricula_aluno:int):
        disciplina_do_aluno = []
        for disciplina in self.__disciplina_dao.get_all():
            try:
                for aluno in disciplina.alunos:
                    if aluno.matricula == matricula_aluno:
                        disciplina_do_aluno.append(disciplina)
                        break
            except AttributeError:
                nome_disciplina = getattr(disciplina, 'nome', 'nome_disponivel')
                self.__tela_disciplina.mostrar_msg(f"A disciplina: {nome_disciplina} está com os dados incompletos")

        return disciplina_do_aluno
    
    @property
    def disciplina_dao(self):
        return self.__disciplina_dao
        
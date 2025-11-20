from entidade.disciplina import Disciplina
from limite.tela_disciplina import TelaDisciplina
from entidade.aluno import Aluno
from dao.disciplina_dao import DisciplinaDAO

class ControladorDisciplina():
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__disciplina_dao = DisciplinaDAO()
        self.__tela_disciplina = TelaDisciplina()

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
        codigo = int (dados_disciplina['codigo'])
        nome = dados_disciplina['nome']
        disciplina = Disciplina(nome, codigo) 
        self.__disciplina_dao.add(disciplina)

        self.__tela_disciplina.mostrar_msg(f"{disciplina.nome} cadastrada com sucesso!")

    def pega_disciplina_codigo(self, codigo: int):
        return self.__disciplina_dao.get(codigo)

    def listar_disciplina(self):
        lista_disciplinas = self.__disciplina_dao.get_all()
        if not lista_disciplinas:
            self.__tela_disciplina.mostrar_msg("Nenhuma disciplina encontrada")
            return
        para_mostrar = []
        for d in lista_disciplinas:
            para_mostrar.append({'nome': d.nome, 'codigo': d.codigo})

        self.__tela_disciplina.mostra_disciplina(para_mostrar)

    def obter_codigo(self):
        self.listar_disciplina()
        escolha_codigo = self.__tela_disciplina.seleciona_disciplina_codigo()

        return escolha_codigo

    def matricular_aluno(self):
        if not self.__disciplina_dao.get_all():
            self.__tela_disciplina.mostrar_msg("Erro: Nenhuma disciplina cadastrada")
            return
        
        self.listar_disciplina()
        codigo_escolhido = self.__tela_disciplina.seleciona_disciplina_codigo()
        disciplina = self.pega_disciplina_codigo(codigo_escolhido)

        if disciplina:
            if not disciplina.turmas:
                self.__tela_disciplina.mostrar_msg(f"A disciplina {disciplina.nome} não possui turmas. Crie uma turma primeiro.")
                return

            turma = self.__controlador_principal.controladorturma.selecionar_turma_de_disciplina(disciplina)
            if not turma:
                return

            aluno = self.__controlador_principal.controladoraluno.incluir_aluno()
            
            try:
                turma.matricular_aluno(aluno)
                disciplina.matricular_aluno(aluno)
                self.__tela_disciplina.mostrar_msg(f"Aluno {aluno.nome} matriculado na Turma {turma.numero} de {disciplina.nome} com sucesso!")
            except Exception as e:
                self.__tela_disciplina.mostrar_msg(f"Erro: {e}")

        else:
            self.__tela_disciplina.mostrar_msg("Erro: Disciplina não encontrada.")

    def alterar_disciplina(self):
        self.listar_disciplina()
        codigo_disciplina = self.__tela_disciplina.seleciona_disciplina_codigo()
        codigo = int(codigo_disciplina)
        disciplina_ha_alterar = self.pega_disciplina_codigo(codigo)

        if (disciplina_ha_alterar is not None):
            nova_disciplina = self.__tela_disciplina.pega_dados_disciplina()
            disciplina_ha_alterar.nome = nova_disciplina["nome"]
            disciplina_ha_alterar.codigo = int(nova_disciplina["codigo"])
            self.__disciplina_dao.update(disciplina_ha_alterar)
            self.__tela_disciplina.mostrar_msg("Disciplina Alterada com Sucesso!")
            self.listar_disciplina()
        else:
            self.__tela_disciplina.mostrar_msg("Erro: A disciplina não existe")

    def excluir_disciplina(self):
        self.listar_disciplina()
        codigo = self.__tela_disciplina.seleciona_disciplina_codigo()
        codigo_int = int(codigo)
        disciplina = self.pega_disciplina_codigo(codigo_int)

        if (disciplina is not None):
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
        if not self.__disciplina_dao.get_all():
            self.__tela_disciplina.mostrar_msg("Nenhuma disciplina cadastrada.")
            return None
        
        self.listar_disciplina()
        codigo = self.__tela_disciplina.seleciona_disciplina_codigo()
        codigo_int = int(codigo)
        disciplina = self.pega_disciplina_codigo(codigo_int)
        return disciplina

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
        
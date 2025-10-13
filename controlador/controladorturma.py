from limite.telaturma import TelaTurma
from entidade.turma import Turma


class ControladorTurma:
    def __init__(self, controladorsistema):
        # self.__turmas = [] # Recomendo que cada disciplina gerencie sua lista de turmas.
        self.__controlador_sistema = controladorsistema
        self.__tela_turma = TelaTurma()

    def criar_turma(self):
        # 1. Selecionar a disciplina
        controlador_disciplina = self.__controlador_sistema.controladordisciplina
        disciplina = controlador_disciplina.selecionar_disciplina()
        if not disciplina:
            return

        # 2. Pegar dados da turma
        dados_turma = self.__tela_turma.pega_dados_turma()
        if not dados_turma:
            return

        # 3. Criar e associar a turma
        nova_turma = Turma(dados_turma["sala"], dados_turma["numero"], dados_turma["semestre"])
        disciplina.adicionar_turma(nova_turma)
        self.__tela_turma.mostrar_msg(f"Turma {nova_turma.numero} criada para a disciplina {disciplina.nome} com sucesso!")

    def selecionar_turma_de_disciplina(self, disciplina):
        turmas = disciplina.turmas
        if not turmas:
            self.__tela_turma.mostrar_msg("Esta disciplina não possui turmas.")
            return None
        turma_selecionada = self.__tela_turma.seleciona_turma(turmas)
        return turma_selecionada
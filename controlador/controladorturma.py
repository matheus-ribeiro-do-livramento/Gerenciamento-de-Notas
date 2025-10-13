from limite.telaturma import TelaTurma
from entidade.turma import Turma


class ControladorTurma:
    def __init__(self, controladorsistema):
        self.__controlador_sistema = controladorsistema
        self.__tela_turma = TelaTurma()

    def criar_turma(self):
        controlador_disciplina = self.__controlador_sistema.controladordisciplina
        disciplina = controlador_disciplina.selecionar_disciplina()
        if not disciplina:
            return

        dados_turma = self.__tela_turma.pega_dados_turma()
        if not dados_turma:
            return

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

    def buscar_turma_do_aluno(self, aluno, disciplina):
        for turma in disciplina.turmas:
            if aluno in turma.alunos:
                return turma
        return None
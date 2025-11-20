from limite.telaturma import TelaTurma
from entidade.turma import Turma
from dao.disciplina_dao import DisciplinaDAO


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
        controlador_disciplina.disciplina_dao.update(disciplina)
        self.__tela_turma.mostrar_msg(f"Turma {nova_turma.numero} criada para a disciplina {disciplina.nome} com sucesso!")

    def listar_turma(self):
        controlador_disciplina = self.__controlador_sistema.controladordisciplina
        disciplina = controlador_disciplina.selecionar_disciplina()
        
        if disciplina is None:
            return
        
        if not disciplina.turmas:
            self.__tela_turma.mostrar_msg(f"A disciplina : {disciplina}, não possui turmas cadastradas.")
            return
        
        para_mostrar = []
        for turma in disciplina.turmas:
            para_mostrar.append({"sala": turma.sala , "numero": turma.numero,"semestre": turma.semestre})
        self.__tela_turma.mostra_turma(para_mostrar)


    def editar_turma(self):
        controlador_disciplina = self.__controlador_sistema.controladordisciplina
        disciplina = controlador_disciplina.selecionar_disciplina()

        if disciplina is None:
            return
        if not disciplina.turmas:
            self.__tela_turma.mostrar_msg(f"A disciplina : {disciplina}, não possui turmas cadastradas.")
            return
        
        self.listar_turma()
        numero_turma = self.__tela_turma.seleciona_numero_turma()


        turma_encontrada = None
        for turma in disciplina.turmas:
            if turma.numero == numero_turma:
                turma_encontrada = turma
                break

        
        if turma_encontrada is None:
            self.__tela_turma.mostrar_msg("Turma Encontrada")
            return
        
        atualizacao_dados = self.__tela_turma.pega_dados_turma()
        turma_encontrada.sala = atualizacao_dados['sala']
        turma_encontrada.numero = atualizacao_dados['numero']
        turma_encontrada.semestre = atualizacao_dados['semestre']

        controlador_disciplina.disciplina_dao.update(disciplina)
        self.__tela_turma.mostrar_msg("Alteração realizada com sucesso!")
     
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
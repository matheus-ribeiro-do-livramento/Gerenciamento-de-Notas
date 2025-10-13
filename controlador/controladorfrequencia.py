from limite.telafrequencia import TelaFrequencia
from entidade.frequencia import Frequencia

class ControladorFrequencia:
    def __init__(self, controladorsistema):
        self.__frequencias_por_turma = {} 
        self.__controlador_sistema = controladorsistema
        self.__tela_frequencia = TelaFrequencia()

    def lancar_frequencia(self):

        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if not disciplina:
            return


        turma = self.__controlador_sistema.controladorturma.selecionar_turma_de_disciplina(disciplina)
        if not turma:
            return

        data = self.__tela_frequencia.pegar_data()
        if not data:
            self.__tela_frequencia.mostrar_msg("Data não informada. Operação cancelada.")
            return

        if turma.numero not in self.__frequencias_por_turma:
            self.__frequencias_por_turma[turma.numero] = Frequencia(turma)
        
        objeto_frequencia = self.__frequencias_por_turma[turma.numero]


        alunos_da_turma = turma.alunos
        if not alunos_da_turma:
            self.__tela_frequencia.mostrar_msg("Não há alunos matriculados nesta turma.")
            return

        frequencia_do_dia = {}
        resumo_para_tela = {}
        for aluno in alunos_da_turma:
            status = self.__tela_frequencia.pegar_frequencia_aluno(aluno.nome)
            frequencia_do_dia[aluno.matricula] = status
            resumo_para_tela[aluno.nome] = status


        objeto_frequencia.registrar_frequencia(data, frequencia_do_dia)

 
        self.__tela_frequencia.mostrar_resumo_frequencia(data, resumo_para_tela)
        self.__tela_frequencia.mostrar_msg("Frequência registrada com sucesso!")

    def editar_frequencia(self):
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if not disciplina: return

        turma = self.__controlador_sistema.controladorturma.selecionar_turma_de_disciplina(disciplina)
        if not turma: return

        if turma.numero not in self.__frequencias_por_turma:
            self.__tela_frequencia.mostrar_msg("Nenhuma frequência foi lançada para esta turma ainda.")
            return
        
        objeto_frequencia = self.__frequencias_por_turma[turma.numero]
        historico = objeto_frequencia.historico
        if not historico:
            self.__tela_frequencia.mostrar_msg("Nenhuma frequência foi lançada para esta turma ainda.")
            return

        datas_disponiveis = list(historico.keys())
        data_selecionada = self.__tela_frequencia.seleciona_data(datas_disponiveis)
        if not data_selecionada: return

        alunos_da_turma = turma.alunos
        aluno_selecionado = self.__tela_frequencia.seleciona_aluno(alunos_da_turma)
        if not aluno_selecionado: return

        status_atual = historico[data_selecionada].get(aluno_selecionado.matricula)
        if status_atual is None:
            self.__tela_frequencia.mostrar_msg(f"O aluno {aluno_selecionado.nome} não possui registro de frequência para esta data.")
            return

        novo_status = self.__tela_frequencia.pega_nova_frequencia(aluno_selecionado.nome, status_atual)
        if not novo_status: return

        sucesso = objeto_frequencia.editar_frequencia_aluno(data_selecionada, aluno_selecionado.matricula, novo_status)
        if sucesso:
            self.__tela_frequencia.mostrar_msg("Frequência atualizada com sucesso!")
        else:
            self.__tela_frequencia.mostrar_msg("Ocorreu um erro ao atualizar a frequência.")

    def excluir_frequencia(self):
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if not disciplina: return

        turma = self.__controlador_sistema.controladorturma.selecionar_turma_de_disciplina(disciplina)
        if not turma: return

        if turma.numero not in self.__frequencias_por_turma:
            self.__tela_frequencia.mostrar_msg("Nenhuma frequência foi lançada para esta turma ainda.")
            return
        
        objeto_frequencia = self.__frequencias_por_turma[turma.numero]
        historico = objeto_frequencia.historico
        if not historico:
            self.__tela_frequencia.mostrar_msg("Nenhuma frequência foi lançada para esta turma ainda.")
            return

        datas_disponiveis = list(historico.keys())
        data_selecionada = self.__tela_frequencia.seleciona_data(datas_disponiveis)
        if not data_selecionada: return

        alunos_da_turma = turma.alunos
        aluno_selecionado = self.__tela_frequencia.seleciona_aluno(alunos_da_turma)
        if not aluno_selecionado: return

        confirmado = self.__tela_frequencia.confirma_exclusao(aluno_selecionado.nome, data_selecionada)
        if not confirmado:
            return

        sucesso = objeto_frequencia.excluir_frequencia_aluno(data_selecionada, aluno_selecionado.matricula)
        if sucesso:
            self.__tela_frequencia.mostrar_msg("Registro de frequência excluído com sucesso!")
        else:
            self.__tela_frequencia.mostrar_msg("Erro: Registro de frequência não encontrado para este aluno nesta data.")

    def calcular_frequencia_aluno(self, turma, aluno):
        if turma.numero not in self.__frequencias_por_turma:
            return None 

        objeto_frequencia = self.__frequencias_por_turma[turma.numero]
        historico = objeto_frequencia.historico

        total_aulas = len(historico)
        if total_aulas == 0:
            return None

        presencas = 0
        for data in historico:
            if historico[data].get(aluno.matricula) == 'P':
                presencas += 1
        
        percentual = (presencas / total_aulas) * 100
        return percentual
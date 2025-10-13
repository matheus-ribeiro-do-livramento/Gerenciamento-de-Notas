from limite.telafrequencia import TelaFrequencia
from entidade.frequencia import Frequencia

class ControladorFrequencia:
    def __init__(self, controladorsistema):
        self.__frequencias_por_turma = {} 
        self.__controlador_sistema = controladorsistema
        self.__tela_frequencia = TelaFrequencia()

    def selecionar_turma_interativamente(self):
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if not disciplina:
            return None
        turma = self.__controlador_sistema.controladorturma.selecionar_turma_de_disciplina(disciplina)
        if not turma:
            return None
        return turma

    def obter_ou_criar_frequencia_da_turma(self, turma):
        if turma.numero not in self.__frequencias_por_turma:
            self.__frequencias_por_turma[turma.numero] = Frequencia(turma)
        return self.__frequencias_por_turma[turma.numero]

    def coletar_frequencias_dos_alunos(self, alunos_da_turma: list):
        frequencia_do_dia = {}
        resumo_para_tela = {}
        for aluno in alunos_da_turma:
            status = self.__tela_frequencia.pegar_frequencia_aluno(aluno.nome)
            frequencia_do_dia[aluno.matricula] = status
            resumo_para_tela[aluno.nome] = status
        return frequencia_do_dia, resumo_para_tela

    def lancar_frequencia(self):
        turma = self.selecionar_turma_interativamente()
        if not turma: 
            return

        if not turma.alunos:
            self.__tela_frequencia.mostrar_msg("Não há alunos matriculados nesta turma.")
            return
        
        data = self.__tela_frequencia.pegar_data()
        if not data: 
            return

        objeto_frequencia = self.obter_ou_criar_frequencia_da_turma(turma)
        frequencia_do_dia, resumo_para_tela = self.coletar_frequencias_dos_alunos(turma.alunos)
        objeto_frequencia.registrar_frequencia(data, frequencia_do_dia)

        self.__tela_frequencia.mostrar_resumo_frequencia(data, resumo_para_tela)
        self.__tela_frequencia.mostrar_msg("Frequência registrada com sucesso!")

    def editar_frequencia(self):
        turma = self.selecionar_turma_interativamente()
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
        if not data_selecionada: 
            return

        aluno_selecionado = self.__tela_frequencia.seleciona_aluno(turma.alunos)
        if not aluno_selecionado: 
            return

        status_atual = historico[data_selecionada].get(aluno_selecionado.matricula)
        if status_atual is None:
            self.__tela_frequencia.mostrar_msg(f"O aluno {aluno_selecionado.nome} não possui registro de frequência para esta data.")
            return

        novo_status = self.__tela_frequencia.pega_nova_frequencia(aluno_selecionado.nome, status_atual)
        if not novo_status:
            return

        sucesso = objeto_frequencia.editar_frequencia_aluno(data_selecionada, aluno_selecionado.matricula, novo_status)
        if sucesso:
            self.__tela_frequencia.mostrar_msg("Frequência atualizada com sucesso!")
        else:
            self.__tela_frequencia.mostrar_msg("Ocorreu um erro ao atualizar a frequência.")

    def excluir_frequencia(self):
        turma = self.selecionar_turma_interativamente()
        if not turma: return

        objeto_frequencia = self.__frequencias_por_turma.get(turma.numero)
        if not objeto_frequencia or not objeto_frequencia.historico:
            self.__tela_frequencia.mostrar_msg("Nenhuma frequência foi lançada para esta turma ainda.")
            return

        datas_disponiveis = list(objeto_frequencia.historico.keys())
        data_selecionada = self.__tela_frequencia.seleciona_data(datas_disponiveis)
        if not data_selecionada: return

        aluno_selecionado = self.__tela_frequencia.seleciona_aluno(turma.alunos)
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
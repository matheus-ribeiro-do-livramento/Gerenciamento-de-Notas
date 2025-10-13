from limite.telafrequencia import TelaFrequencia
from entidade.frequencia import Frequencia

class ControladorFrequencia:
    def __init__(self, controladorsistema):
        # Dicionário para armazenar um objeto Frequencia por turma
        self.__frequencias_por_turma = {} # Chave: turma.numero, Valor: objeto Frequencia
        self.__controlador_sistema = controladorsistema
        self.__tela_frequencia = TelaFrequencia()

    def lancar_frequencia(self):
        # 1. Selecionar a disciplina
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if not disciplina:
            return

        # 2. Selecionar a turma
        turma = self.__controlador_sistema.controladorturma.selecionar_turma_de_disciplina(disciplina)
        if not turma:
            return

        # 3. Pegar a data da aula
        data = self.__tela_frequencia.pegar_data()
        if not data:
            self.__tela_frequencia.mostrar_msg("Data não informada. Operação cancelada.")
            return

        # 4. Garante que existe um objeto Frequencia para esta turma
        if turma.numero not in self.__frequencias_por_turma:
            self.__frequencias_por_turma[turma.numero] = Frequencia(turma)
        
        objeto_frequencia = self.__frequencias_por_turma[turma.numero]

        # 5. Percorre os alunos da turma para registrar a frequência
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

        # 6. Salva o registro no objeto Frequencia
        objeto_frequencia.registrar_frequencia(data, frequencia_do_dia)

        # 7. Mostra um resumo para o professor
        self.__tela_frequencia.mostrar_resumo_frequencia(data, resumo_para_tela)
        self.__tela_frequencia.mostrar_msg("Frequência registrada com sucesso!")

    def editar_frequencia(self):
        # 1. Selecionar disciplina e turma
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if not disciplina: return

        turma = self.__controlador_sistema.controladorturma.selecionar_turma_de_disciplina(disciplina)
        if not turma: return

        # 2. Verificar se existem registros de frequência para a turma
        if turma.numero not in self.__frequencias_por_turma:
            self.__tela_frequencia.mostrar_msg("Nenhuma frequência foi lançada para esta turma ainda.")
            return
        
        objeto_frequencia = self.__frequencias_por_turma[turma.numero]
        historico = objeto_frequencia.historico
        if not historico:
            self.__tela_frequencia.mostrar_msg("Nenhuma frequência foi lançada para esta turma ainda.")
            return

        # 3. Selecionar a data
        datas_disponiveis = list(historico.keys())
        data_selecionada = self.__tela_frequencia.seleciona_data(datas_disponiveis)
        if not data_selecionada: return

        # 4. Selecionar o aluno
        alunos_da_turma = turma.alunos
        aluno_selecionado = self.__tela_frequencia.seleciona_aluno(alunos_da_turma)
        if not aluno_selecionado: return

        # 5. Pegar o novo status
        status_atual = historico[data_selecionada].get(aluno_selecionado.matricula)
        if status_atual is None:
            self.__tela_frequencia.mostrar_msg(f"O aluno {aluno_selecionado.nome} não possui registro de frequência para esta data.")
            return

        novo_status = self.__tela_frequencia.pega_nova_frequencia(aluno_selecionado.nome, status_atual)
        if not novo_status: return

        # 6. Atualizar a frequência
        sucesso = objeto_frequencia.editar_frequencia_aluno(data_selecionada, aluno_selecionado.matricula, novo_status)
        if sucesso:
            self.__tela_frequencia.mostrar_msg("Frequência atualizada com sucesso!")
        else:
            self.__tela_frequencia.mostrar_msg("Ocorreu um erro ao atualizar a frequência.")

    def calcular_frequencia_aluno(self, turma, aluno):
        if turma.numero not in self.__frequencias_por_turma:
            return None # Se não houve aula, não há dados de frequência

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
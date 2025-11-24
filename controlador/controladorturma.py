from limite.telaturma import TelaTurma
from entidade.turma import Turma
from dao.disciplina_dao import DisciplinaDAO


class ControladorTurma:
    def __init__(self, controladorsistema):
        self.__controlador_sistema = controladorsistema
        self.__tela_turma = TelaTurma()

    @property
    def tela_turma(self):
        return self.__tela_turma

    def criar_turma(self):
        controlador_disciplina = self.__controlador_sistema.controladordisciplina
        disciplina = controlador_disciplina.selecionar_disciplina()
        if not disciplina:
            return

        dados_turma = self.__tela_turma.pega_dados_turma()
        if dados_turma is None:
            return
        
        numero_turma = dados_turma.get('numeroturma')
        for turma_existente in disciplina.turmas:
            if turma_existente.numero == numero_turma:
                return

        nova_turma = disciplina.criar_e_adicionar_turma(dados_turma["sala"], 
                                                        dados_turma["numeroturma"], 
                                                        dados_turma["semestre"])
        controlador_disciplina.disciplina_dao.update(disciplina)
        self.__tela_turma.mostrar_msg(f"Turma {nova_turma.numero} criada para a disciplina {disciplina.nome} com sucesso!")

    def listar_turma(self, disciplina=None):
        if disciplina is None:
            controlador_disciplina = self.__controlador_sistema.controladordisciplina
            disciplina = controlador_disciplina.selecionar_disciplina()

        if disciplina is None:
            return
        
        if not disciplina.turmas:
            self.__tela_turma.turma_nao_cadastrada()
            return
        
        para_mostrar = []
        for turma in disciplina.turmas:
            para_mostrar.append({"sala": turma.sala , "numeroturma": turma.numero,"semestre": turma.semestre})
        self.__tela_turma.mostra_turma(para_mostrar)


    def editar_turma(self):
        controlador_disciplina = self.__controlador_sistema.controladordisciplina
        disciplina = controlador_disciplina.selecionar_disciplina()

        if disciplina is None:
            return
        if not disciplina.turmas:
            self.__tela_turma.turma_nao_cadastrada()
            return
        
        turma_para_editar = self.selecionar_turma_de_disciplina(disciplina)
        if not turma_para_editar:
            return
        
        atualizacao_dados = self.__tela_turma.pega_dados_turma()
        if not atualizacao_dados:
            return
        
        # Validação para garantir que o novo número da turma não colida com um existente
        if turma_para_editar.numero != atualizacao_dados['numeroturma'] and any(t.numero == atualizacao_dados['numeroturma'] for t in disciplina.turmas):
            self.__tela_turma.mostrar_msg("Erro: Já existe uma turma com este novo número.")
            return
        
        turma_para_editar.sala = atualizacao_dados['sala']
        turma_para_editar.numero = atualizacao_dados['numeroturma']
        turma_para_editar.semestre = atualizacao_dados['semestre']

        controlador_disciplina.disciplina_dao.update(disciplina)
        self.__tela_turma.mostrar_msg("Turma editada com sucesso!")

     
    def selecionar_turma_de_disciplina(self, disciplina):
        turmas = disciplina.turmas
        if not turmas:
            self.__controlador_sistema.controladordisciplina.tela_disciplina.disciplina_sem_turma()
            return None
        else:
            turma_selecionada = self.__tela_turma.seleciona_turma(turmas)
            return turma_selecionada

    def buscar_turma_do_aluno(self, aluno, disciplina):
        for turma in disciplina.turmas:
            for alunos_na_turma in turma.alunos:
                if alunos_na_turma.matricula == aluno.matricula:
                    return turma
        return None
    
    def excluir_turma(self):
        controlador_disciplina = self.__controlador_sistema.controladordisciplina
        disciplina = controlador_disciplina.selecionar_disciplina()
        

        if disciplina is None:
            return

        if not disciplina.turmas:
            self.__tela_turma.turma_nao_cadastrada()
            return  

        else:
            turma_para_excluir = self.selecionar_turma_de_disciplina(disciplina)
            if not turma_para_excluir:
                return

            disciplina.turmas.remove(turma_para_excluir)
            controlador_disciplina.disciplina_dao.update(disciplina)
            self.__tela_turma.mostrar_msg("Turma excluída com sucesso!")

        
        

        

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
        
        self.listar_turma(disciplina)

        try:
            numero_turma = int(self.__tela_turma.seleciona_numero_turma())
        except ValueError:
            self.__tela_turma.mostrar_msg("O numero deve ser inteiro")
            return

        turma_encontrada = None
        for turma in disciplina.turmas:
            if turma.numero == numero_turma:
                turma_encontrada = turma
                break

        if turma_encontrada is None:
            self.__tela_turma.mostrar_msg("Turma NÃO Encontrada")
            return
        
        atualizacao_dados = self.__tela_turma.pega_dados_turma()
        if not atualizacao_dados:
            return
        
        turma_encontrada.sala = atualizacao_dados['sala']
        turma_encontrada.numero = atualizacao_dados['numeroturma']
        turma_encontrada.semestre = atualizacao_dados['semestre']

        controlador_disciplina.disciplina_dao.update(disciplina)

     
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
            self.listar_turma(disciplina)
            numero = self.__tela_turma.seleciona_numero_turma()
            if not numero:
                return

            for c in disciplina.turmas:
                if c.numero == int(numero):
                    disciplina.turmas.remove(c)

        
        

        

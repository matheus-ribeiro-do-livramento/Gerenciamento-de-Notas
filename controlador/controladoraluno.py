from entidade.aluno import Aluno
from limite.telaaluno import TelaAluno

class ControladorAluno():
    def __init__(self, controlador_sistema):
        self.__alunos = []
        self.__controlador_sistema = controlador_sistema
        self.__tela_aluno = TelaAluno()

    
    def pega_aluno_matricula(self, matricula):
        for a in self.__alunos:
            if (a.matricula == matricula):
                return a
        return None


    def incluir_aluno(self):
        dados_aluno = self.__tela_aluno.pega_dados_aluno()
        matricula = dados_aluno["matricula"]
        
        aluno_existente = self.pega_aluno_matricula(matricula)
        if aluno_existente:
            self.__tela_aluno.mostrar_msg("Aluno com esta matrícula já cadastrado. Utilizando aluno existente.")
            return aluno_existente

        aluno_novo = Aluno(dados_aluno["nome"], matricula)
        self.__alunos.append(aluno_novo)
        self.__tela_aluno.mostrar_msg("Aluno incluido com sucesso!")
        return aluno_novo

    def alterar_aluno(self):
        self.listar_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_matricula(matricula_aluno)

        if (aluno is not None):
            novos_dados = self.__tela_aluno.pega_dados_aluno()
            aluno.nome = novos_dados["nome"]
            aluno.matricula = novos_dados["matricula"]
            self.listar_alunos()
        else:
            self.__tela_aluno.mostrar_msg("Erro: Aluno não existe")

    def listar_alunos(self):
        for a in self.__alunos:
            self.__tela_aluno.mostra_aluno({"nome": a.nome, "matricula": a.matricula})

    def excluir_aluno(self):
        self.listar_alunos()
        matricula_aluno = self.__tela_aluno.seleciona_aluno()
        aluno = self.pega_aluno_matricula(matricula_aluno)

        if (aluno is not None):
            self.__alunos.remove(aluno)
            self.listar_alunos()
        else:
            self.__tela_aluno.mostrar_msg("Erro: Aluno não existe")

    def sair(self):
        self.__controlador_sistema.abre_tela()

    def abre_tela(self):
        list_opcoes = {1: self.incluir_aluno, 2: self.listar_alunos, 3: self.alterar_aluno, 4: self.excluir_aluno, 5: self.sair}

        continua = True
        while continua:
            list_opcoes[self.__tela_aluno.tela_opcoes()]()
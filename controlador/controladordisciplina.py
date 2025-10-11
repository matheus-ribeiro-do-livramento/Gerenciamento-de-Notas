from entidade.disciplina import Disciplina
from limite.tela_disciplina import TelaDisciplina
from entidade.aluno import Aluno

class ControladorDisciplina():
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__disciplinas = []
        self.__tela_disciplina = TelaDisciplina()

    def abre_tela(self):
        while True:
            opcao = self.__tela_disciplina.tela_opcoes()

            if opcao == 1:
                self.cadastrar_aluno()
            elif opcao == 2:
                self.cadastrar_disciplina()
            elif opcao == 3:
                self.alterar_disciplina()  
            elif opcao == 4:
                self.excluir_disciplina()
            elif opcao == 5:
                pass
            elif opcao == 6:
                self.listar_disciplina()
            elif opcao == 7:
                self.sair()
            else:
                self.__tela_disciplina.mostrar_msg("Opção inválida!")
                self.sair()
                
            
    def cadastrar_disciplina(self):
        dados_disciplina = self.__tela_disciplina.pega_dados_disciplina()
        disciplina = Disciplina(dados_disciplina["nome"], dados_disciplina["codigo"])
        self.__disciplinas.append(disciplina)

        self.__tela_disciplina.mostrar_msg(f"{disciplina.nome} cadastrada com sucesso!")

    def pega_disciplina_codigo(self, codigo: str):
        for d in self.__disciplinas:
            if (d.codigo == codigo):
                return d
        return None

    def listar_disciplina(self):
        para_mostrar = []
        for d in self.__disciplinas:
            para_mostrar.append({'nome': d.nome, 'codigo': d.codigo})

        self.__tela_disciplina.mostra_disciplina(para_mostrar)

    def obter_codigo(self):
        self.listar_disciplina()
        escolha_codigo = self.__tela_disciplina.seleciona_disciplina_codigo()

        return escolha_codigo

    def cadastrar_aluno(self):
        if not self.__disciplinas:
            self.__tela_disciplina.mostrar_msg("Erro: Nenhuma disciplina cadastrada")
            return
        self.listar_disciplina()
        codigo_escolhido = self.obter_codigo()
        disciplina_escolhida = self.pega_disciplina_codigo(codigo_escolhido)

        if disciplina_escolhida:
            dados_aluno = self.__tela_disciplina.pega_dados_aluno()
            aluno = Aluno(dados_aluno["nome"], dados_aluno["matricula"])
            
            try:
                disciplina_escolhida.matricular_aluno(aluno)
                self.__tela_disciplina.mostrar_msg(f"Aluno {aluno} matriculado em {disciplina_escolhida.nome} com sucesso!")
            
            except Exception as e:
                self.__tela_disciplina.mostrar_msg(f"Erro: {e}")

        else:
            self.__tela_disciplina.mostrar_msg("Erro: O codigo da disciplina é invalido")

    def alterar_disciplina(self):
        self.listar_disciplina()
        codigo_disciplina = self.__tela_disciplina.seleciona_disciplina_codigo()
        alterar_disciplina = self.pega_disciplina_codigo(codigo_disciplina)

        if (alterar_disciplina is not None):
            nova_disciplina = self.__tela_disciplina.pega_dados_disciplina()
            alterar_disciplina.nome = nova_disciplina["nome"]
            alterar_disciplina.codigo = nova_disciplina["codigo"]
            self.listar_disciplina()
        else:
            self.__tela_disciplina.mostrar_msg("Erro: A disciplina não existe")

    def excluir_disciplina(self):
        self.listar_disciplina()
        codigo = self.__tela_disciplina.seleciona_disciplina_codigo()
        disciplina = self.pega_disciplina_codigo(int(codigo))

        if (disciplina is not None):
            self.__disciplinas.remove(disciplina)
            self.listar_disciplina
        else:
            self.__tela_disciplina.mostrar_msg("Erro: Disciplina não existe")

    def sair(self):
        self.__controladorsistema.abre_tela()

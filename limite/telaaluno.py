class TelaAluno:
    
    def tela_opcoes(self):
        print("----------Alunos----------")
        print("1 - Incluir Aluno")
        print("2 - Alterar Aluno")
        print("3 - Listar Aluno")
        print("4 - Excluir Aluno")
        print("5 - Sair")

        opcao = int(input("Escolha uma opcao:"))
        return opcao


    def pega_dados_aluno(self):
        print("----------Dados Aluno----------")
        nome = input("Nome:")
        matricula = input("Matricula:")

        return {'nome': nome, 'matricula': matricula}
    
    def mostra_aluno(self, dados_aluno):
        print("Nome do Aluno:",dados_aluno["nome"])
        print("Matricula do Aluno:",dados_aluno["matricula"])
        print("\n")

    def seleciona_aluno(self):
        matricula = input("Digite a matricula do Aluno que deseja selecionar:")
        return matricula
    
    def mostrar_msg(self, msg):
        print(msg)
class TelaDisciplina():

    def tela_opcoes(self):
        print("----------Disciplina----------")
        print("Escolha uma das opções abaixo")
        print("1 - Adicionar um Aluno")
        print("2 - Cadastrar Disciplina")
        print("3 - Alterar Disciplina")
        print("4 - Alterar Disciplina")
        print("5 - Excluir Disciplina")
        print("6 - Listar Aluno")
        print("7 - Listar Disciplina")
        print("8 - sair")

        opcao = int(input("Escolha uma opcao:"))
        return opcao

    def pega_dados_aluno(self):
        print("----------Dados do Aluno----------")
        nome = input("Digite o Nome do Aluno:")
        matricula = int(input("Digite a Matricula do Aluno:"))
        disciplina = input("Digite a Disciplina do Aluno:")

        return {"nome": nome, "matricula": matricula, "disciplina": disciplina}

    def pega_dados_disciplina(self):
        print("----------Dados Disciplina----------")
        nome = input("Digite o nome da Disciplina")
        codigo =input("Digite o COdigo da Disciplina")

        return {"nome": nome, "codigo": codigo}
    
    def mostrar_msg(self, msg):
        print(msg)

    def mostra_disciplina(self, dados_disciplina):
        print("----------Lista de Disciplinas----------")
        print("Nome da Disciplina:", dados_disciplina["nome"])
        print("Codigo:", dados_disciplina["codigo"])
        print("\n")

    def seleciona_disciplina_codigo(self):
        codigo = input("Digite o codigo da disciplina")
        return codigo
    
    
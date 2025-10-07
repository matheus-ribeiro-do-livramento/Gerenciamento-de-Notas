class TelaDisciplina():

    def tela_opcoes(self):
        print("----------Disciplina----------")
        print("Escolha uma das opções abaixo")
        print("1 - Adicionar um Aluno")
        print("2 - Alterar um Aluno")
        print("3 - Excluir um Aluno")
        print("4 - listar os Alunos")
        print("5 - Sair")

        opcao = int(input("Escolha uma opcao:"))
        if isinstance(opcao, int):
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


class TelaDisciplina():

    def tela_opcoes(self):
        print("-----Disciplina-----")
        print("Escolha uma das opções abaixo")
        print("1 - Matricular Aluno")
        print("2 - Cadastrar Disciplina")
        print("3 - Listar Disciplina")
        print("4 - Alterar Disciplina")
        print("5 - Excluir Disciplina")
        print("6 - Listar Aluno")
        print("7 - sair")

        while True:
            try:
                opcao = int(input("Escolha uma opcao:"))
                if opcao in range(8):
                    return opcao
                else:
                    self.mostrar_msg("Opção inválida. Por favor, escolha uma das opções listadas.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")
            except KeyboardInterrupt:
                return 7

    def pega_dados_aluno(self):
        print("----------Dados do Aluno----------")
        nome = input("Digite o Nome do Aluno: ")
        matricula = input("Digite a Matricula do Aluno: ")

        return {"nome": nome, "matricula": matricula}

    def pega_dados_disciplina(self):
        print("----------Dados Disciplina----------")
        nome = input("Digite o nome da Disciplina: ")
        codigo = input("Digite o Código da Disciplina: ")

        return {"nome": nome, "codigo": codigo}
    
    def mostrar_msg(self, msg):
        print(msg)

    def mostra_disciplina(self, lista_dados_disciplina):
        print("----------Lista de Disciplinas----------")
        if not lista_dados_disciplina:
            print("Nenhuma disciplina cadastrada.")
            return
        

        if not isinstance(lista_dados_disciplina, list):
            lista_dados_disciplina = [lista_dados_disciplina]

        for disciplina in lista_dados_disciplina:
            print(f"Nome: {disciplina['nome']}, Código: {disciplina['codigo']}")

    def seleciona_disciplina_codigo(self):
        codigo = input("Digite o codigo da disciplina: ")
        return codigo
    
    def seleciona_matricula_aluno(self):
        matricula = input("Digite a Matricula:")
        return matricula
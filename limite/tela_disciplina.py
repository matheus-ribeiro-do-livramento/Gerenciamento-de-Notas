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

        opcao = int(input("Escolha uma opcao:"))
        return opcao

    def pega_dados_disciplina(self):
        print("-----Dados Disciplina-----")
        nome = input("Digite o nome da Disciplina")
        codigo =input("Digite o COdigo da Disciplina")

        return {"nome": nome, "codigo": codigo}
    
    def mostrar_msg(self, msg):
        print(msg)

    def mostra_disciplina(self, dados_disciplina):
        print("-----Lista de Disciplinas-----")
        if isinstance(dados_disciplina, list):
            for disciplina in dados_disciplina:
                print(f"Nome: {disciplina['nome']}, Codigo: {disciplina['codig']}")
            print("--------------------")
        

    def mostra_aluno(self, dados_aluno):
        print("-----Listar Alunos-----")
        if isinstance(dados_aluno, list):
            for aluno in dados_aluno:
                print(f"Nome: {aluno['nome']}, Matricula: {aluno['matricula']}")
            print("--------------------")

    def seleciona_disciplina_codigo(self):
        codigo = input("Digite o codigo da disciplina")
        return codigo
    
    def seleciona_matricula_aluno(self):
        matricula = input("Digite a Matricula:")
        return matricula
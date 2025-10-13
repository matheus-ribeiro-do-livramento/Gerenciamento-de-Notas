class TelaAluno:
    
    def tela_opcoes(self):
        print("----------Alunos----------")
        print("1 - Incluir Aluno")
        print("2 - Alterar Aluno")
        print("3 - Listar Aluno")
        print("4 - Excluir Aluno")
        print("0 - Voltar")

        while True:
            try:
                opcao = int(input("Escolha uma opcao:"))
                if opcao in [0,1,2,3,4]:
                    return opcao
                else:
                    print("Opção invalida, por favor escolha umas das opcoes listdas")
            except ValueError:
                print("Entrada invalida!, Por favor tente novamente")

    def tela_opcoes_login_cadastro(self):
        print("-----Eldoom-----")
        print("Você gostaria de ?")
        print("1 - Logar")
        print("2 - Cadastrar")
        print("0 - Voltar")

        while True:
            try:
                opcao = int(input("Escolha uma opcao:"))
                if opcao in (0,1,2):
                    return opcao
                else:
                    print("Opcao invalida")
            except ValueError:
                print("Opção incoferre, tente novamente")
            
    def pega_dados_aluno(self):
        print("----------Dados Aluno----------")
        try:
            nome = input("Nome: ").strip()
            if not nome:
                print("Erro: Nome não pode ser vazio.")
                return None
            matricula = int(input("Matricula: "))
            return {'nome': nome, 'matricula': matricula}
        except ValueError:
            print("Erro: Matrícula deve ser um número.")
            return None
        except KeyboardInterrupt:
            return None
    
    def mostra_aluno(self, dados_aluno):
        print("-----Listagem de Alunos-----")
        if isinstance(dados_aluno, list):
            for aluno in dados_aluno:
                print(f"Nome: {aluno['nome']}, Matrícula: {aluno['matricula']}")
        else:
            print(f"Nome: {dados_aluno['nome']}, Matrícula: {dados_aluno['matricula']}")

    def seleciona_aluno(self):
        matricula = int(input("Digite a matricula do Aluno que deseja selecionar:"))
        return matricula
    
    def mostrar_msg(self, msg):
        print(msg)

    def tela_login(self):
        print('-----Eldoom-----')
        print('     login     ')
        print()
        print()
        while True:
            try:
                matricula_login = int(input('Matricula: '))
                return matricula_login
            except ValueError:
                print('Opção não correspondida, tente novamente.')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário.')
                return 0
    
    def tela_funcoes_aluno_logado(self, nome_aluno):
        print(f"------Bem vindo (a), {nome_aluno}-----")
        print("O que gostaria de fazer?")
        print("1 - Ver minhas notas")
        print("2 - listar minhas disciplinas")
        print("3 - Frequencia")
        print("4 - Ver boletim")
        print("5 - Ver desempenho")
        print("0 - Sair")

        while True:
            try:
                opcao = int(input("Digite a opcao desejada:"))
                if opcao in [0,1,2,3,4,5]:
                    return opcao
                else:
                    print("Opcao invalida, Tente novamente")

            except ValueError:
                print("Entrada invalida, Tente novamente")

    def tela_cadastro(self):
        print('-----Eldoom-----')
        print('   Cadastrar    ')
        print()
        print()
        while True:
            try:
                nome = str(input('Digite seu nome: ')).strip()
                if not nome:
                    print("O nome não pode ser vazio.")
                    continue
                matricula_cadastro = int(input('Coloque a matricula: '))
                return nome, matricula_cadastro
            except ValueError:
                print("Matrícula inválida. Por favor, digite apenas números.")
            except KeyboardInterrupt:
                print("\nCadastro cancelado.")
                return None, None

    

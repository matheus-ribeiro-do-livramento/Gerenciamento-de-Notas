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
                print("Opção incorreta, tente novamente")
            
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

    def mostra_disciplina(self, dados_disciplina):
        print("-----Suas Disciplinas-----")
        if not dados_disciplina:
            print("Você não está matriculado a nenhuma disciplina")
            input("Pressione ENTER para prosseguir")
            return
    
        for disciplina in dados_disciplina:
                print(f"Nome: {disciplina['nome']}, Codigo: {disciplina['codigo']}")

        input("Pressione ENTER para prosseguir")

    def mostra_frequencia(self, resultados: list):
        print("\n----- Sua Frequência-----")
        if not resultados:
            print("Não foi possível calcular sua frequência em nenhuma disciplina.")
            input("\nPressione ENTER para continuar...")
            return

        for item in resultados:
            percentual = item['percentual']
            if percentual is not None:
                print(f"{item['disciplina']}: {percentual:.2f}% de presença")
            else:
                print(f"{item['disciplina']}: Nenhuma frequência registrada ainda.")
        
        input("\nPressione ENTER para prosseguir")
    
    def mostra_boletim(self, boletim_data: list):
        print("\n--- SEU BOLETIM ---")
        if not boletim_data:
            self.mostrar_msg("Nenhum dado de boletim disponível.")
            input("\nPressione ENTER para continuar...")
            return

        for item in boletim_data:
            print(f"\nDisciplina: {item['nome_disciplina']} (Código: {item['codigo_disciplina']})")
            print(f"  Professor(a): {item['professor_nome']}")
            
            if item['notas']:
                notas_str = ", ".join([f"{n:.2f}" for n in item['notas']])
                print(f"  Notas: [{notas_str}]")
            else:
                print("  Notas: Nenhuma nota lançada.")
            
            if item['media'] is not None:
                print(f"  Média: {item['media']:.2f}")
            else:
                print("  Média: Não calculada (sem notas).")
            
            if item['frequencia'] is not None:
                print(f"  Frequência: {item['frequencia']:.2f}%")
            else:
                print("  Frequência: Não disponível (sem registro de frequência).")
            print("-" * 10)
        
        input("\nPressione ENTER para continuar...")



    def seleciona_aluno(self):
        while True:
            try:
                matricula = int(input("Digite a matricula do Aluno que deseja selecionar: "))
                return matricula
            except ValueError:
                print("Entrada inválida. Por favor, digite um número para a matrícula.")
            except KeyboardInterrupt:
                print("\nOperação cancelada.")
                return None

    
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
        print("3 - Ver minha Frequencia")
        print("4 - Ver boletim")
        print("0 - Sair")

        while True:
            try:
                opcao = int(input("Digite a opcao desejada:"))
                if opcao in [0,1,2,3,4,]:
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

    

class TelaProfessor:
    def mostrar_msg(self, msg: str):
        print(msg)
        
    def pegar_codigo_disciplina(self):
        print('\n--- Vincular Disciplina ---')
        while True:
            try:
                codigo = input('Digite o código da disciplina: ').strip()
                if codigo:
                    return codigo
                print('Código não pode ser vazio!')
            except KeyboardInterrupt:
                print('\nOperação cancelada pelo usuário.')
                return None
                
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
        
    def tela_opcoes(self):
        print('-----Eldoom-----')
        print('Você gostaria de ?')
        print('1 - Logar')
        print('2 - Cadastrar')
        print('0 - Voltar')
        while True:
            try:
                opcao = int(input('Escolha uma opção: '))
                return opcao
            except ValueError:
                print('Opção não correspondida, tente novamente.')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário.')
                return 0



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
                return 0, 0

    
    def mostrar_msg(self, msg):
        print(msg)

    def tela_funcoes(self, nome = 'professor(a)'):
        print('-----Eldoom-----')
        print(f'Bem vindo {nome}!')
        print()
        print('O que gostaria de fazer?')
        print('1 - Criar disciplina')
        print('2 - Vincular a uma disciplina')
        print('3 - Criar Turma')
        print('4 - Matricular aluno em disciplina')
        print('5 - Adicionar nota')
        print('6 - Editar nota')
        print('7 - Excluir nota')
        print('8 - Lançar Frequência')
        print('9 - Editar Frequência')
        print('10 - Excluir Frequência')
        print('11 - Listar status dos alunos')
        print('12 - Consultar notas de aluno')
        print('0 - Sair')
        while True:
            try:
                opcao = int(input('Qual opção deseja: '))
                return opcao
            except ValueError:
                print('Opção não correspondida, tente novamente.')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário.')
                return 0

    def mostra_status_alunos(self, dados_alunos: list):
        print("\n--- Status dos Alunos ---")
        if not dados_alunos:
            print("Nenhum aluno para exibir.")
            return
        
        for dados in dados_alunos:
            print(f"Disciplina: {dados['disciplina']}")
            print(f"  Aluno: {dados['nome']} (Matrícula: {dados['matricula']})")

            if dados['notas']:
                notas_str = ", ".join(map(str, dados['notas']))
                print(f"  Notas: [{notas_str}]")

            media_str = f"{dados['media']:.2f}" if isinstance(dados['media'], (int, float)) else "Não cadastrada"
            print(f"  Média: {media_str}")

            frequencia_str = f"{dados['frequencia']:.2f}%" if isinstance(dados['frequencia'], (int, float)) else "Não cadastrada"
            print(f"  Frequência: {frequencia_str}\n")

        
    
    
    

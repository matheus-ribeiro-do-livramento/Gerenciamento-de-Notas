class TelaProfessor:
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
        print('Você gostaria de?')
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
                nome = str(input('Digite seu nome: ')).strip()
                disciplina = str(input('coloque sua disciplina: ')).strip()
                matricula_cadastro = int(input('Coloque a matricula: '))
                return nome, disciplina, matricula_cadastro

    
    def mostrar_msg(self, msg):
        print(msg)

    def tela_funcoes(self, nome = 'professor(a)'):
        print('-----Eldoom-----')
        print(f'Bem vindo {nome}!')
        print()
        print('O que gostaria de fazer?')
        print('1 - Adicionar nota')
        print('2 - Editar nota')
        print('3 - Excluir nota')
        print('4 - Adicionar Frequência')
        print('5 - Editar frequência')
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

        
    
    
    

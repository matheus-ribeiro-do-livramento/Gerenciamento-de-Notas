class TelaProfessor:
    def tela_login(self):
        print('-----Eldoom-----')
        print(     'login      ')
        print()
        print()
        while True:
            try:
                matricula_login = int(input('Matricula: '))
                return matricula_login
            except ValueError:
                print('Opção não correspondida, tente novamente')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário')
                return 0 

    def tela_cadastro(self):
        print('-----Eldoom-----')
        print('   Cadastrar    ')
        print()
        print()
        while True:
            try:
                nome = str(input('Digite seu nome: ')).strip()
                disciplina = str(input('coloque sua disciplina: ')).strip()
                matricula_cadastro = int(input('Coloque a matricula: '))
                return nome, disciplina, matricula_cadastro
            except ValueError:
                print('Opção não correspondida, tente novamente')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário')
                return 0
    
    def mostrar_msg(self, msg):
        print(msg)
    
    
    

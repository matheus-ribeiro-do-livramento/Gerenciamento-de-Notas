import FreeSimpleGUI as sg

class TelaProfessor:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

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
        self.init_opcoes()
        button, values = self.__window.Read()
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['0'] or button in (None,'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    def init_opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Eldoom', font=("Helvica",25))],
            [sg.Text('Você gostaria de ?', font=("Helvica",15))],
            [sg.Radio('Logar',"RD1", key='1')],
            [sg.Radio('Cadastrar',"RD1", key='2')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Sistema de livros').Layout(layout)



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
        print()
        print('-----Eldoom-----')
        print(f'Bem vindo {nome}!')
        print()
        print('Em que categoria gostaria de usar?')
        print('1 - Disciplina')
        print('2 - Vincular a uma disciplina')
        print('3 - Turma')
        print('4 - Aluno')
        print('5 - Nota')
        print('6 - Frequência')
        print('7 - Listar status dos alunos')
        print('0 - Sair')
        print()
        while True:
            try:
                opcao = int(input('Qual opção deseja: '))
                if opcao not in [1, 2, 3, 4, 5, 6, 7, 0]:
                    print('Opção inválida, por favor escolha umas das opções listadas.')
                return opcao
            except ValueError:
                print('Opção não correspondida, tente novamente.')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário.')
                return 0
    
    def tela_opcoes_disciplina(self):
        print()
        print('-----Eldoom-----')
        print()
        print('1 - Adicionar Disciplina')
        print('2 - Editar Disciplina')
        print('3 - Excluir disciplina')
        print('4 - Visualizar Disciplina')
        print('0 - Voltar')
        print()
        while True:
            try:
                opcao = int(input('Qual opção deseja: '))
                if opcao not in [1, 2, 3, 4, 0]:
                    print('Opção inválida, por favor escolha umas das opções listadas.')
                return opcao
            except ValueError:
                print('Opção não correspondida, tente novamente.')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário.')
                return 0
    
    def tela_opcoes_aluno(self):
        print()
        print('-----Eldoom-----')
        print()
        print('1 - Matricular Aluno')
        print('2 - Editar Aluno')
        print('3 - Excluir Aluno')
        print('4 - Visualizar Aluno')
        print('0 - Voltar')
        print()
        while True:
            try:
                opcao = int(input('Qual opção deseja: '))
                if opcao not in [1, 2, 3, 4, 0]:
                    print('Opção inválida, por favor escolha umas das opções listadas.')
                return opcao
            except ValueError:
                print('Opção não correspondida, tente novamente.')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário.')
                return 0
    
    def tela_opcoes_nota(self):
        print()
        print('-----Eldoom-----')
        print()
        print('1 - Adicionar Nota')
        print('2 - Editar Nota')
        print('3 - Excluir nota')
        print('4 - Visualizar Nota')
        print('0 - Voltar')
        print()
        while True:
            try:
                opcao = int(input('Qual opção deseja: '))
                if opcao not in [1, 2, 3, 4, 0]:
                    print('Opção inválida, por favor escolha umas das opções listadas.')
                return opcao
            except ValueError:
                print('Opção não correspondida, tente novamente.')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário.')
                return 0
    
    def tela_opcoes_frequencia(self):
        print()
        print('-----Eldoom-----')
        print()
        print('1 - Adicionar Frequência')
        print('2 - Editar Frequência')
        print('3 - Excluir Frequência')
        print('4 - Visualizar Frequência')
        print('0 - Voltar')
        print()
        while True:
            try:
                opcao = int(input('Qual opção deseja: '))
                if opcao not in [1, 2, 3, 4, 0]:
                    print('Opção inválida, por favor escolha umas das opções listadas.')
                return opcao
            except ValueError:
                print('Opção não correspondida, tente novamente.')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário.')
                return 0
        
    def tela_opcoes_turma(self):
        print()
        print('-----Eldoom-----')
        print()
        print('1 - Adicionar Turma')
        print('2 - Editar Turma')
        print('3 - Excluir Turma')
        print('4 - Visualizar Turma')
        print('0 - Voltar')
        print()
        while True:
            try:
                opcao = int(input('Qual opção deseja: '))
                if opcao not in [1, 2, 3, 4, 0]:
                    print('Opção inválida, por favor escolha umas das opções listadas.')
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

    def close(self):
        self.__window.Close()
    
    
    

import FreeSimpleGUI as sg

class TelaAluno:
    def __init__(self):
        self.__window = None
        self.init_aluno()
    
    def tela_opcoes_aluno(self):
        self.init_aluno()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
            
    def init_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- ELDOOM ----------', font=("Helvica", 25))],
        [sg.Text('Gostaria de:', font=("Helvica", 15))],
        [sg.Radio('Criar Aluno', "RD1", key='1')],
        [sg.Radio('Editar Aluno', "RD1", key='2')],
        [sg.Radio('Excluir Aluno', "RD1", key='3')],
        [sg.Radio('Visualizar Aluno', "RD1", key='4')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

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
                    print("Opção inválida, por favor escolha umas das opções listadas.")
            except ValueError:
                print("Opção incorreta, tente novamente")
            
    def pega_dados_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
      [sg.Text('-------- Dados Aluno ----------', font=("Helvica", 25))],
      [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

        while True:
            button, values = self.open()

            if button in (None, 'Cancelar'):
                self.close()
                return None

            try:
                nome = values['nome']
                matricula = int(values['matricula'])
                if not nome.strip():
                    sg.popup_error('O campo "Nome" não pode ser vazio.')
                else:
                    self.close()
                    return {'nome': nome, 'matricula': matricula}
            except ValueError:
                sg.popup_error('Matrícula inválida! Por favor, digite apenas números.')
    
    def aluno_nao_cadastrado(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('Nenhum aluno cadastrado', font=("Helvica", 15))],
        [sg.Button('Continuar')]
            ]
        self.__window = sg.Window('ELDOOM').Layout(layout)
        button, values = self.open()

        if button in (None, 'Continuar'):
            self.close()
            return None
    
    def mostra_aluno(self, dados_aluno):
        string_todos_amigos = ""
        for dado in dados_aluno:
            string_todos_amigos = string_todos_amigos + "Aluno(a): " + dado["nome"] + '\n'
            string_todos_amigos = string_todos_amigos + "Matricula: " + str(dado["matricula"]) + '\n\n'

        sg.Popup('-------- LISTA DE TURMA ----------', string_todos_amigos)

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
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('Digite a matricula do aluno(a): ', size=(15, 1)), sg.InputText('', key='matricula')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

        while True:
            button, values = self.open()
            
            if button in (None, 'Cancelar'):
                self.close()
                return None

            try:
                matricula = int(values['matricula'])
                self.close()
                return matricula
            except ValueError:
                sg.popup_error('Código inválido! Por favor, digite apenas números.')

    
    def mostrar_msg(self, msg):
        sg.popup(msg)

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
                    print("Opção inválida, por favor escolha umas das opções listadas.")

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
            

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    

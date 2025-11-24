import FreeSimpleGUI as sg

class TelaProfessor:
    def __init__(self):
        self.__window = None
        self.init_opcoes()
        self.init_funcoes()

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
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Eldoom ----------', font=("Helvica", 25))],
        [sg.Text('Login', font=("Helvica", 20))],
        [sg.Text('Matricula:', size=(15, 1)), sg.InputText('', key='matricula')],
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
                sg.popup_error('Matrícula inválida! Por favor, digite apenas números.')

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
        self.__window = sg.Window('ELDOOM').Layout(layout)



    def tela_cadastro(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
      [sg.Text('-------- Cadastro ----------', font=("Helvica", 25))],
      [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
    ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

        while True:
            button, values = self.open()

            if button in (None, 'Cancelar'):
                self.close()
                return None, None

            try:
                nome = values['nome']
                matricula = int(values['matricula'])
                if not nome.strip():
                    sg.popup_error('O campo "Nome" não pode ser vazio.')
                else:
                    self.close()
                    return nome, matricula
            except ValueError:
                sg.popup_error('Matrícula inválida! Por favor, digite apenas números.')
    
    def mostrar_msg(self, msg):
        print(msg)

    def tela_funcoes(self, nome = 'professor(a)'):
        self.init_funcoes()
        button, values = self.open()
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    def init_funcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- ELDOOM ----------', font=("Helvica", 25))],
        [sg.Text('Escolha sua opção', font=("Helvica", 15))],
        [sg.Radio('Disciplina', "RD1", key='1')],
        [sg.Radio('Vincular a uma disciplina', "RD1", key='2')],
        [sg.Radio('Turma', "RD1", key='3')],
        [sg.Radio('Aluno', "RD1", key='4')],
        [sg.Radio('Nota', "RD1", key='5')],
        [sg.Radio('Frequência', "RD1", key='6')],
        [sg.Radio('Listar status alunos', "RD1", key='7')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

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
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    
    

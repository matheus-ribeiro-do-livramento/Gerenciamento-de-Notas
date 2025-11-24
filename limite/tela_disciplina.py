import FreeSimpleGUI as sg

class TelaDisciplina():
    def __init__(self):
        self.__window = None
        self.init_disciplina()

    def tela_opcoes_disciplina(self):
        self.init_disciplina()
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
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
        self.close()
        return opcao
    
    def init_disciplina(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- ELDOOM ----------', font=("Helvica", 25))],
        [sg.Text('Gostaria de:', font=("Helvica", 15))],
        [sg.Radio('Criar Disciplina', "RD1", key='1')],
        [sg.Radio('Editar Disciplina', "RD1", key='2')],
        [sg.Radio('Excluir Disciplina', "RD1", key='3')],
        [sg.Radio('Visualizar Disciplina', "RD1", key='4')],
        [sg.Radio('Matricular Aluno', "RD1", key='5')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

    def pega_dados_aluno(self):
        print("----------Dados do Aluno----------")
        nome = input("Digite o Nome do Aluno: ")
        matricula = input("Digite a Matricula do Aluno: ")

        return {"nome": nome, "matricula": matricula}

    def pega_dados_disciplina(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- DADOS DISCIPLINA ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('Código:', size=(15, 1)), sg.InputText('', key='codigo')],
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
                codigo = int(values['codigo'])
                if not nome.strip():
                    sg.popup_error('O campo "Nome" não pode ser vazio.')
                else:
                    self.close()
                    return {"nome": nome, "codigo": codigo}
            except ValueError:
                sg.popup_error('Código inválido! Por favor, digite apenas números.')
    
    def mostrar_msg(self, msg):
        sg.Popup(msg)

    def mostra_disciplina(self, lista_dados_disciplina):
        string_todos_amigos = ""
        for dado in lista_dados_disciplina:
            string_todos_amigos = string_todos_amigos + "Nome: " + dado["nome"] + '\n'
            string_todos_amigos = string_todos_amigos + "Código: " + str(dado["codigo"]) + '\n\n'

        sg.Popup('-------- LISTA DE DISCIPLINA ----------', string_todos_amigos)

    def seleciona_disciplina(self, disciplinas: list):
        sg.ChangeLookAndFeel('DarkTeal4')

        if not disciplinas:
            self.mostrar_msg("Nenhuma disciplina cadastrada.")
            return None

        display_disciplinas = [f"{d.nome} (Código: {d.codigo})" for d in disciplinas]

        layout = [
            [sg.Text('Selecione a Disciplina', font=("Helvica", 15))],
            [sg.Listbox(values=display_disciplinas, size=(40, 10), key='-DISC-', enable_events=True)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Disciplina').Layout(layout)

        button, values = self.open()
        self.close()

        if button in (None, 'Cancelar'):
            return None

        if values['-DISC-']:
            selected_str = values['-DISC-'][0]
            selected_index = display_disciplinas.index(selected_str)
            return disciplinas[selected_index]
        return None
    def seleciona_matricula_aluno(self):
        matricula = input("Digite a Matricula:")
        return matricula
    
    def disciplina_sem_turma(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('Disciplina sem turma', font=("Helvica", 15))],
        [sg.Button('Continuar')]
            ]
        self.__window = sg.Window('ELDOOM').Layout(layout)
        button, values = self.open()

        if button in (None, 'Continuar'):
            self.close()
            return None
    
    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
    

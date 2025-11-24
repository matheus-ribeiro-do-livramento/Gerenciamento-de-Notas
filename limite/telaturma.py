import FreeSimpleGUI as sg

class TelaTurma:
    def __init__(self):
        self.__window = None
 
    def tela_opcoes_turma(self):
        self.init_turma()
        button, values = self.open()
        if button in (None, "Cancelar"):
            self.close()
            return 0
        
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['3']:
            opcao = 3
        if values['4']:
            opcao = 4
 
        self.close()
        return opcao

    def init_turma(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- ELDOOM ----------', font=("Helvica", 25))],
        [sg.Text('Gostaria de:', font=("Helvica", 15))],
        [sg.Radio('Criar Turma', "RD1", key='1')],
        [sg.Radio('Editar Turma', "RD1", key='2')],
        [sg.Radio('Excluir Turma', "RD1", key='3')],
        [sg.Radio('Visualizar Turma', "RD1", key='4')],
        [sg.Button('Confirmar',bind_return_key=True), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

    def pega_dados_turma(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
      [sg.Text('-------- Cadastro ----------', font=("Helvica", 25))],
      [sg.Text('Sala: ', size=(15, 1)), sg.InputText('', key='sala')],
      [sg.Text('Número da turma: ', size=(15, 1)), sg.InputText('', key='numeroturma')],
      [sg.Text('Semestre: ', size=(15, 1)), sg.InputText('', key='semestre')],
      [sg.Button('Confirmar',bind_return_key=True), sg.Cancel('Cancelar')]
    ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

        while True:
            button, values = self.open()

            if button in (None, 'Cancelar'):
                self.close()
                return None

            try:
                sala = values['sala']
                numero_turma = int(values['numeroturma'])
                semestre = int(values['semestre'])

                if not sala.strip():
                    sg.popup_error('O campo "Sala" não pode ser vazio.')
                else:
                    self.close()
                    return {'sala': sala, 'numeroturma': numero_turma, 'semestre': semestre}
            except ValueError:
                sg.popup_error('Valor inválido! Por favor, digite apenas números.')

    def mostrar_msg(self, msg: str):
        sg.popup(msg)

    def seleciona_turma(self, turmas: list):
        sg.ChangeLookAndFeel('DarkTeal4')


        display_turmas = [f"Turma {t.numero} ({t.semestre}) - Sala: {t.sala}" for t in turmas]

        layout = [
            [sg.Text('Selecione a Turma', font=("Helvica", 15))],
            [sg.Listbox(values=display_turmas, size=(40, 10), key='-TURMA-', enable_events=True)],
            [sg.Button('Confirmar',bind_return_key=True), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Turma').Layout(layout)

        button, values = self.open()
        self.close()

        if button in (None, 'Cancelar'):
            return None

        if values['-TURMA-']:
            selected_str = values['-TURMA-'][0]
            selected_index = display_turmas.index(selected_str)
            return turmas[selected_index]
        return None
            
    def mostra_turma(self, lista_dados_turma):
        string_todos_amigos = ""
        for dado in lista_dados_turma:
            string_todos_amigos = string_todos_amigos + "Sala: " + dado["sala"] + '\n'
            string_todos_amigos = string_todos_amigos + "Número da turma: " + str(dado["numeroturma"]) + '\n'
            string_todos_amigos = string_todos_amigos + "Semestre: " + str(dado["semestre"]) + '\n\n'

        sg.Popup('-------- LISTA DE TURMA ----------', string_todos_amigos)
    
    def turma_nao_cadastrada(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('Nenhuma turma cadastrada', font=("Helvica", 15))],
        [sg.Button('Continuar',bind_return_key=True)]
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
    
  
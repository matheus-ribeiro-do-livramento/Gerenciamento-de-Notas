import FreeSimpleGUI as sg

class TelaProfessor:
    def __init__(self):
        self.__window = None

    def mostrar_msg(self, msg: str):
        sg.popup(msg)
        
    def pegar_codigo_disciplina(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('-------- Vincular Disciplina ----------', font=("Helvica", 25))],
            [sg.Text('Digite o código da disciplina:', size=(20, 1)), sg.InputText('', key='codigo')],
            [sg.Button('Confirmar', bind_return_key=True), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

        while True:
            button, values = self.open()
            
            if button in (None, 'Cancelar'):
                self.close()
                return None

            try:
                codigo = int(values['codigo'])
                self.close()
                return codigo
            except ValueError:
                sg.popup_error('Código inválido! Por favor, digite apenas números.')
                
    def tela_login(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Eldoom ----------', font=("Helvica", 25))],
        [sg.Text('Login', font=("Helvica", 20))],
        [sg.Text('Matricula:', size=(15, 1)), sg.InputText('', key='matricula')],
        [sg.Button('Confirmar', bind_return_key=True), sg.Cancel('Cancelar')]
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
            [sg.Button('Confirmar',bind_return_key=True), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)



    def tela_cadastro(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
      [sg.Text('-------- Cadastro ----------', font=("Helvica", 25))],
      [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
      [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula')],
      [sg.Button('Confirmar',bind_return_key=True), sg.Cancel('Cancelar')]
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
    
    def tela_funcoes(self, nome = 'professor(a)'):
        self.init_funcoes()
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
        if values['5']:
            opcao = 5
        if values['6']:
            opcao = 6
        if values['7']:
            opcao = 7
            
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
        [sg.Button('Confirmar',bind_return_key=True), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

    def mostra_status_alunos(self, dados_alunos: list):
        titulo = "Status dos Alunos"
        if not dados_alunos:
            sg.Popup(titulo, "Nenhum aluno para exibir.")
            return
        
        texto_completo = []
        for dados in dados_alunos:
            texto_completo.append(f"Disciplina: {dados['disciplina']}")
            texto_completo.append(f"  Aluno: {dados['nome']} (Matrícula: {dados['matricula']})")

            notas_str = "Nenhuma nota lançada"
            if dados['notas']:
                notas_str = ", ".join([f"{n:.2f}" for n in dados['notas']])
            texto_completo.append(f"  Notas: [{notas_str}]")

            media_str = f"{dados['media']:.2f}" if dados['media'] is not None else "Não calculada"
            texto_completo.append(f"  Média: {media_str}")

            frequencia_str = f"{dados['frequencia']:.2f}%" if dados['frequencia'] is not None else "Não registrada"
            texto_completo.append(f"  Frequência: {frequencia_str}")
            texto_completo.append("-" * 30)

        texto_final = "\n".join(texto_completo)
        sg.PopupScrolled(titulo, texto_final, size=(60, 25))

    def close(self):
        self.__window.Close()
    
    def open(self):
        button, values = self.__window.Read()
        return button, values
    
    
    

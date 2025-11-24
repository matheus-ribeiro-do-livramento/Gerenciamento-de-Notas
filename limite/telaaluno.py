import FreeSimpleGUI as sg

class TelaAluno:
    def __init__(self):
        self.__window = None

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
        [sg.Button('Confirmar',bind_return_key=True), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

    def tela_opcoes_login_cadastro(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [[sg.Text('Eldoom',font=("Helvica", 25))],
                  [sg.Text('Você Gostaria de ?:', font=("Helvica",25))],
                  [sg.Radio('Logar',"RD1", key='1')],
                  [sg.Radio('Cadastrar',"RD1", key='2')],
                  [sg.Radio('Finalizar sistema',"RD1", key='0')],
                  [sg.Button('Confirmar',bind_return_key=True), sg.Cancel('Cancelar')]
                  ]
        
        self.__window = sg.Window("Eldoom").Layout(layout)

        button, values = self.open()
        if button is (None, "Cancelar"):
            self.close()
            return 0
        
        opcao = 0
        if values['1']:
            opcao = 1
        if values['2']:
            opcao = 2
        if values['0'] or button in (None, 'Cancelar'):
            opcao = 0
            
        self.close()
        return opcao
                    
    def pega_dados_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Dados Aluno ----------', font=("Helvica", 25))],
        [sg.Text('Nome:', size=(15, 1)), sg.InputText('', key='nome')],
        [sg.Text('Matricula', size=(15, 1)), sg.InputText('', key='matricula')],
        [sg.Button('Confirmar',bind_return_key=True), sg.Cancel('Cancelar')]]

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
        [sg.Button('Continuar',bind_return_key=True)]
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
        if not dados_disciplina:
            sg.popup("Você não está matriculado a nenhuma disciplina")
            return

        texto_display = "----- Suas Disciplinas -----\n\n"
        for disciplina in dados_disciplina:
            texto_display += f"Nome: {disciplina['nome']}| Codigo: {disciplina['codigo']}\n"

        sg.popup_scrolled(texto_display, title="Disciplinas", size=(50,10))

    def mostra_frequencia(self, resultados: list):
        if not resultados:
            self.mostrar_msg("Aviso","Não foi possível calcular sua frequência em nenhuma disciplina.")
            return

        texto_display = '----- Sua Frequência -----\n\n'
        for item in resultados:
            percentual = item['percentual']
            if percentual is not None:
                texto_display +=f"{item['disciplina']}: {percentual:.2f}% de presença\n"
            else:
                texto_display +=(f"{item['disciplina']}: Nenhuma frequência registrada ainda.")
        
        sg.popup_scrolled(texto_display, title="Frequência", size=(50,10))
    
    def mostra_boletim(self, boletim_data: list):
        if not boletim_data:
            self.mostrar_msg("Nenhum dado de boletim disponível.")
            return

        texto_display = "----- Boletim -----\n\n"
        for item in boletim_data:
            texto_display +=f"\nDisciplina: {item['nome_disciplina']} (Código: {item['codigo_disciplina']})\n"
            texto_display +=f"  Professor(a): {item['professor_nome']}\n"
            
            if item['notas']:
                notas_str = ", ".join([f"{n:.2f}" for n in item['notas']])
                texto_display +=f"  Notas: [{notas_str}]\n"
            else:
                texto_display += "  Notas: Nenhuma nota lançada.\n"
            
            if item['media'] is not None:
                texto_display +=f"  Média: {item['media']:.2f}\n"
            else:
                texto_display+= "  Média: Não calculada (sem notas).\n"
            
            if item['frequencia'] is not None:
                texto_display +=f"  Frequência: {item['frequencia']:.2f}%\n"
            else:
                texto_display +="  Frequência: Não disponível.\n"
        
        sg.popup_scrolled(texto_display, title="Boletim", size=(50,10))

    def seleciona_aluno(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('Digite a matricula do aluno(a): ', size=(15, 1)), sg.InputText('', key='matricula')],
        [sg.Button('Confirmar',bind_return_key=True), sg.Cancel('Cancelar')]
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
        sg.popup("Aviso", msg)

    def tela_login(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- Eldoom ----------', font=("Helvica", 25))],
        [sg.Text('Login', font=("Helvica", 20))],
        [sg.Text('Matricula:', size=(15, 1)), sg.InputText('', key='matricula')],
        [sg.Button('Confirmar',bind_return_key=True), sg.Cancel('Cancelar')]
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
    
    def tela_funcoes_aluno_logado(self, nome_aluno):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text(f'----- Bem Vindo (a), {nome_aluno} -------', font=("Helvica", 25))],
        [sg.Radio('Ver Minhas Notas', "RD1", key='1')],
        [sg.Radio('Listar Minhas Disciplinas', "RD1", key='2')],
        [sg.Radio('Ver Minha Frequência', "RD1", key='3')],
        [sg.Radio('Ver Meu Boletim', "RD1", key='4')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar', bind_return_key=True), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

        button, values = self.open()
        if button in (None, "Cancelar"):
            self.close()
            return 0

        opcao = 0
        if values['1']: opcao = 1
        if values['2']: opcao = 2
        if values['3']: opcao = 3
        if values['4']: opcao = 4
        if values['0'] or button in (None, 'Cancelar'): opcao = 0
        
        self.close()
        return opcao
        
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
            

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    

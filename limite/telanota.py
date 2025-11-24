import FreeSimpleGUI as sg

class TelaNota:
    def __init__(self):
        self.__window = None
        self.init_nota()

    def tela_opcoes_nota(self):
        self.init_nota()
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
    
    def init_nota(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- ELDOOM ----------', font=("Helvica", 25))],
        [sg.Text('Gostaria de:', font=("Helvica", 15))],
        [sg.Radio('Criar Nota', "RD1", key='1')],
        [sg.Radio('Editar Nota', "RD1", key='2')],
        [sg.Radio('Excluir Nota', "RD1", key='3')],
        [sg.Radio('Visualizar Nota', "RD1", key='4')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

    def mostrar_mensagem(self, mensagem: str):
        sg.Popup(mensagem)

    def pegar_codigo_disciplina(self):
        while True:
            try:
                codigo = input("Digite o código da disciplina: ")
                if codigo.strip() == "":
                    self.mostrar_mensagem("Código não pode ser vazio!")
                    continue
                return codigo
            except ValueError:
                self.mostrar_mensagem("Valor inválido para código!")

    def selecionar_aluno(self, alunos: list):
        if not alunos:
            self.mostrar_mensagem("Não há alunos matriculados nesta turma!")
            return None
        
        sg.ChangeLookAndFeel('DarkTeal4')

        display_alunos = [f"{aluno.nome} (Matrícula: {aluno.matricula})" for aluno in alunos]

        layout = [
            [sg.Text('Selecione o Aluno', font=("Helvica", 15))],
            [sg.Listbox(values=display_alunos, size=(40, 10), key='-ALUNO-', enable_events=True)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Aluno').Layout(layout)

        button, values = self.open()
        self.close()

        if button in (None, 'Cancelar'):
            return None

        if values['-ALUNO-']:
            selected_str = values['-ALUNO-'][0]
            selected_index = display_alunos.index(selected_str)
            return alunos[selected_index]
        return None
    
    def quantidade_nota(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Quantas notas deseja lançar?', font=("Helvica", 15))],
            [sg.Text('Quantidade:', size=(15, 1)), sg.InputText('', key='-QTD-')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Quantidade de Notas').Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            try:
                quantidade = int(values['-QTD-'])
                if quantidade > 0:
                    self.close()
                    return quantidade
                else:
                    sg.popup_error('A quantidade deve ser um número maior que zero.')
            except ValueError:
                sg.popup_error('Valor inválido! Por favor, digite um número inteiro.')
    
    def nota(self, numero_nota: int):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text(f'Digite o valor da {numero_nota}ª nota:', font=("Helvica", 15))],
            [sg.Text('Valor:', size=(15, 1)), sg.InputText('', key='-NOTA-')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Lançar Nota').Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None
            try:
                nota_str = values['-NOTA-'].replace(',', '.')
                nota_float = float(nota_str)
                if 0 <= nota_float <= 10:
                    self.close()
                    return nota_float
                else:
                    sg.popup_error("A nota deve estar entre 0 e 10!")
            except ValueError:
                sg.popup_error("Valor inválido! Por favor, digite um número.")
                
    def seleciona_nota_para_editar(self, notas: list):
        if not notas:
            self.mostrar_mensagem("Não há notas para editar.")
            return None

        sg.ChangeLookAndFeel('DarkTeal4')

        display_notas = [f"{i+1}ª Nota: {nota.valor:.2f}" for i, nota in enumerate(notas)]

        layout = [
            [sg.Text('Selecione a nota para editar', font=("Helvica", 15))],
            [sg.Listbox(values=display_notas, size=(40, 10), key='-NOTA-', enable_events=True)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Editar Nota').Layout(layout)

        button, values = self.open()
        self.close()

        if button in (None, 'Cancelar') or not values['-NOTA-']:
            return None

        return display_notas.index(values['-NOTA-'][0])

    def mostra_notas_aluno(self, notas: list, nome_aluno: str = None):
        titulo = "--- Notas ---"
        if nome_aluno:
            titulo = f"--- Notas de {nome_aluno} ---"

        if notas:
            media = sum(notas) / len(notas)
            notas_formatadas = "\n".join([f"  • {i}ª Nota: {nota:.2f}" for i, nota in enumerate(notas, 1)])
            texto_final = f"{notas_formatadas}\n\n--- Média ---\n  • Média Final: {media:.2f}"

            sg.Popup(titulo, texto_final)
        else:
            self.mostrar_mensagem("\nNenhuma nota lançada para este aluno.")

    def pega_novo_valor_nota(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Digite o novo valor da nota', font=("Helvica", 15))],
            [sg.Text('Novo Valor:', size=(15, 1)), sg.InputText('', key='-NOVO_VALOR-')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Alterar Valor da Nota').Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None
            
            try:
                nota_str = values['-NOVO_VALOR-'].replace(',', '.')
                nota_float = float(nota_str)
                if 0 <= nota_float <= 10:
                    self.close()
                    return nota_float
                else:
                    sg.popup_error("A nota deve estar entre 0 e 10!")
            except ValueError:
                sg.popup_error("Valor inválido! Por favor, digite um número válido.")

    def seleciona_nota_para_excluir(self, notas: list):
        if not notas:
            self.mostrar_mensagem("Não há notas para excluir.")
            return None

        sg.ChangeLookAndFeel('DarkTeal4')

        display_notas = [f"{i+1}ª Nota: {nota.valor:.2f}" for i, nota in enumerate(notas)]

        layout = [
            [sg.Text('Selecione a nota para EXCLUIR', font=("Helvica", 15))],
            [sg.Listbox(values=display_notas, size=(40, 10), key='-NOTA-', enable_events=True)],
            [sg.Button('Confirmar Exclusão', button_color=('white', 'red')), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Excluir Nota').Layout(layout)

        button, values = self.open()
        self.close()

        if button in (None, 'Cancelar') or not values['-NOTA-']:
            return None

        return display_notas.index(values['-NOTA-'][0])
    
    def disciplina_nao_selecionada(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('Nenhuma disciplina foi selecionada.', font=("Helvica", 15))],
        [sg.Button('Continuar')]
            ]
        self.__window = sg.Window('ELDOOM').Layout(layout)
        button, values = self.open()

        if button in (None, 'Continuar'):
            self.close()
            return None
    
    def nenhum_aluno_matriculado(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('Nenhum aluno matriculado na turma.', font=("Helvica", 15))],
        [sg.Button('Continuar')]
            ]
        self.__window = sg.Window('ELDOOM').Layout(layout)
        button, values = self.open()

        if button in (None, 'Continuar'):
            self.close()
            return None

    def aluno_sem_nota(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('Aluno sem nota', font=("Helvica", 15))],
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

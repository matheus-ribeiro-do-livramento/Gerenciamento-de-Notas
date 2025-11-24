import datetime
import FreeSimpleGUI as sg

class TelaFrequencia:
    def __init__(self):
        self.__window = None
        self.init_frequencia()

    def tela_opcoes_frequencia(self):
        self.init_frequencia()
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
    
    def init_frequencia(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
        [sg.Text('-------- ELDOOM ----------', font=("Helvica", 25))],
        [sg.Text('Gostaria de:', font=("Helvica", 15))],
        [sg.Radio('Criar Frequência', "RD1", key='1')],
        [sg.Radio('Editar Frequência', "RD1", key='2')],
        [sg.Radio('Excluir Frequência', "RD1", key='3')],
        [sg.Radio('Visualizar Frequência', "RD1", key='4')],
        [sg.Radio('Retornar', "RD1", key='0')],
        [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)

    def mostrar_msg(self, msg: str):
        sg.Popup(msg)

    def pegar_data(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Lançamento de Frequência', font=("Helvica", 15))],
            [sg.Text('Data da aula (DD/MM/AAAA):', size=(25, 1)), sg.InputText('', key='-DATA-')],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Lançar Frequência').Layout(layout)

        while True:
            button, values = self.open()
            if button in (None, 'Cancelar'):
                self.close()
                return None

            data_str = values['-DATA-']
            try:
                datetime.datetime.strptime(data_str, '%d/%m/%Y')
                self.close()
                return data_str
            except ValueError:
                sg.popup_error("Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")

    def pegar_frequencia_aluno(self, nome_aluno: str):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text(f'Defina a frequência para {nome_aluno}:', font=("Helvica", 15))],
            [sg.Button('Presente', key='P', size=(10, 2)), sg.Button('Falta', key='F', size=(10, 2))],
            [sg.Cancel('Cancelar Lançamento', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Lançar Frequência', layout, element_justification='c')

        button, values = self.open()
        self.close()

        if button in ('P', 'F'):
            return button
        
        return None

    def mostrar_resumo_frequencia(self, data: str, resumo: dict):
        titulo = f"Resumo da Frequência - {data}"
        
        if not resumo:
            texto_resumo = "Nenhum aluno para exibir no resumo."
        else:
            linhas_resumo = [f"  • {nome}: {'Presente' if status == 'P' else 'Falta'}" for nome, status in resumo.items()]
            texto_resumo = "\n".join(linhas_resumo)
        sg.Popup(titulo, texto_resumo)

    def seleciona_data(self, datas: list):
        if not datas:
            self.mostrar_msg("Não há datas com frequência registrada para selecionar.")
            return None

        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [
            [sg.Text('Selecione a Data', font=("Helvica", 15))],
            [sg.Listbox(values=datas, size=(40, 10), key='-DATA-', enable_events=True)],
            [sg.Button('Confirmar'), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('Selecionar Data').Layout(layout)

        button, values = self.open()
        self.close()

        if button in (None, 'Cancelar') or not values['-DATA-']:
            return None

        return values['-DATA-'][0]

    def seleciona_aluno(self, alunos: list):
        if not alunos:
            self.mostrar_msg("Não há alunos nesta turma para selecionar.")
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

        if button in (None, 'Cancelar') or not values['-ALUNO-']:
            return None

        selected_index = display_alunos.index(values['-ALUNO-'][0])
        return alunos[selected_index]

    def pega_nova_frequencia(self, nome_aluno: str, status_atual: str):
        status_texto = 'Presente' if status_atual == 'P' else 'Falta'
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text(f'Editar frequência para {nome_aluno}', font=("Helvica", 15))],
            [sg.Text(f'Status atual: {status_texto}', font=("Helvica", 12))],
            [sg.Text('Selecione o novo status:', pad=((0,0), (10,5)))],
            [sg.Button('Presente', key='P', size=(10, 2)), sg.Button('Falta', key='F', size=(10, 2))],
            [sg.Cancel('Cancelar', button_color=('white', 'red'))]
        ]
        self.__window = sg.Window('Editar Frequência', layout, element_justification='c')

        button, values = self.open()
        self.close()

        if button in ('P', 'F'):
            return button

        return None

    def confirma_exclusao(self, nome_aluno: str, data: str) -> bool:
        print(f"\nTem certeza que deseja excluir a frequência de {nome_aluno} para a data {data}?")
        while True:
            resposta = input("Confirmar (S/N): ").upper().strip()
            if resposta == 'S':
                return True
            if resposta == 'N':
                self.mostrar_msg("Exclusão cancelada.")
                return False
            self.mostrar_msg("Opção inválida. Digite 'S' para Sim ou 'N' para Não.")

    def mostra_frequencia_turma(self, nome_disciplina: str, numero_turma: int, historico: dict, mapa_nomes: dict):
        titulo = f"Frequência da Turma {numero_turma} ({nome_disciplina})"
        
        if not historico:
            texto_final = "Nenhuma frequência lançada para esta turma."
        else:
            texto_completo = []
            for data, lista_presenca in historico.items():
                texto_completo.append(f"\n--- Data: {data} ---")
                if not lista_presenca:
                    texto_completo.append("  Nenhum registro de aluno para esta data.")
                    continue
                for matricula, status in lista_presenca.items():
                    nome_aluno = mapa_nomes.get(matricula, f"Matrícula {matricula}")
                    status_texto = 'Presente' if status == 'P' else 'Falta'
                    texto_completo.append(f"  • {nome_aluno}: {status_texto}")
            texto_final = "\n".join(texto_completo)

        sg.PopupScrolled(titulo, texto_final, size=(50, 20))

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
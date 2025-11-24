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
        print(msg)

    def pegar_data(self):
        print("\n--- Lançamento de Frequência ---")
        while True:
            data_str = input("Digite a data da aula (DD/MM/AAAA): ").strip()
            try:
                datetime.datetime.strptime(data_str, '%d/%m/%Y')
                return data_str 
            except ValueError:
                self.mostrar_msg("Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")
            except KeyboardInterrupt:
                self.mostrar_msg("\nOperação cancelada.")
                return None

    def pegar_frequencia_aluno(self, nome_aluno: str):
        while True:
            status = input(f"Frequência para {nome_aluno} (P - Presente / F - Falta): ").upper().strip()
            if status in ['P', 'F']:
                return status
            self.mostrar_msg("Opção inválida. Digite 'P' para Presente ou 'F' para Falta.")

    def mostrar_resumo_frequencia(self, data: str, resumo: dict):
        print(f"\n--- Resumo da Frequência - {data} ---")
        for nome, status in resumo.items():
            print(f"{nome}: {'Presente' if status == 'P' else 'Falta'}")
        print("-" * 30)

    def seleciona_data(self, datas: list):
        print("\n--- Selecione a Data para Editar ---")
        for i, data in enumerate(datas, 1):
            print(f"[{i}] - {data}")
        
        while True:
            try:
                opcao = int(input("Escolha o número da data: "))
                if 1 <= opcao <= len(datas):
                    return datas[opcao - 1]
                self.mostrar_msg("Opção inválida.")
            except ValueError:
                self.mostrar_msg("Por favor, digite um número.")
            except KeyboardInterrupt:
                self.mostrar_msg("\nOperação cancelada.")
                return None

    def seleciona_aluno(self, alunos: list):
        print("\n--- Selecione o Aluno para Editar a Frequência ---")
        for i, aluno in enumerate(alunos, 1):
            print(f"[{i}] - {aluno.nome} (Matrícula: {aluno.matricula})")
        
        while True:
            try:
                opcao = int(input("Escolha o número do aluno: "))
                if 1 <= opcao <= len(alunos):
                    return alunos[opcao - 1]
                self.mostrar_msg("Opção inválida.")
            except ValueError:
                self.mostrar_msg("Por favor, digite um número.")
            except KeyboardInterrupt:
                self.mostrar_msg("\nOperação cancelada.")
                return None

    def pega_nova_frequencia(self, nome_aluno: str, status_atual: str):
        print(f"\nO status atual de {nome_aluno} é: {'Presente' if status_atual == 'P' else 'Falta'}")
        return self.pegar_frequencia_aluno(nome_aluno)

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

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values
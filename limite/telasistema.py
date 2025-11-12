import FreeSimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_opcoes()

    def tela_opcoes(self):
        print('----- Eldoom -----')
        print('você é?')
        print('1 - Professor')
        print('2 - Aluno')
        print('0 - Finalizar sistema')
        while True:
            try:
                op = int(input('Escolha uma opção: '))
                if op in (0, 1, 2):
                    return op
            except ValueError:
                print('Opção não correspondida, tente novamente')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário')
                return 0 
    def opcoes(self):
        sg.ChangeLookAndFeel('DarkTeal4')

        layout = [

      [sg.Text('-------- Sistema ----------', font=("Arial", 25))],
      [sg.Text('Escolha sua opção', font=("Arial", 15))],
      [sg.Radio('Login Profesor', "RD1", key='1')],
      [sg.Radio('Login Aluno', "RD1", key='2')],
      [sg.Radio('Sair', "RD1", key='3')],
      [sg.Button('Confirmar'), sg.Cancel('Cancelar')]

        ]
        self.__window = sg.Window('Sistema Eldoom').Layout(layout)



    def mostrar_msg(self, msg):
        print(msg)
            
        
            
      
import FreeSimpleGUI as sg

class TelaSistema:
    def __init__(self):
        self.__window = None
        self.init_components()


    def tela_opcoes(self):
        self.init_components()
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
    
    def close(self):
        self.__window.Close()

    
    def init_components(self):
        sg.ChangeLookAndFeel('DarkTeal4')
        layout = [
            [sg.Text('Bem vindo ao Eldoom', font=("Helvica",25))],
            [sg.Text('Você é ?', font=("Helvica",15))],
            [sg.Radio('Professor',"RD1", key='1')],
            [sg.Radio('Aluno',"RD1", key='2')],
            [sg.Radio('Finalizar sistema',"RD1", key='0')],
            [sg.Button('Confirmar', bind_return_key=True), sg.Cancel('Cancelar')]
        ]
        self.__window = sg.Window('ELDOOM').Layout(layout)
    
    def mostrar_msg(self, msg):
        print(msg)
            
        
            
      
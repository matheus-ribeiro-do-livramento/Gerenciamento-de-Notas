class TelaSistema:
    def tela_opcoes(self):
        print('----- Eldoom -----')
        print('você é?')
        print('1 - Professor')
        print('2 - Aluno')
        print('0 - Finalizar sistema')
        while True:
            try:
                op = (input('Escolha uma opção: ')).strip()
                opcao = int(op)
                if opcao in (0, 1, 2):
                    return opcao
            except ValueError:
                print('Opção não correspondida, tente novamente')
            except KeyboardInterrupt:
                print('Execução interrompida pelo usuário')
                return 0 
    
    def mostrar_msg(self, msg):
        print(msg)
            
        
            
      
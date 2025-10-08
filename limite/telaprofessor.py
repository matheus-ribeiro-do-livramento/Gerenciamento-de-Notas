class TelaProfessor:
    def tela_login(self):
        print('-----Eldoom-----')
        print(     'login      ')
        print()
        print()
        matricula_login = int(input('Matricula: '))
        senha_login = input('Senha: ').strip()
        return {'matricula': matricula_login, 'senha': senha_login}

    def tela_cadastro(self):
        print('-----Eldoom-----')
        print('   Cadastrar    ')
        print()
        print()
        matricula_cadastro = int(input('Coloque a matricula: '))
        print('''A senha deve conter:
Minimo 8 caracteres;
1 letra maiúscula;
1 letra;
1 número;
1 simbolo.''')
        senha_cadastro = str(input('Coloque a senha: ')).strip()
        return {'matricula': matricula_cadastro, 'senha':  senha_cadastro}
    
    
    

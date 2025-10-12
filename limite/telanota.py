class TelaNota:
    """ def cadastrar_nota(self):
        while True:
            try:
                quantidade = int(input('Serão quantas notas? '))
                break
            except ValueError:
                print('Valor não interpretado, tente novamente.')
        while True:
            for nota in range(1, quantidade + 1):
                try:
                    notas = str(input(f'{nota}º Nota: '))
                    notas_atualizada = notas.replace(',', '.')
                    notas_float = float(notas_atualizada)
                except ValueError:
                    print('Valor não interpretado, tente novamente.')
            return notas_float """
    
    def cadastrar_nota(self):
        cont = 1
        while True:
            try:
                quantidade = int(input('Serão quantas notas? '))
                break
            except ValueError:
                print('Valor não interpretado, tente novamente.')
        while True:
            try:
                notas = str(input(f'{cont}º Nota: '))
                notas_atualizada = notas.replace(',', '.')
                notas_float = float(notas_atualizada)
                
                if cont == quantidade:
                    break
                cont += 1
            except ValueError:
                print('Valor não interpretado, tente novamente.')
        return notas_float
    

        



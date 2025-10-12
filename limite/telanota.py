class TelaNota:
    def mostrar_mensagem(self, mensagem: str):
        print(mensagem)

    def pegar_matricula(self):
        while True:
            try:
                matricula = input("Digite a matrícula do aluno: ")
                if matricula.strip() == "":
                    self.mostrar_mensagem("Matrícula não pode ser vazia!")
                    continue
                return matricula
            except ValueError:
                self.mostrar_mensagem("Valor inválido para matrícula!")
    
    def quantidade_nota(self):
        while True:
            try:
                quantidade = int(input('Quantidade de notas: '))
                if quantidade <= 0:
                    self.mostrar_mensagem("A quantidade deve ser maior que zero!")
                    continue
                return quantidade
            except ValueError:
                self.mostrar_mensagem("Por favor digite um número inteiro!")
    
    def nota(self, numero_nota: int):
        while True:
            try:
                nota_str = input(f'{numero_nota}ª Nota: ')
                nota_str = nota_str.replace(',', '.')
                nota_float = float(nota_str)
                
                if 0 <= nota_float <= 10:
                    return nota_float
                else:
                    self.mostrar_mensagem("A nota deve estar entre 0 e 10!")
            except ValueError:
                self.mostrar_mensagem("Por favor digite um número válido!")
    

        



class TelaNota:
    def mostrar_mensagem(self, mensagem: str):
        print(mensagem)

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
            self.mostrar_mensagem("Não há alunos matriculados nesta disciplina!")
            return None
            
        self.mostrar_mensagem("\nAlunos matriculados:")
        for i, aluno in enumerate(alunos, 1):
            self.mostrar_mensagem(f"{i}. {aluno.nome} (Matrícula: {aluno.matricula})")
        
        while True:
            try:
                opcao = int(input("\nSelecione o número do aluno: "))
                if 1 <= opcao <= len(alunos):
                    return alunos[opcao - 1]
                else:
                    self.mostrar_mensagem("Opção inválida!")
            except ValueError:
                self.mostrar_mensagem("Por favor digite um número!")
    
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
    
    def seleciona_nota_para_editar(self, notas: list):
        self.mostrar_mensagem("\nQual nota você deseja editar?")
        while True:
            try:
                opcao = int(input("Selecione o número da nota: "))
                if 1 <= opcao <= len(notas):
                    return opcao - 1  # Retorna o índice da lista
                else:
                    self.mostrar_mensagem("Opção inválida!")
            except ValueError:
                self.mostrar_mensagem("Por favor, digite um número.")
            except KeyboardInterrupt:
                self.mostrar_mensagem("\nOperação cancelada.")
                return None

    def pega_novo_valor_nota(self):
        while True:
            try:
                nota_str = input('Digite o novo valor da nota: ').replace(',', '.')
                nota_float = float(nota_str)
                if 0 <= nota_float <= 10:
                    return nota_float
                else:
                    self.mostrar_mensagem("A nota deve estar entre 0 e 10!")
            except ValueError:
                self.mostrar_mensagem("Por favor, digite um número válido!")

    def seleciona_nota_para_excluir(self, notas: list):
        self.mostrar_mensagem("\nQual nota você deseja excluir?")
        while True:
            try:
                opcao = int(input("Selecione o número da nota: "))
                if 1 <= opcao <= len(notas):
                    return opcao - 1  # Retorna o índice da lista
                else:
                    self.mostrar_mensagem("Opção inválida!")
            except ValueError:
                self.mostrar_mensagem("Por favor, digite um número.")
            except KeyboardInterrupt:
                self.mostrar_mensagem("\nOperação cancelada.")
                return None
        

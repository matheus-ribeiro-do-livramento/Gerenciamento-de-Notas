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
    def seleciona_nota_para_editar(self, total_de_notas: int):
        """Pergunta qual nota o usuário deseja alterar. Retorna o índice da nota."""
        try:
            print("Qual nota você deseja alterar? (Digite 0 para cancelar)")
            indice = int(input("Número da nota: "))

            if indice == 0:
                return None
            
            if 1 <= indice <= total_de_notas:
                return indice - 1 
            else:
                self.mostrar_mensagem("Número da nota inválido.")
                return None

        except ValueError:
            self.mostrar_mensagem("Entrada inválida. Operação cancelada.")
            return None

    def mostra_notas_aluno(self, notas: list | None):
        """
        Exibe a lista de notas de forma simples para a visualização do aluno.
        """
        if notas:
            print("\n--- Suas Notas ---")
            for nota in notas:
                print(f"  - Nota: {nota}")
        else:
            self.mostrar_mensagem("\nVocê ainda não possui notas lançadas.")
        input("\nPressione ENTER para continuar...")
        
    def mostrar_mensagem(self, msg: str):
        print(msg)


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
        self.mostrar_mensagem("\nQual nota você deseja excluir? (Digite 0 para cancelar)")
        while True:
            try:
                opcao = int(input("Selecione o número da nota: "))
                if 1 <= opcao <= len(notas):
                    return opcao - 1 
                else:
                    self.mostrar_mensagem("Opção inválida!")
                if opcao == 0:
                    return None
            except ValueError:
                self.mostrar_mensagem("Por favor, digite um número.")
            except KeyboardInterrupt:
                self.mostrar_mensagem("\nOperação cancelada.")
                return None
        

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
    def seleciona_nota_para_editar(self, total_de_notas: int):
        try:
            print("Qual nota você deseja alterar? (Digite 0 para cancelar)")
            indice = int(input("Número da nota: "))

            if indice == 0:
                self.mostrar_mensagem("Operação cancelada.")
                return None
            
            if 1 <= indice <= total_de_notas:
                novo_valor = float(input(f"Digite o novo valor para a {indice}ª nota: "))
                return (indice, novo_valor)
            else:
                self.mostrar_mensagem("Número da nota inválido.")
                return None

        except ValueError:
            self.mostrar_mensagem("Entrada inválida. Operação cancelada.")
            return None

    def seleciona_nota_para_excluir(self, total_de_notas: int) -> int | None:
        """
        Pergunta qual nota o usuário deseja excluir.
        Retorna o índice da nota a ser removida.
        """
        try:
            print("Qual nota você deseja excluir? (Digite 0 para cancelar)")
            indice = int(input("Número da nota: "))

            if indice == 0:
                self.mostrar_mensagem("Operação cancelada.")
                return None
            
            if 1 <= indice <= total_de_notas:
                return indice
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
                # Se 'nota' for apenas um número (float/int)
                print(f"  - Nota: {nota}")
                # Se 'nota' for uma tupla (ex: ('Prova 1', 8.5)), você faria:
                # print(f"  - {nota[0]}: {nota[1]}")
        else:
            self.mostrar_mensagem("\nVocê ainda não possui notas lançadas.")
        
        # Pausa para o usuário poder ler as notas antes de voltar ao menu
        input("\nPressione ENTER para continuar...")
        
    def mostrar_mensagem(self, msg: str):
        """
        Método genérico para exibir qualquer mensagem para o usuário.
        """
        print(msg)


        



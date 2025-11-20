class TelaTurma:
    def pega_dados_turma(self):
        print("\n--- Nova Turma ---")
        while True:
            try:
                sala = input("Sala: ").strip()
                numero = int(input("Número da Turma: "))
                semestre = input("Semestre: ").strip()
                if sala and semestre:
                    return {"sala": sala, "numero": numero, "semestre": semestre}
                print("Sala e semestre não podem ser vazios.")
            except ValueError:
                print("Número da turma deve ser um inteiro.")
            except KeyboardInterrupt:
                print("\nOperação cancelada.")
                return None

    def mostrar_msg(self, msg: str):
        print(msg)

    def seleciona_turma(self, turmas: list):
        print("\n--- Selecione a Turma ---")
        for i, turma in enumerate(turmas, 1):
            print(f"[{i}] - Turma {turma.numero} ({turma.semestre}) - Sala: {turma.sala}")
        
        while True:
            try:
                opcao = int(input("Escolha o número da turma: "))
                if 1 <= opcao <= len(turmas):
                    return turmas[opcao - 1]
                print("Opção inválida.")
            except ValueError:
                print("Por favor, digite um número.")
            except KeyboardInterrupt:
                print("\nOperação cancelada.")
                return None
            
    def mostra_turma(self, lista_dados_turma):
        print("----------Lista de Turmas----------")
        if not lista_dados_turma:
            print("Nenhuma turma cadastrada.")
            return
        

        if not isinstance(lista_dados_turma, list):
            lista_dados_turma = [lista_dados_turma]

        for turma in lista_dados_turma:
            print(f"sala: {turma['sala']}, numero: {turma['numero']}, semestre: {turma['semestre']}")

    def seleciona_numero_turma(self):
        numero = input("Digite o número da turma")
        return numero
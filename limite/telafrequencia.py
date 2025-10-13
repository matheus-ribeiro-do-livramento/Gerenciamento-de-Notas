import datetime

class TelaFrequencia:
    def mostrar_msg(self, msg: str):
        print(msg)

    def pegar_data(self):
        print("\n--- Lançamento de Frequência ---")
        while True:
            data_str = input("Digite a data da aula (DD/MM/AAAA): ").strip()
            try:
                datetime.datetime.strptime(data_str, '%d/%m/%Y')
                return data_str 
            except ValueError:
                self.mostrar_msg("Formato de data inválido. Por favor, use o formato DD/MM/AAAA.")
            except KeyboardInterrupt:
                self.mostrar_msg("\nOperação cancelada.")
                return None

    def pegar_frequencia_aluno(self, nome_aluno: str):
        while True:
            status = input(f"Frequência para {nome_aluno} (P - Presente / F - Falta): ").upper().strip()
            if status in ['P', 'F']:
                return status
            self.mostrar_msg("Opção inválida. Digite 'P' para Presente ou 'F' para Falta.")

    def mostrar_resumo_frequencia(self, data: str, resumo: dict):
        print(f"\n--- Resumo da Frequência - {data} ---")
        for nome, status in resumo.items():
            print(f"{nome}: {'Presente' if status == 'P' else 'Falta'}")
        print("-" * 30)

    def seleciona_data(self, datas: list):
        print("\n--- Selecione a Data para Editar ---")
        for i, data in enumerate(datas, 1):
            print(f"[{i}] - {data}")
        
        while True:
            try:
                opcao = int(input("Escolha o número da data: "))
                if 1 <= opcao <= len(datas):
                    return datas[opcao - 1]
                self.mostrar_msg("Opção inválida.")
            except ValueError:
                self.mostrar_msg("Por favor, digite um número.")
            except KeyboardInterrupt:
                self.mostrar_msg("\nOperação cancelada.")
                return None

    def seleciona_aluno(self, alunos: list):
        print("\n--- Selecione o Aluno para Editar a Frequência ---")
        for i, aluno in enumerate(alunos, 1):
            print(f"[{i}] - {aluno.nome} (Matrícula: {aluno.matricula})")
        
        while True:
            try:
                opcao = int(input("Escolha o número do aluno: "))
                if 1 <= opcao <= len(alunos):
                    return alunos[opcao - 1]
                self.mostrar_msg("Opção inválida.")
            except ValueError:
                self.mostrar_msg("Por favor, digite um número.")
            except KeyboardInterrupt:
                self.mostrar_msg("\nOperação cancelada.")
                return None

    def pega_nova_frequencia(self, nome_aluno: str, status_atual: str):
        print(f"\nO status atual de {nome_aluno} é: {'Presente' if status_atual == 'P' else 'Falta'}")
        return self.pegar_frequencia_aluno(nome_aluno)

    def confirma_exclusao(self, nome_aluno: str, data: str) -> bool:
        print(f"\nTem certeza que deseja excluir a frequência de {nome_aluno} para a data {data}?")
        while True:
            resposta = input("Confirmar (S/N): ").upper().strip()
            if resposta == 'S':
                return True
            if resposta == 'N':
                self.mostrar_msg("Exclusão cancelada.")
                return False
            self.mostrar_msg("Opção inválida. Digite 'S' para Sim ou 'N' para Não.")
class TelaFrequencia:
    def mostrar_msg(self, msg: str):
        print(msg)

    def pegar_data(self):
        print("\n--- Lançamento de Frequência ---")
        data = input("Digite a data da aula (DD/MM/AAAA): ").strip()
        return data

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
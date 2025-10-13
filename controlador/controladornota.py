from limite.telanota import TelaNota

class ControladorNota:
    def __init__(self, controladorsistema):
        self.__notas_por_aluno = {}
        self.__controlador_sistema = controladorsistema
        self.__tela_nota = TelaNota()
    
    def adicionar_nota(self):
        # Pega a matrícula do aluno através da tela
        matricula = self.__tela_nota.pegar_matricula()

        aluno_existente = self.__controlador_sistema.controlador_aluno.pega_aluno_matricula(matricula)
        if aluno_existente is None:
            self.__tela_nota.mostrar_mensagem("Matricula do aluno não encontrada no sistema")
        
        # Inicializa a lista de notas do aluno se não existir
        if matricula not in self.__notas_por_aluno:
            self.__notas_por_aluno[matricula] = []
        
        # Pega a quantidade de notas através da tela
        quantidade = self.__tela_nota.quantidade_nota()
        
        # Adiciona as notas para este aluno
        for numero_nota in range(1, quantidade + 1):
            nota = self.__tela_nota.nota(numero_nota)
            self.__notas_por_aluno[matricula].append(nota)
        
        # Mostra o resultado
        notas_add = self.buscar_notas_do_aluno(matricula)
        self.exibir_notas(matricula, notas_add)
    
    def consultar_notas(self):
        matricula = self.__tela_nota.pegar_matricula()
        self.__mostrar_notas_aluno(matricula)
    
    def editar_nota(self):
        matricula = self.__tela_nota.pegar_matricula()
        notas_do_aluno = self.buscar_notas_do_aluno(matricula)

        # Mostra as notas atuais para o professor saber qual editar
        self.exibir_notas(matricula, notas_do_aluno)

        if notas_do_aluno:
            try:
                # Você precisará criar este método na sua TelaNota
                dados_edicao = self.__tela_nota.seleciona_nota_para_editar(len(notas_do_aluno))
                if dados_edicao is None:  # Permite que o usuário cancele
                    return

                indice_nota, novo_valor = dados_edicao
                
                # Atualiza a nota na lista (índice - 1 porque listas começam em 0)
                self.__notas_por_aluno[matricula][indice_nota - 1] = novo_valor
                self.__tela_nota.mostrar_mensagem("Nota alterada com sucesso!")
                
                # Mostra o resultado final
                self.exibir_notas(matricula, self.buscar_notas_do_aluno(matricula))

            except (ValueError, IndexError):
                self.__tela_nota.mostrar_mensagem("Opção inválida. Tente novamente.")

    def excluir_nota(self):
            matricula = self.__tela_nota.pegar_matricula()
            notas_do_aluno = self.buscar_notas_do_aluno(matricula)

            self.exibir_notas(matricula, notas_do_aluno)

            if notas_do_aluno:
                try:
                    # Você precisará criar este método na sua TelaNota
                    indice_para_excluir = self.__tela_nota.seleciona_nota_para_excluir(len(notas_do_aluno))
                    if indice_para_excluir is None:
                        return

                    # Remove a nota da lista
                    self.__notas_por_aluno[matricula].pop(indice_para_excluir - 1)
                    self.__tela_nota.mostrar_mensagem("Nota excluída com sucesso!")
                    
                    self.exibir_notas(matricula, self.buscar_notas_do_aluno(matricula))

                except (ValueError, IndexError):
                    self.__tela_nota.mostrar_mensagem("Opção inválida. Tente novamente.")

    def buscar_notas_do_aluno(self, matricula: int):
        return self.__notas_por_aluno.get(matricula)
    
    def exibir_notas(self, matricula: int, notas: list):
        if notas:
            self.__tela_nota.mostrar_mensagem(f'\nNotas do Aluno (Matricula: {matricula}):')
            for i, nota in enumerate(notas, 1):
                self.__tela_nota.mostrar_mensagem(f"{i}° Nota: {nota}")
        else:
            self.__tela_nota.mostrar_mensagem("Aluno não encontrado ou sem notas")

    def exibir_notas_para_aluno(self, notas: list | None):
        """
        Usa a sua própria tela (TelaNota) para exibir as notas de forma simples para o aluno.
        Este método é chamado pelo ControladorAluno.
        """
        # Supondo que você criou o método 'mostra_notas_aluno' na sua TelaNota
        self.__tela_nota.mostra_notas_aluno(notas)




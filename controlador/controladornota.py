from limite.telanota import TelaNota

class ControladorNota:
    def __init__(self, controladorsistema):
        self.__notas_por_aluno = {}  # chave: (codigo_disciplina, matricula)
        self.__controlador_sistema = controladorsistema
        self.__tela_nota = TelaNota()
    
    def adicionar_nota(self):
        # Pega a matrícula do aluno através da tela
        matricula = self.__tela_nota.pegar_matricula()

        aluno_existente = self.__controlador_sistema.controlador_aluno.pega_aluno_matricula(matricula)
        if aluno_existente is None:
            self.__tela_nota.mostrar_mensagem("Matricula do aluno não encontrada no sistema")
        
        # Busca a disciplina
        disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        
        # Mostra e seleciona o aluno
        aluno = self.__tela_nota.selecionar_aluno(disciplina.alunos)
        if aluno is None:
            return
        
        # Cria a chave única para este aluno na disciplina
        chave = (codigo_disciplina, aluno.matricula)
        
        # Inicializa a lista de notas se não existir
        if chave not in self.__notas_por_aluno:
            self.__notas_por_aluno[chave] = []
        
        # Pega a quantidade de notas
        quantidade = self.__tela_nota.quantidade_nota()
        
        # Adiciona as notas para este aluno na disciplina
        for numero_nota in range(1, quantidade + 1):
            nota = self.__tela_nota.nota(numero_nota)
            self.__notas_por_aluno[chave].append(nota)
        
        # Mostra o resultado
        notas_add = self.buscar_notas_do_aluno(matricula)
        self.exibir_notas(matricula, notas_add)
    
    def consultar_notas(self):
        # Pega o código da disciplina
        codigo_disciplina = self.__tela_nota.pegar_codigo_disciplina()
        
        # Busca a disciplina
        disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        
        # Mostra e seleciona o aluno
        aluno = self.__tela_nota.selecionar_aluno(disciplina.alunos)
        if aluno is None:
            return
        
        # Mostra as notas
        self.mostrar_notas_aluno((codigo_disciplina, aluno.matricula))
    
    def editar_nota(self):
        # Pega o código da disciplina
        codigo_disciplina = self.__tela_nota.pegar_codigo_disciplina()
        
        # Busca a disciplina
        disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        
    
        # Mostra e seleciona o aluno
        aluno = self.__tela_nota.selecionar_aluno(disciplina.alunos)
        if aluno is None:
            return
            
        # Verifica se o aluno tem notas
        chave = (codigo_disciplina, aluno.matricula)
        if chave not in self.__notas_por_aluno or not self.__notas_por_aluno[chave]:
            self.__tela_nota.mostrar_mensagem("Este aluno não possui notas cadastradas nesta disciplina.")
            return
            
        # Mostra as notas atuais e pede para selecionar uma
        self.mostrar_notas_aluno(chave)
        indice_nota = self.__tela_nota.seleciona_nota_para_editar(self.__notas_por_aluno[chave])
        
        if indice_nota is not None:
            novo_valor = self.__tela_nota.pega_novo_valor_nota()
            self.__notas_por_aluno[chave][indice_nota] = novo_valor
            self.__tela_nota.mostrar_mensagem("\nNota alterada com sucesso!")
            self.mostrar_notas_aluno(chave)

    def excluir_nota(self):
        # Pega o código da disciplina
        codigo_disciplina = self.__tela_nota.pegar_codigo_disciplina()
        
        # Busca a disciplina
        disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        
        # Mostra e seleciona o aluno
        aluno = self.__tela_nota.selecionar_aluno(disciplina.alunos)
        if aluno is None:
            return
            
        # Verifica se o aluno tem notas
        chave = (codigo_disciplina, aluno.matricula)
        if chave not in self.__notas_por_aluno or not self.__notas_por_aluno[chave]:
            self.__tela_nota.mostrar_mensagem("Este aluno não possui notas cadastradas nesta disciplina.")
            return
            
        # Mostra as notas atuais e pede para selecionar uma para excluir
        self.mostrar_notas_aluno(chave)
        indice_nota = self.__tela_nota.seleciona_nota_para_excluir(self.__notas_por_aluno[chave])
        
        if indice_nota is not None:
            nota_removida = self.__notas_por_aluno[chave].pop(indice_nota)
            self.__tela_nota.mostrar_mensagem(f"\nNota {nota_removida} removida com sucesso!")
            self.mostrar_notas_aluno(chave)
    
    def calcular_media_aluno(self, codigo_disciplina: str, matricula_aluno: int):
        chave = (codigo_disciplina, matricula_aluno)
        if chave in self.__notas_por_aluno and self.__notas_por_aluno[chave]:
            notas = self.__notas_por_aluno[chave]
            media = sum(notas) / len(notas)
            return media
        return None # Retorna None se não houver notas



        
 

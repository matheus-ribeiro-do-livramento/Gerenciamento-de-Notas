from limite.telanota import TelaNota

class ControladorNota:
    def __init__(self, controladorsistema):
        self.__notas_por_aluno = {}  
        self.__controlador_sistema = controladorsistema
        self.__tela_nota = TelaNota()
    
    def adicionar_nota(self):
        codigo_disciplina = self.__tela_nota.pegar_codigo_disciplina()
        
        disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        
        aluno = self.__tela_nota.selecionar_aluno(disciplina.alunos)
        if aluno is None:
            return
        
        chave = (codigo_disciplina, aluno.matricula)
        
        if chave not in self.__notas_por_aluno:
            self.__notas_por_aluno[chave] = []
        
        quantidade = self.__tela_nota.quantidade_nota()
        for numero_nota in range(1, quantidade + 1):
            nota = self.__tela_nota.nota(numero_nota)
            self.__notas_por_aluno[chave].append(nota)
        
        self.__tela_nota.mostrar_mensagem("\nNotas adicionadas com sucesso!")
        self.mostrar_notas_aluno(chave)
    
    def consultar_notas(self):
        codigo_disciplina = self.__tela_nota.pegar_codigo_disciplina()
        
        disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        
        aluno = self.__tela_nota.selecionar_aluno(disciplina.alunos)
        if aluno is None:
            return
        
        self.mostrar_notas_aluno((codigo_disciplina, aluno.matricula))

    def mostrar_notas_aluno(self, chave: tuple):
        notas = self.__notas_por_aluno.get(chave)
        
        if notas:
            print("\n--- Notas Atuais ---")
            for i, nota in enumerate(notas, 1):
                print(f"  {i}ª Nota: {nota}")
        else:
            self.__tela_nota.mostrar_mensagem("\nEste aluno não possui notas lançadas nesta disciplina.")
        print("-" * 20)
    
    def editar_nota(self):
        codigo_disciplina = self.__tela_nota.pegar_codigo_disciplina()
        
        disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        

        aluno = self.__tela_nota.selecionar_aluno(disciplina.alunos)
        if aluno is None:
            return
            
        chave = (codigo_disciplina, aluno.matricula)
        if chave not in self.__notas_por_aluno or not self.__notas_por_aluno[chave]:
            self.__tela_nota.mostrar_mensagem("Este aluno não possui notas cadastradas nesta disciplina.")
            return
            
        self.mostrar_notas_aluno(chave)
        indice_nota = self.__tela_nota.seleciona_nota_para_editar(len(self.__notas_por_aluno[chave]))
        
        if indice_nota is not None:
            novo_valor = self.__tela_nota.pega_novo_valor_nota()
            self.__notas_por_aluno[chave][indice_nota] = novo_valor
            self.__tela_nota.mostrar_mensagem("\nNota alterada com sucesso!")
            self.mostrar_notas_aluno(chave)

    def excluir_nota(self):
        codigo_disciplina = self.__tela_nota.pegar_codigo_disciplina()
        
        disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        
        aluno = self.__tela_nota.selecionar_aluno(disciplina.alunos)
        if aluno is None:
            return
            
        chave = (codigo_disciplina, aluno.matricula)
        if chave not in self.__notas_por_aluno or not self.__notas_por_aluno[chave]:
            self.__tela_nota.mostrar_mensagem("Este aluno não possui notas cadastradas nesta disciplina.")
            return
            
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
            return media, notas
        return None, None 
    
    def buscar_notas_do_aluno(self, matricula: int):
        notas_encontradas = {}
        for (cod_disciplina, mat_aluno), notas in self.__notas_por_aluno.items():
            if mat_aluno == matricula:
                notas_encontradas[cod_disciplina] = notas
        return notas_encontradas



        
 

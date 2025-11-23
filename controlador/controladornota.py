from limite.telanota import TelaNota
from entidade.nota import Nota

class ControladorNota:
    def __init__(self, controladorsistema):
        self.__controlador_sistema = controladorsistema
        self.__tela_nota = TelaNota()
    
    def adicionar_nota(self):        
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        
        turma = self.__controlador_sistema.controladorturma.selecionar_turma_de_disciplina(disciplina)
        if not turma:
            return

        aluno = self.__tela_nota.selecionar_aluno(turma.alunos)
        if aluno is None:
            return
        
        quantidade = self.__tela_nota.quantidade_nota()
        for numero_nota in range(1, quantidade + 1):
           valor_nota = self.__tela_nota.nota(numero_nota)

           nova_nota = Nota(valor_nota)
           nova_nota.aluno = aluno

           turma.adcionar_nota(nova_nota)
           self.__controlador_sistema.controladordisciplina.disciplina_dao.update(disciplina)

        self.__tela_nota.mostrar_mensagem("\nNotas adicionadas com sucesso!")

        notas_atualizadas = self.buscar_notas_do_aluno(aluno, turma)
        self.mostrar_notas_aluno(notas_atualizadas)
    
    def consultar_notas(self):        
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem
            ("Disciplina não encontrada!")
            return
        
        aluno = self.__tela_nota.selecionar_aluno(disciplina.alunos)
        if aluno is None:
            return
        
        controlador_turma = self.__controlador_sistema.controladorturma
        turma = controlador_turma.buscar_turma_do_aluno(aluno, disciplina)

        if not turma:
            self.__tela_nota.mostrar_mensagem("Aluno não está em nenhuma turma")
            return
        
        notas = self.buscar_notas_do_aluno(aluno, turma)
        self.mostrar_notas_aluno(notas)

    def mostrar_notas_aluno(self, notas: list):        
        if notas:
            print("\n--- Notas Atuais ---")
            for i, nota in enumerate(notas, 1):
                print(f"  {i}ª Nota: {nota}")
        else:
            self.__tela_nota.mostrar_mensagem("\nEste aluno não possui notas lançadas nesta disciplina.")
        print("-" * 20)
    
    def editar_nota(self):
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
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

        controlador_aluno = self.__controlador_sistema.controladoraluno
        controlador_turma = self.__controlador_sistema.controladorturma

        aluno = controlador_aluno.pega_aluno_matricula(matricula_aluno)
        if not aluno:
            return None, None
        
        disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
        if not disciplina:
            return None, None
        
        turma = controlador_turma.buscar_turma_do_aluno(aluno, disciplina)
        if not turma:
            return None, None

        nota_aluno = self.buscar_notas_do_aluno(aluno, turma)
        if chave in nota_aluno and nota_aluno[chave]:
            notas = nota_aluno[chave]
            media = sum(notas) / len(notas)
            return media, notas
        return None, None 
    
    def buscar_notas_do_aluno(self, aluno, turma):
        notas_encontradas = []
        for nota in turma.notas:
            if nota.aluno.matricula == aluno.matricula:
                notas_encontradas.append(nota.valor)
        return notas_encontradas

    def exibir_notas_para_aluno(self, notas_por_disciplina: dict):
        if not notas_por_disciplina:
            self.__tela_nota.mostrar_mensagem("Você ainda não possui notas lançadas em nenhuma disciplina.")
            input("\nPressione ENTER para prosseguir")
            return

        self.__tela_nota.mostrar_mensagem("\n--- Suas Notas por Disciplina ---")
        for codigo_disciplina, notas in notas_por_disciplina.items():
            disciplina = self.__controlador_sistema.controladordisciplina.pega_disciplina_codigo(codigo_disciplina)
            nome_disciplina = disciplina.nome if disciplina else f"Disciplina (Código: {codigo_disciplina})"
            
            self.__tela_nota.mostrar_mensagem(f"\nDisciplina: {nome_disciplina}")
            self.__tela_nota.mostra_notas_aluno(notas)
        
        input("\nPressione ENTER para prosseguir")

        
 

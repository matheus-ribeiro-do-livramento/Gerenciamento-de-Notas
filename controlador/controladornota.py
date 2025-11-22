from limite.telanota import TelaNota
from entidade.nota import Nota
from entidade.aluno import Aluno

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
        if turma is None:
            return

        aluno = self.__tela_nota.selecionar_aluno(turma.alunos)
        if aluno is None:
            return
        
     #   chave = (codigo_disciplina, aluno.matricula)
        
      #  if chave not in self.__notas_por_aluno:
      #      self.__notas_por_aluno[chave] = []
        
        quantidade = self.__tela_nota.quantidade_nota()
        for numero_nota in range(1, quantidade + 1):
           # nota = self.__tela_nota.nota(numero_nota)
           # self.__notas_por_aluno[chave].append(nota)
           valor_nota = self.__tela_nota.nota(numero_nota)

           nova_nota = Nota(valor_nota)
           nova_nota.aluno = aluno

           turma.adicionar_nota(nova_nota)

        self.__controlador_sistema.controladordisciplina.disciplina_dao.update(disciplina)
        
        self.__tela_nota.mostrar_mensagem("\nNotas adicionadas com sucesso!")
        self.mostrar_notas_aluno(aluno, turma)
    
    def consultar_notas(self):
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()

        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        
        turma = self.__controlador_sistema.controladorturma.selecionar_turma_de_disciplina(disciplina)
        if turma is None:
            return
        
        aluno = self.__tela_nota.selecionar_aluno(turma.alunos)
        if aluno is None:
            return
        
        self.mostrar_notas_aluno(aluno, turma)

    def mostrar_notas_aluno(self, aluno: Aluno, turma):
        notas_aluno = [nota.valor for nota in turma.notas if nota.aluno.matricula == aluno.matricula]
        
        if notas_aluno:
            print("\n--- Notas Atuais ---")
            for i, nota in enumerate(notas_aluno, 1):
                print(f"  {i}ª Nota: {nota}")
        else:
            self.__tela_nota.mostrar_mensagem("\nEste aluno não possui notas lançadas nesta disciplina.")
        print("-" * 20)
    
    def editar_nota(self):
        
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        
        turma = self.__controlador_sistema.controladorturma.selecionar_turma_de_disciplina(disciplina)
        if turma is None:
            return
        

        aluno = self.__tela_nota.selecionar_aluno(turma.alunos)
        if aluno is None:
            return
            
        notas_do_aluno_na_turma = [nota for nota in turma.notas if nota.aluno.matricula == aluno.matricula]

        if not notas_do_aluno_na_turma:
            self.__tela_nota.mostrar_mensagem("Este aluno não possui notas cadastradas nesta disciplina.")
            return
            
        self.mostrar_notas_aluno(aluno, turma)
        indice_nota = self.__tela_nota.seleciona_nota_para_editar(len(notas_do_aluno_na_turma))
        
        if indice_nota is not None:
            novo_valor = self.__tela_nota.pega_novo_valor_nota()
            notas_do_aluno_na_turma[indice_nota].valor = novo_valor
            self.__controlador_sistema.controladordisciplina.disciplina_dao.update(disciplina)
            self.__tela_nota.mostrar_mensagem("\nNota alterada com sucesso!")
            self.mostrar_notas_aluno(aluno, turma)

    def excluir_nota(self):
        
        disciplina = self.__controlador_sistema.controladordisciplina.selecionar_disciplina()
        if disciplina is None:
            self.__tela_nota.mostrar_mensagem("Disciplina não encontrada!")
            return
        
        turma = self.__controlador_sistema.controladorturma.selecionar_turma_de_disciplina(disciplina)
        if turma is None:
            return

        aluno = self.__tela_nota.selecionar_aluno(turma.alunos)
        if aluno is None:
            return
            
        notas_do_aluno_na_turma = [nota for nota in turma.notas if nota.aluno.matricula == aluno.matricula]
        valores_notas = [nota.valor for nota in notas_do_aluno_na_turma]
        if not notas_do_aluno_na_turma:
            self.__tela_nota.mostrar_mensagem("Este aluno não possui notas cadastradas nesta disciplina.")
            return
            
        self.mostrar_notas_aluno(aluno, turma)
        indice_nota = self.__tela_nota.seleciona_nota_para_excluir(valores_notas)
        
        if indice_nota is not None:
            nota_a_remover = notas_do_aluno_na_turma[indice_nota]
            turma.notas.remove(nota_a_remover)
            self.__controlador_sistema.controladordisciplina.disciplina_dao.update(disciplina)
            self.__tela_nota.mostrar_mensagem(f"\nNota {nota_a_remover.valor} removida com sucesso!")
            self.mostrar_notas_aluno(aluno, turma)
    
    def calcular_media_aluno(self, codigo_disciplina: str, matricula_aluno: int):

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

        notas_aluno = [nota.valor for nota in turma.notas if nota.aluno.matricula == aluno.matricula]
        if notas_aluno:
            media = sum(notas_aluno) / len(notas_aluno)
            return media, notas_aluno
        return None, None
    
    def buscar_notas_do_aluno(self, matricula: int):
        notas_encontradas = {}
        disciplinas = self.__controlador_sistema.controladordisciplina.disciplina_dao.get_all()
        for disciplina in disciplinas:
            for turma in disciplina.turmas:
                notas_aluno_turma = [nota.valor for nota in turma.notas if nota.aluno and nota.aluno.matricula == matricula]
                if notas_aluno_turma:
                    if disciplina.codigo not in notas_encontradas:
                        notas_encontradas[disciplina.codigo] = []
                    notas_encontradas[disciplina.codigo].extend(notas_aluno_turma)
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

        
 

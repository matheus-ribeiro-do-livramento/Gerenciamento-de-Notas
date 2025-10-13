from limite.telanota import TelaNota

class ControladorNota:
    def __init__(self, controladorsistema):
        self.__notas_por_aluno = {}
        self.__controlador_sistema = controladorsistema
        self.__tela_nota = TelaNota()
    
    def adicionar_nota(self):
        # Pega a matrícula do aluno através da tela
        matricula = self.__tela_nota.pegar_matricula()
        
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
        self.__mostrar_notas_aluno(matricula)
    
    def __mostrar_notas_aluno(self, matricula: str):
        if matricula in self.__notas_por_aluno:
            self.__tela_nota.mostrar_mensagem(f"\nNotas do aluno (Matrícula: {matricula}):")
            for i, nota in enumerate(self.__notas_por_aluno[matricula], 1):
                self.__tela_nota.mostrar_mensagem(f"{i}ª Nota: {nota}")
        else:
            self.__tela_nota.mostrar_mensagem("Aluno não encontrado ou sem notas cadastradas.")
    
    def consultar_notas(self):
        matricula = self.__tela_nota.pegar_matricula()
        self.__mostrar_notas_aluno(matricula)
    
    def editar_nota(self):
        pass
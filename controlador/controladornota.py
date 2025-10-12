from limite.telanota import TelaNota

class ControladorNota:
    def __init__(self, controladorsistema):
        self.__notas = []
        self.__controlador_sistema = controladorsistema
        self.__tela_nota = TelaNota()
    
    def adicionar_nota(self):
        notas = self.__tela_nota()
        self.__notas.append(notas)
        print(self.__notas)
    

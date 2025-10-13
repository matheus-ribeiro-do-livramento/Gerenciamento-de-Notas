from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, matricula: int):
        self.__nome = nome
        self.__matricula = matricula


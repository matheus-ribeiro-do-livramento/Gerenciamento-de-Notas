from dao.dao import DAO
from entidade.nota import Nota

class NotaDAO(DAO):
    def __init__(self):
        super().__init__('nota.pkl')

    def add(self, nota: Nota):
        if isinstance(nota, int) and (nota is not None) \
        and (nota, Nota):
            super().add(nota, nota)

    def update(self, nota: Nota):
        if isinstance(nota, Nota) and (nota is not None) \
        and (nota, int):
            super().update(nota, nota)

    def get (self, key: int):
        if isinstance(key, int):
            return super().get(key)
        
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
    
from dao.dao import DAO
from entidade.disciplina import Disciplina

class DisciplinaDAO(DAO):
    def __init__(self):
        super().__init__('disciplina.pkl')

    def add(self, disciplina: Disciplina):
        if isinstance(disciplina.codigo, int) and (disciplina is not None):
            super().add(disciplina.codigo, disciplina)

    def update(self, disciplina: Disciplina):
        if isinstance(disciplina is not None) and (disciplina.codigo, int) and isinstance(disciplina, Disciplina):
            super().update(disciplina.codigo, disciplina)

    def get (self, key: int):
        if isinstance(key, int):
            return super().get(key)
        
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
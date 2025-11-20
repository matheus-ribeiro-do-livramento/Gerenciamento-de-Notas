from dao.dao import DAO
from entidade.professor import Professor

class ProfessorDao(DAO):
    def __init__(self):
        super().__init__('professor.pkl')
    
    def add(self, professor: Professor):
        if isinstance(professor.matricula, int) and (professor is not None) and (professor, Professor):
            super().add(professor.matricula, professor)
    
    def update(self, professor: Professor):
        if isinstance(professor.matricula, int) and (professor is not None) and (professor, Professor):
            super().update(professor.matricula, professor)
    
    def get(self, key: int):
        if isinstance(key, int):
            return super().get(key)
        
    def remove(self, key: int):
        if isinstance(key, int):
            return super().remove(key)
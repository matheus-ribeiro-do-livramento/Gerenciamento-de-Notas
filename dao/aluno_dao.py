from dao.dao import DAO
from entidade.aluno import Aluno

class AlunoDAO(DAO):
    def __init(self):
        super().__init__('aluno.pkl')

    def add(self, aluno):
        super().add(aluno.matricula, aluno)

    
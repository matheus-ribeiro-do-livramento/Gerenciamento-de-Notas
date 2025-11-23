class AlunoExistenteException(Exception):
    def __init__(self):
        super().__init__('Já existe aluno com essa matricula')
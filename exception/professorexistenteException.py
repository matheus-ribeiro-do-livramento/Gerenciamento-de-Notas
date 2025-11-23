class ProfessorExistenteException(Exception):
    def __init__(self):
        super().__init__('Já existe um professor com essa matricula')
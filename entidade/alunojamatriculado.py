class AlunoJaMatriculado(Exception):
    def __init__(self, nome_aluno, nome_disciplina): 
        mensagem = f"O Aluno {nome_aluno} já esta matriculado na disciplina {nome_disciplina}"
        super().__init__(mensagem)
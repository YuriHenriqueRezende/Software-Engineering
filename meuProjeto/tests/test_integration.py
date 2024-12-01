from meuProjeto.app.models import Aluno, Professor, Curso

def test_integracao():
    aluno1 = Aluno("Yuri Rezende", 12345)
    aluno2 = Aluno("Vitor Martins", 67890)
    professor = Professor("Hugo Idagawa", 1)
    curso = Curso("Engenharia de Software")

    curso.addProfessor(professor)
    assert "Hugo Idagawa" in curso.get_professores()

    curso.addAluno(aluno1)
    curso.addAluno(aluno2)
    assert "Yuri Rezende" in curso.listAlunos()
    assert "Vitor Martins" in curso.listAlunos()

    curso.remAluno(67890)
    assert "Vitor Martins" not in curso.listAlunos()

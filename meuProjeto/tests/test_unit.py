import pytest
from meuProjeto.app.models import Aluno, Professor, Curso

@pytest.fixture
def aluno_teste():
    return Aluno(nome="Yuri Rezende", matricula=12345)

@pytest.fixture
def professor_teste():
    return Professor(nome="Hugo Idagawa", id_professor=678)

@pytest.fixture
def curso_teste():
    return Curso(nome="Engenharia de Software")

def test_aluno(aluno_teste):
    assert aluno_teste.nome == "Yuri Rezende"
    assert aluno_teste.matricula == 12345

def test_professor(professor_teste):
    assert professor_teste.nome == "Hugo Idagawa"
    assert professor_teste.id == 678

def test_curso_adicionar_professor(curso_teste, professor_teste):
    curso_teste.addProfessor(professor_teste)
    assert professor_teste.nome in curso_teste.get_professores()

def test_curso_adicionar_remover_aluno(curso_teste, aluno_teste):
    curso_teste.addAluno(aluno_teste)
    assert aluno_teste.nome in curso_teste.listAlunos()

    curso_teste.remAluno(aluno_teste.matricula)
    assert aluno_teste.nome not in curso_teste.listAlunos()

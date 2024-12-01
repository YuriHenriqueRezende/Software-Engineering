from app.models import Aluno, Professor, Curso

if __name__ == "__main__":
    # Criando alunos
    aluno1 = Aluno(nome="Yuri Rezende", matricula=23134001)
    aluno2 = Aluno(nome="Vitor Martins", matricula=23134063)

    # Criando um professor
    professor = Professor(nome="Hugo Idagawa", id_professor=1)

    # Criando um curso e associando professor e alunos
    curso = Curso(nome="Engenharia de Software")
    curso.addProfessor(professor)
    curso.addAluno(aluno1)
    curso.addAluno(aluno2)

    # Exibindo informações do curso
    print(f"Curso: {curso.nome}")
    print(f"Professor(es): {', '.join(curso.get_professores())}")
    print("Alunos matriculados:")
    for aluno in curso.listAlunos():
        print(f"  - {aluno}")

    # Removendo um aluno do curso
    curso.remAluno(23134001)

    # Exibindo informações do curso após remoção
    print("\nApós remoção do aluno:")
    print("Alunos matriculados:")
    for aluno in curso.listAlunos():
        print(f"  - {aluno}")

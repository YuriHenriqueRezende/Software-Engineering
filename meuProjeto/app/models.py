class Aluno:
    def __init__(self, nome: str, matricula: int):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @property
    def matricula(self):
        return self.__matricula


class Professor:
    def __init__(self, nome: str, id_professor: int):
        self.__nome = nome
        self.__id = id_professor

    @property
    def nome(self):
        return self.__nome

    @property
    def id(self):
        return self.__id


class Curso:
    def __init__(self, nome: str):
        self.__nome = nome
        self.__professores = []
        self.__alunos = []

    @property
    def nome(self):
        return self.__nome

    def addProfessor(self, professor: Professor):
        self.__professores.append(professor)

    def remProfessor(self, id_professor: int):
        self.__professores = [prof for prof in self.__professores if prof.id != id_professor]

    def get_professores(self):
        return [prof.nome for prof in self.__professores]

    def addAluno(self, aluno: Aluno):
        self.__alunos.append(aluno)

    def remAluno(self, matricula: int):
        self.__alunos = [aluno for aluno in self.__alunos if aluno.matricula != matricula]

    def listAlunos(self):
        return [aluno.nome for aluno in self.__alunos]

class Employee():
    def __init__(self, name):
        self.name = name

    def hours_registered(self, horas):
        print('Horas resgistradas...')

    def show_activities(self):
        print('Fez muita coisa...')


class Caelum(Employee):
    def show_activities(self):
        print('Fez muita coisa, Caelumer.')

    def search_month_courses(self, month=None):
        print(f'Mostrando cursos - Mês {month}'
              if month else 'Mostrando cursos desses mês...')


class Alura(Employee):
    def show_activities(self):
        print('Fez muita coisa, Alurete.')

    def search_questions_without_answer(self):
        print('Mostrando perguntas sem resposta do Fórum...')


class Hipster():
    def __str__(self):
        return f'Hipster, {self.name}'


class Junior(Alura):
    pass


class Pleno(Alura, Caelum, Hipster):
    pass


class Senior(Alura, Caelum, Hipster):
    pass

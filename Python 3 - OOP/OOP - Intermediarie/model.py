class Programs():
    def __init__(self, name, year):
        self._name = name.title()
        self.year = year
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def give_likes(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f'{self._name} - {self.year} - Likes: {self._likes}'


class Movie(Programs):
    def __init__(self, name, year, duration):
        super().__init__(name, year)
        self.duration = duration

    def __str__(self):
        return f'{self._name} - {self.year} - {self.duration} min - {self._likes} Likes'


class Series(Programs):
    def __init__(self, name, year, seasons):
        super().__init__(name, year)
        self.seasons = seasons

    def __str__(self):
        return f'{self._name} - {self.year} - {self.seasons} Temporadas - {self._likes} Likes'


class Playlist():
    def __init__(self, nome, programs):
        self.nome = nome
        self.programs = programs

    def __getitem__(self, item):
        return self.programs[item]

    def __len__(self):
        return len(self.programs)


##### Test Area #####

vingadores = Movie('vingadores', 2018, 160)
atlanta = Series('atlanta', 2018, 2)
family_guy = Series('family guy', 2010, 13)
simpsons = Series('the simpsons', 2008, 32)

vingadores.give_likes()
atlanta.give_likes()
simpsons.give_likes()
simpsons.give_likes()
family_guy.give_likes()
family_guy.give_likes()
family_guy.give_likes()

movies_and_series = [atlanta, vingadores, family_guy, simpsons]
playlist_weekend = Playlist('playlist do final de semana', movies_and_series)

print(f'Quantidade de Programas: {len(playlist_weekend)}')

for program in playlist_weekend:
    print(program)

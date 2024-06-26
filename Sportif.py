class Personne():
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age
        return self.age

    def __str__(self):
        return f"Bonjour je m'appelle {self.name} et j'ai {self.age} ans"

class Sportif(Personne):
    def __init__(self, name, age, sport):
        Personne.__init__(self, name, age)
        self.sport = sport

    def get_sport(self):
        return self.sport

    def __str__(self):
        return f"Je suis {self.name}, j'ai {self.age} ans et je pratique le {self.sport}"
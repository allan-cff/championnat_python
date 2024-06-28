class Personne():
    def __init__(self, name, age = 0):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Personne {self.name} d'âge {self.age} ans"

class Sportif(Personne):
    def __init__(self, name, age, sport):
        Personne.__init__(self, name, age)
        self.sport = sport

    def __str__(self):
        return f"{self.name} ({self.sport}) d'âge {self.age} ans"
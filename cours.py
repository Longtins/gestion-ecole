class Cours:
    def __init__(self, nom, professeur):
        self.nom = nom
        self.professeur = professeur
        self.eleves = []

    def inscrire(self, eleve):
        self.eleves.append(eleve)
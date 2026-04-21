class Cours:
    def __init__(self, nom, enseignant):
        self.nom = nom
        self.enseignant = enseignant
        self.eleves = []

    def inscrire(self, eleve):
        self.eleves.append(eleve)
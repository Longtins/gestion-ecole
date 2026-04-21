class Cours:
    def __init__(self, nom,sigle_cours, professeur, description = None):
        self.nom = nom
        self.professeur = professeur
        self.sigle_cours = sigle_cours
        self.description = description
        self.eleves = []

    def inscrire(self, eleve):
        self.eleves.append(eleve)
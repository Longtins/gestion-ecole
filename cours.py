class Cours:
    def __init__(self, nom,sigle_cours, enseignant,description = None):
        self.nom = nom
        self.sigle_cours = sigle_cours
        self.enseignant = enseignant
        self.description = description

    def inscrire(self, eleve):
        self.eleves.append(eleve)
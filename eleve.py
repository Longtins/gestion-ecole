class Eleve:
    def __init__(self, nom, prenom,num_etudiant,courriel):
        self.nom = nom
        self.prenom = prenom
        self.num_etudiant = num_etudiant
        self.courriel = courriel

    def __str__(self):
        return f"{self.prenom} {self.nom} (numéro: {self.num_etudiant}) — {self.courriel}"
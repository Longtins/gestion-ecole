class Eleve:
    def __init__(self, nom, prenom, num_etudiant, telephone):
        self.nom = nom
        self.prenom = prenom
        self.num_etudiant = num_etudiant
        self.telephone = telephone

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.telephone})(numéro: {self.num_etudiant}) — {self.telephone}"

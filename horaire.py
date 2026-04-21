class Horaire:
    def __init__(self, cours, jour, heure_debut, heure_fin, local):
        self.cours = cours
        self.jour = jour
        self.heure_debut = heure_debut
        self.heure_fin = heure_fin
        self.local = local

    def __str__(self):
        return f"{self.cours} — {self.jour} de {self.heure_debut} à {self.heure_fin} (local {self.local})"
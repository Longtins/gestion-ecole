class Absence:
    def __init__(self, eleve, cours, date):
        self.eleve = eleve
        self.cours = cours
        self.date = date
        self.justifiee = False

    def justifier(self):
        self.justifiee = True

    def __str__(self):
        statut = "justifiée" if self.justifiee else "non justifiée"
        return f"Absence de {self.eleve} en {self.cours} le {self.date} ({statut})"
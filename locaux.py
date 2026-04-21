class Local:
    def __init__(self, numero, capacite, type_local):
        self.numero = numero
        self.capacite = capacite
        self.type_local = type_local

    def __str__(self):
        return f"Local {self.numero} (capacité {self.capacite}, type {self.type_local})"

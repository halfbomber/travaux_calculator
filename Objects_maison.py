
def __init__(self):
    pass

class Maison:
    def __init__(self):
        self.Longueur = float()
        self.Largeur = float()
        self.Hauteur = float()
        self.PieceS = int()

class Piece:
    def __init__(self):
        self.Longueur = float()
        self.Largeur = float()
        self.Hauteur = float()
        self.FaceS = int()

    def surface(self):
        return (self.Longueur * self.Hauteur)

    def volume(self):
        return (self.Largeur * self.Longueur * self.Hauteur)


class Face:
    def __init__(self):
        self.Longueur = float()
        self.LargHaut= float()
        self.OuvertureS = int()

class Ouverture:
    def __init__(self):
        self.Longueur = float()
        self.Largeur= float()

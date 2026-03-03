import random
from pokemonchoice import Pokemon

class Random_Pokemon(Pokemon):
    def __init__(self):
        # On choisit un ID au hasard (1 à 151)
        random_id = str(random.randint(1, 151))
        # On utilise le code de la classe Pokemon
        super().__init__(random_id)
        # L'ennemi est toujours de face
        self.image = self.image_front
class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100, hidden: bool = False):
        self.name = name
        self.health = health
        self.hidden = hidden
        Animal.alive.append(self)

    def __repr__(self):
        return f"{{Name: {self.name}, Health: {self.health}, Hidden: {self.hidden}}}"

    def is_alive(self):
        return self.health > 0

    def die(self):
        if self in Animal.alive:
            Animal.alive.remove(self)

class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


var = 8
def bite(other):
    if isinstance(other, Herbivore) and not other.hidden:
        other.health -= 50
        if other.health <= 0:
            other.die()


class Carnivore(Animal):
    pass


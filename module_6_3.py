import random

class Animal:
    def __init__(self, live = True, sound = None, _degree_of_danger = 0, speed = 1):
        self.live = live
        self.sound = sound
        self._degree_of_danger = _degree_of_danger
        self.speed = speed
        self._cords = [0, 0, 0]

    def move(self, dx, dy, dz):
        self._cords[0] += self.speed * dx
        self._cords[1] += self.speed * dy
        self._cords[2] += self.speed * dz
        if dz < 0:
            print("It's too deep, i can't dive :(")

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._degree_of_danger > 0:
            print("Be careful, i'm attacking you 0_0")
        else:
            print("Sorry, i'm peaceful :)" )

    def speak(self):
        if self.sound:
            print(self.sound)
        else:
            print('...')

class Bird(Animal):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.beak = True

    def lay_eggs(self):
        random_number = random.randint(0, 4)
        print(f"Here are(is) {random_number} eggs for you")

class AquaticAnimal(Animal):
    def __init__(self, _degree_of_danger=3, **kwargs):
        super().__init__(_degree_of_danger=_degree_of_danger, **kwargs)

    def dive_in(self, dz):
        self._cords[2] -= self.speed * abs(dz) / 2

class PoisonousAnimal(Animal):
    def __init__(self, _degree_of_danger=8, **kwargs):
        super().__init__(_degree_of_danger=_degree_of_danger, **kwargs)

class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):  # Порядок наследования важен!
    def __init__(self, speed=1, sound="Click-click-click", **kwargs):
        super().__init__(speed=speed, sound=sound, **kwargs)

db = Duckbill(10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()
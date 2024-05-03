from abc import ABC, abstractmethod

# Создание абстрактного класса для оружия
class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass
# Реализация конкретных типов оружия

class Sword(Weapon):
    def attack(self):
        print("Боец наносит удар мечом.")

class Bow(Weapon):
    def attack(self):
        print("Боец наносит удар из лука.")

# класс Fighter

class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def change_weapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            print(f"{self.name} выбирает {self.weapon.__class__.__name__}.")
            self.weapon.attack()
        else:
            print("Боец не выбрал оружие.")

class Monster:
    def __init__(self, name):
        self.name = name

    def is_defeated(self):
        print(f"{self.name} побежден!")

# Пример использования:

fighter = Fighter("Алеша Попович")
sword = Sword()
bow = Bow()
monster = Monster("Тугарин")

fighter.change_weapon(sword)
fighter.attack()
monster.is_defeated()

fighter.change_weapon(bow)
fighter.attack()
monster.is_defeated()
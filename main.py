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


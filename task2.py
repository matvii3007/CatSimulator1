class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        print(self.name, "атакує!")


class Hero(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        print(self.name, "атакує зброєю:", self.weapon)


class Enemy(Character):
    def __init__(self, name, health, damage):
        super().__init__(name, health)
        self.damage = damage

    def attack(self):
        print(self.name, "атакує! Шкода:", self.damage)


# Створення персонажів
hero = Hero("Герой", 100, "Меч")
enemy = Enemy("Ворог", 80, 20)

hero.attack()
enemy.attack()
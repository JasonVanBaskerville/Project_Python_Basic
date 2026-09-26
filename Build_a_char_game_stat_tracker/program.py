class GameCharacter:
    def __init__(self, name):
        self._name = name
        self._health = 100
        self._mana = 50
        self._level = 1

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, new_health):
        if new_health < 0:
            self._health = 0
        elif new_health > 100:
            self._health = 100
        else:
            self._health = new_health
        print(f"Health was successfully changed.")
    
    @property
    def mana(self):
        return self._mana

    @mana.setter
    def mana(self, new_mana):
        if new_mana < 0:
            self._mana = 0
        elif new_mana > 50:
            self._mana = 50
        else:
            self._mana = new_mana
        print(f"Mana was successfully changed.")

    @property
    def level(self):
        return self._level

    def level_up(self):
        self._level += 1
        self.health = 100
        self.mana = 50
        print(f"{self.name} leveled up to {self.level}!")

    def __str__(self):
        teks = f"Name: {self.name}\nLevel: {self.level}\nHealth: {self.health}\nMana: {self.mana}"
        return teks


# Object
character1 = GameCharacter("Prince")
print(character1)

# Health
character1.health = 70
print(character1.health)

character1.health = -20
print(character1.health)

character1.health = 150
print(character1.health)


# Mana
character1.mana = 30
print(character1.mana)

character1.mana = 100
print(character1.mana)

# Level
character1.health = 40
character1.mana = 10

print(character1)

character1.level_up()
print(character1)
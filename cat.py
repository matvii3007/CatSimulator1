
class Cat:
    def __init__(self, name):
        self.name = name
        self.age = 1
        self.hunger = 50
        self.energy = 100
        self.happiness = 80
        self.health = 100

    def eat(self):
        self.hunger = max(0, self.hunger - 30)
        self.happiness = min(100, self.happiness + 10)
        print(f"\n{self.name} смачно поїв!")

    def play(self):
        if self.energy >= 20:
            self.energy -= 20
            self.happiness = min(100, self.happiness + 20)
            self.hunger = min(100, self.hunger + 10)
            print(f"\n{self.name} весело грається!")
        else:
            print(f"\n{self.name} занадто втомився!")

    def sleep(self):
        self.energy = min(100, self.energy + 40)
        self.hunger = min(100, self.hunger + 10)
        print(f"\n{self.name} солодко спить!")

    def next_day(self):
        self.hunger = min(100, self.hunger + 15)
        self.energy = max(0, self.energy - 10)
        self.happiness = max(0, self.happiness - 5)
        self.age += 1

        if self.hunger >= 80:
            self.health = max(0, self.health - 10)

        if self.energy == 0:
            self.health = max(0, self.health - 5)

        if self.happiness < 20:
            self.health = max(0, self.health - 5)

        print(f"\nПройшов ще один день життя {self.name}!")

    def show_status(self):
        print("\n" + "=" * 30)
        print(f"       КОТИК {self.name}")
        print("=" * 30)
        print(f"Вік: {self.age} днів")
        print(f"Голод: {self.hunger}/100")
        print(f"Енергія: {self.energy}/100")
        print(f"Щастя: {self.happiness}/100")
        print(f"Здоров'я: {self.health}/100")
        print("=" * 30)


cat = Cat(input("Як звати твого котика? "))

print(f"\nВітаємо! Тепер ти доглядаєш за котиком {cat.name}!")

while cat.health > 0:
    cat.show_status()

    print("\nЩо хочеш зробити?")
    print("1. Погодувати котика")
    print("2. Погратися з котиком")
    print("3. Покласти котика спати")
    print("4. Наступний день")
    print("5. Вийти з гри")

    choice = input("\nТвій вибір: ")

    if choice == "1":
        cat.eat()
    elif choice == "2":
        cat.play()
    elif choice == "3":
        cat.sleep()
    elif choice == "4":
        cat.next_day()
    elif choice == "5":
        print("\nДякуємо за гру! Бережи свого котика!")
        break
    else:
        print("\nНеправильний вибір! Спробуй ще раз.")

if cat.health <= 0:
    print(f"\nНа жаль, {cat.name} помер. Гру завершено.")

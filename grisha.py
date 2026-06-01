import time
import random
import json
import os

SAVE_FILE = "grisha_save.json"

class Hamster:
    def __init__(self, name):
        self.name = name
        self.breed = "Джунгарский"
        self.color = "Жемчужный"
        self.gender = "Мальчик"
        self.age = "1 год 9 месяцев (Почтенный возраст 🧓)"
        
        # Характеристики
        self.satiety = 75   
        self.energy = 55    
        self.happiness = 60 
        
        # Экономика
        self.coins = 10 

        # Список случайных мыслей и действий Гриши
        self.thoughts = [
            "Гриша тщательно чистит свою красивую жемчужную шубку. ✨",
            "Гриша сладко зевнул и потянулся всеми четырьмя лапками. 💤",
            "Гриша тихонько шуршит опилками, обустраивая теплое гнёздышко. 🪵",
            "Гриша забавно набил обе щёчки воображаемыми семечками. 🐹",
            "Гриша внимательно смотрит на вас своими чёрными глазками-бусинками. 👀",
            "Гриша замер на секунду и прислушался к шорохам в комнате. 👂",
            "Гриша умывает мордочку крошечными лапками. 🥰",
            "Гриша думает о том, какая у него вкусная заначка в углу клетки. 🍕"
        ]

    def show_status(self):
        print(f"\n--- 🐹 Профиль любимого питомца ---")
        print(f"Имя: {self.name} | Пол: {self.gender}")
        print(f"Порода: {self.breed} | Окрас: {self.color}")
        print(f"Возраст: {self.age}")
        print(f"----------------------------------")
        print(f"🍕 Сытость: {self.satiety}/100")
        print(f"⚡ Энергия: {self.energy}/100")
        print(f"❤️ Счастье: {self.happiness}/100")
        print(f"🪙 Баланс: {self.coins} монет")
        print(f"----------------------------------")
        # Показываем случайную мысль хомячка каждый ход
        print(f"💭 Мысли Гриши: {random.choice(self.thoughts)}")
        print(f"----------------------------------")

    def feed(self):
        print(f"\nВы дали {self.name} мягкое детское пюре и полезные семена!")
        self.satiety = min(100, self.satiety + 30)
        self.happiness = min(100, self.happiness + 10)
        earned = random.randint(3, 7)
        self.coins += earned
        print(f"🪙 Вы заработали {earned} монет за заботу!")

    def play(self):
        if self.energy < 25:
            print(f"\n{self.name} не хочет в колесо, он тихонько шуршит в опилках.")
            return
        print(f"\n{self.name} вспомнил молодость и немного побегал в колесе! 🎡")
        self.happiness = min(100, self.happiness + 15)
        self.energy = max(0, self.energy - 30)
        self.satiety = max(0, self.satiety - 15)
        earned = random.randint(5, 10)
        self.coins += earned
        print(f"🪙 Вы заработали {earned} монет за активность!")

    def pet(self):
        print(f"\nВы аккуратно погладили {self.name} за ушком. Он довольно зажмурился... 🥰")
        self.happiness = min(100, self.happiness + 25)
        self.energy = min(100, self.energy + 5) 
        earned = random.randint(2, 5)
        self.coins += earned
        print(f"🪙 Вы заработали {earned} монет за любовь!")

    def sleep(self):
        print(f"\n{self.name} свернулся в пушистый жемчужный комочек и спит... 💤")
        time.sleep(2)
        self.energy = min(100, self.energy + 50)
        self.satiety = max(0, self.satiety - 10)
        print("💤 Гриша отлично отдохнул!")

    def shop(self):
        while True:
            print(f"\n--- 🛒 ЗООМАГАЗИН ДЛЯ ГРИШИ ---")
            print(f"Ваш баланс: {self.coins} монет")
            print(f"-------------------------------")
            print("1. 💎 Минеральный камень (Цена: 15 монет) -> +20 к Счастью")
            print("2. 🍓 Вкусный ягодный дропс (Цена: 30 монет) -> +40 к Сытости")
            print("3. 🪵 Мягкая труба для лазания (Цена: 50 монет) -> +40 к Энергии и +20 к Счастью")
            print("4. ❌ Выйти из магазина")
            
            choice = input("\nЧто хотите купить Грише? (1-4): ")
            
            if choice == "1":
                if self.coins >= 15:
                    self.coins -= 15
                    self.happiness = min(100, self.happiness + 20)
                    print(f"\n🎉 Вы купили минеральный камень! Гриша с удовольствием точит об него зубки!")
                else:
                    print("\n❌ Недостаточно монет! Погладьте или покормите Гришу, чтобы заработать.")
            elif choice == "2":
                if self.coins >= 30:
                    self.coins -= 30
                    self.satiety = min(100, self.satiety + 40)
                    print(f"\n🎉 Вы купили ягодный дропс! Гриша мгновенно спрятал его за щеку!")
                else:
                    print("\n❌ Недостаточно монет!")
            elif choice == "3":
                if self.coins >= 50:
                    self.coins -= 50
                    self.energy = min(100, self.energy + 40)
                    self.happiness = min(100, self.happiness + 20)
                    print(f"\n🎉 Вы купили новую трубу! Гриша обустраивает в ней уютное гнездышко!")
                else:
                    print("\n❌ Недостаточно монет!")
            elif choice == "4":
                print("\nВы вышли из магазина.")
                break
            else:
                print("\nНеверный пункт меню.")

    def save_game(self):
        data = {
            "satiety": self.satiety,
            "energy": self.energy,
            "happiness": self.happiness,
            "coins": self.coins
        }
        with open(SAVE_FILE, "w") as f:
            json.dump(data, f)
        print("💾 Прогресс и монеты успешно сохранены!")

    def load_game(self):
        if os.path.exists(SAVE_FILE):
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
                self.satiety = data.get("satiety", 75)
                self.energy = data.get("energy", 55)
                self.happiness = data.get("happiness", 60)
                self.coins = data.get("coins", 10)
            print("📂 Предыдущее сохранение загружено!")
        else:
            print("✨ Началась новая игра! Сохранений пока нет.")

def main():
    grisha = Hamster("Гриша")
    print(f"Добро пожаловать в игру про вашего долгожителя {grisha.name}!")
    grisha.load_game()
    
    while True:
        grisha.show_status()
        if grisha.satiety <= 20:
            print(f"⚠️ {grisha.name} проголодался, пора обновить кормушку!")
        print("\nЧто вы хотите сделать?")
        print("1. Покормить вкусняшкой")
        print("2. Выпустить побегать")
        print("3. Погладить и приласкать")
        print("4. Уложить отдыхать")
        print("5. 🛒 Открыть Магазин")
        print("6. Сохранить игру")
        print("7. Выйти из игры")
        
        choice = input("Выберите действие (1-7): ")
        if choice == "1":
            grisha.feed()
        elif choice == "2":
            grisha.play()
        elif choice == "3":
            grisha.pet()
        elif choice == "4":
            grisha.sleep()
        elif choice == "5":
            grisha.shop()
        elif choice == "6":
            grisha.save_game()
        elif choice == "7":
            grisha.save_game()
            print(f"Вы вышли. Берегите Гришу, он у вас настоящий молодец! 👋")
            break
        else:
            print("Пожалуйста, введите цифру от 1 до 7.")

if __name__ == "__main__":
    main()

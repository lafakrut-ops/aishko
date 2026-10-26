
import random


brands_of_car = ["BMW", "Mercedes", "Tesla", "Audi"]
job_list = [
    ("Programmer", 150, 5),
    ("Designer", 100, 3),
    ("Teacher", 80, 2),
]


class House:
    def __init__(self):
        self.food = 50
        self.mess = 0


class Auto:
    def __init__(self, brands):
        self.brand = random.choice(brands)
        self.fuel = 100
        self.strength = 100

    def drive(self):
        if self.fuel >= 10 and self.strength >= 10:
            self.fuel -= 10
            self.strength -= 5
            return True
        return False


class Job:
    def __init__(self, jobs):
        self.job, self.salary, self.gladness_less = random.choice(jobs)


class Human:
    def __init__(self, name="Human", job=None, home=None, car=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car is not None and not self.car.drive():
            self.to_repair()

        self.job = Job(job_list)

    def eat(self):
        if self.home.food < 5:
            self.shopping("food")

        if self.home.food >= 5 and self.satiety < 100:
            self.satiety = min(100, self.satiety + 5)
            self.home.food -= 5
            print("I am eating")

    def work(self):
        if self.car.fuel < 20:
            self.shopping("fuel")
            return

        if self.car.strength < 15:
            self.to_repair()
            return

        if not self.car.drive():
            self.to_repair()
            return

        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4
        self.home.mess += 1
        print(f"I am working as a {self.job.job}")

    def shopping(self, manage):
        if manage == "fuel":
            print("Buying fuel")
            self.money -= 30
            self.car.fuel += 100

        elif manage == "food":
            print("Buying food")
            self.money -= 50
            self.home.food += 50

        elif manage in ("eda", "delicacies"):
            print("Buying treats")
            self.gladness = min(100, self.gladness + 10)
            self.satiety = min(100, self.satiety + 2)
            self.money -= 15

    def chill(self):
        self.gladness = min(100, self.gladness + 10)
        self.home.mess = max(0, self.home.mess - 5)
        print("I am chilling")

    def clean_home(self):
        self.home.mess = 0
        self.gladness = min(100, self.gladness + 5)
        print("The house is clean")

    def to_repair(self):
        self.car.strength = 100
        self.money -= 50
        print("The car has been repaired")

    def days_index(self, day):
        title = f"Today is day {day} of {self.name}'s life"
        print(f"{title:=^50}\n")
        print(f"Money: {self.money}")
        print(f"Gladness: {self.gladness}")
        print(f"Satiety: {self.satiety}")

        print(f"\n{'Home status':=^50}")
        print(f"Food: {self.home.food}")
        print(f"Mess: {self.home.mess}")

        print(f"\n{self.car.brand} car status")
        print(f"Fuel: {self.car.fuel}")
        print(f"Strength: {self.car.strength}")
        print()

    def is_alive(self):
        if self.gladness <= 0:
            print("Depression...")
            return False

        if self.satiety <= 0:
            print("Dead from hunger...")
            return False

        if self.money < -500:
            print("Bankrupt!")
            return False

        return True

    def live(self, day):
        if not self.is_alive():
            return False

        if self.home is None:
            print("Settled in a house")
            self.get_home()

        if self.car is None:
            self.get_car()
            print(f"I bought a car: {self.car.brand}")

        if self.job is None:
            self.get_job()
            print(
                f"I got a job: {self.job.job}, "
                f"salary: {self.job.salary}"
            )

        self.days_index(day)

        dice = random.randint(1, 6)

        if self.satiety < 20:
            print("I need to eat")
            self.eat()

        elif self.gladness < 20:
            print("I need some rest")
            self.chill()

        elif self.home.mess > 15:
            print("Cleaning time!")
            self.clean_home()

        elif self.money < 0:
            print("I need to work")
            self.work()

        elif self.car.strength < 15:
            print("I need to repair my car")
            self.to_repair()

        elif self.car.fuel < 20:
            self.shopping("fuel")

        elif dice == 1:
            self.chill()

        elif dice == 2:
            self.work()

        elif dice == 3:
            self.clean_home()

        elif dice == 4:
            self.shopping("delicacies")

        elif dice == 5:
            self.eat()

        else:
            self.work()

        return self.is_alive()


class auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strength = brand_list[self.brand]["strength"]
        self.consumption = brand_list[self.brand]["consumption"]
    def drive(self):
        if self.strength > 0 and self.fuel > 0:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print("I am cant drive")
            return False











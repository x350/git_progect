# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.

import random

class Animal:
    """Базовый класс"""
    count = 0
    def __init__(self):
        Animal.count += 1

    # def sey(self):
    #     raise NotImplementedError
    #


class Mammals(Animal):
    """Класс млекопитающие"""
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name


class Birds(Animal):
    """Класс птицы"""
    name = ''
    def __init__(self):
        super().__init__()

    def getEgg(self):
        egg = Egg(self.name)
        return egg


class Egg() :
    def __init__(self, whoseEgg):
        self.weight = random.random()*200
        self.whoseEgg = whoseEgg


class Cow(Mammals):
    """Класс корова"""
    def __init__(self, name):
        super().__init__(name)

    def say(self):
        print("Му-у-у-у, мычит {}.".format(self.name))


class Goat(Mammals):
    """Класс  коза"""
    def __init__(self, name):
        super().__init__(name)

    def say(self):
        print("Бе-е-е-е, бекает {}.".format(self.name))


class Sheep(Mammals):
    """Класс овца"""
    def __init__(self, name):
        super().__init__(name)

    def say(self):
        print("Ме-е-е-е, мекает {}.".format(self.name))


class Pig(Mammals):
    """Класс свинья"""
    def __init__(self, name):
        super().__init__(name)

    def say(self):
        print("Хрю-хрю, хрюкает {}.".format(self.name))


class Ducks(Birds):
    """Класс утка"""
    name = 'Уткa'
    def __init__(self):
        super().__init__()

    def say(self):
        print("Кря-кря")


class Chicken(Birds):
    """Класс курица"""
    name = 'Курицa'
    def __init__(self):
        super().__init__()
    def say(self):
        print("Ко-о-о-ко-ко-ко-о")


class Geese(Birds):
    """Класс гусь"""
    name = 'Гусa'
    def __init__(self):
        super().__init__()
    def say(self):
        print("Га-га-га")


class Farm():
    def __init__(self, l_cows, l_goats, l_sheeps, l_pigs, nDucks, nChicken, nGeese):
        self.l_cows = l_cows
        self.l_goats = l_goats
        self.l_sheeps = l_sheeps
        self.l_pigs = l_pigs
        self.nDucks = nDucks
        self.nChicken = nChicken
        self.nGeese = nGeese

    def createFarm(self):
        our_farm = {'cows': [], 'goats': [], 'sheeps': [], 'pigs': [], 'ducks': [], 'chicken': [], 'geese': [] }
        for item in self.l_cows:
            our_farm['cows'].append(Cow(item))

        for item in self.l_goats:
            our_farm['goats'].append(Goat(item))

        for item in self.l_sheeps:
            our_farm['sheeps'].append(Sheep(item))

        for item in self.l_pigs:
            our_farm['pigs'].append(Pig(item))

        for item in range(self.nDucks):
            our_farm['ducks'].append(Ducks())

        for item in range(self.nChicken):
            our_farm['chicken'].append(Chicken())

        for item in range(self.nGeese):
            our_farm['geese'].append(Geese())
        return  our_farm


list_cows_name = ['Дуся', 'Зорька', 'Бася', 'Машка', 'Астра' ]
list_goats_name = ['Белка', 'Снежка', 'Шустрая', 'Чернушка']
list_sheeps_name = ['Шон', 'Тимми', 'мать Тимми', 'Лола', 'перая овца', 'вторая овца', 'третья овца']
list_pigs_name = ['Ганс', 'Брунс', 'Астор']


my_farm = Farm(list_cows_name, list_goats_name, list_sheeps_name,  list_pigs_name, 10, 12, 4 )
our_farm = my_farm.createFarm()
for item in our_farm['cows']:
    item.say()
for item in our_farm['goats']:
    item.say()
for item in our_farm['sheeps']:
    item.say()
for item in our_farm['pigs']:
    item.say()
for item in our_farm['ducks']:
    item.say()
print("У меня на ферме {} животных".format(Animal.count))
duck = Ducks()
egg = duck.getEgg()
print("{} снесла яйцо, весом {:0.1f} грамм".format(egg.whoseEgg, egg.weight))

# Коровы, козы, овцы, свиньи;
# Утки, куры, гуси.
import random


class Animal:
    """Базовый класс"""
    count = 0

    def __init__(self):
        Animal.count += 1


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

    def get_egg(self):
        return Egg(self.name)


class Egg:
    def __init__(self, whose_egg):
        self.weight = random.random()*200
        self.whose_egg = whose_egg


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
    name = 'Гусыня'

    def __init__(self):
        super().__init__()

    def say(self):
        print("Га-га-га")


class Farm:
    def __init__(self, l_cows, l_goats, l_sheeps, l_pigs, n_ducks, n_chicken, n_geese):
        self.l_cows = l_cows
        self.l_goats = l_goats
        self.l_sheeps = l_sheeps
        self.l_pigs = l_pigs
        self.n_ducks = n_ducks
        self.n_chicken = n_chicken
        self.n_geese = n_geese

    def create_farm(self):
        our_farm = {'cows': [], 'goats': [], 'sheeps': [], 'pigs': [], 'ducks': [], 'chicken': [], 'geese': [] }
        for item in self.l_cows:
            our_farm['cows'].append(Cow(item))

        for item in self.l_goats:
            our_farm['goats'].append(Goat(item))

        for item in self.l_sheeps:
            our_farm['sheeps'].append(Sheep(item))

        for item in self.l_pigs:
            our_farm['pigs'].append(Pig(item))

        for item in range(self.n_ducks):
            our_farm['ducks'].append(Ducks())

        for item in range(self.n_chicken):
            our_farm['chicken'].append(Chicken())

        for item in range(self.n_geese):
            our_farm['geese'].append(Geese())
        return our_farm


list_cows_name = ['Дуся', 'Зорька', 'Бася', 'Машка', 'Астра' ]
list_goats_name = ['Белка', 'Снежка', 'Шустрая', 'Чернушка']
list_sheeps_name = ['Шон', 'Тимми', 'мать Тимми', 'Лола', 'перая овца', 'вторая овца', 'третья овца']
list_pigs_name = ['Ганс', 'Брунс', 'Астор']

my_farm = Farm(list_cows_name, list_goats_name, list_sheeps_name,  list_pigs_name, 10, 12, 4 )
our_farm = my_farm.create_farm()
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
egg = duck.get_egg()
print("{} снесла яйцо, весом {:0.1f} грамм".format(egg.whose_egg, egg.weight))


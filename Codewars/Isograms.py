class Car:

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed

    def __del__(self):
        print(f'{self.name} удален')

    def __str__(self):
        return str((self.name, self.color, self.year, self.is_crashed))


bmw = Car('BMW X6', 'white', 1920, True)
mazda = Car('Mazda CX7', 'black', 1920, True)
mazda.is_crashed = False
x = str(mazda)
print(x)

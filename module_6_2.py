class Vehicle():
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']
    def __init__(self, owner, __model, __engine_power, __color):
        self.owner = str(owner)
        self.__model = str(__model)
        self.__engine_power =int(__engine_power)
        self.__color = str(__color)

    def get_model(self):
        print(f'Модель : {self.__model}')

    def get_horsepowerr(self):
        print(f'Мощность двигателя : {self.__engine_power}')

    def get_color(self):
        print(f'Цвет автомобиля : {self.__color}')

    def print_info(self):
        self.get_model()
        self.get_horsepowerr()
        self.get_color()
        print(f'Владелец : {self.owner}')

    def set_color(self, new_color):
        reg_colours = [colour.lower() for colour in self.__COLOR_VARIANTS]
        if  new_color.lower() in reg_colours:
            self.__color = new_color
        else:
            print(f'Нельзя сменить цвет {new_color}\n')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

Vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
Vehicle1.print_info()

Vehicle1.set_color('Pink')
Vehicle1.set_color('BLACK')
Vehicle1.owner = 'Vasyok'

Vehicle1.print_info()



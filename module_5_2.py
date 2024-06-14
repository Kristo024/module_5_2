class House:

    def __init__(self):
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print(self.numberOfFloors)

    # def __del__(self):
    #     print(f'Строительство {self.numberOfFloors} этажей завершено')


h1 = House()
h1.setNewNumberOfFloors(11)
h2 = House()
h2.setNewNumberOfFloors(33)
class House () :
    houses_history = []
    first = ()
    __instance = None

    def __new__(cls,*args,**kwargs) :
        if cls.__instance is None :
            first = ''
            second = 0
            third = 0
        cls.houses_history.append(args[0])
        return super().__new__(cls)
        cls.first = args[0]

    def __init__(self, first, second = 25, third = 3.14):

        self.first = first
        self.second = second
        self. third = third
# =========
    def __del__(self):

        print(self.first,' снесён, но он останется в истории')
 # ======


h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)


# Удаление объектов

del h2

del h3


print(House.houses_history)
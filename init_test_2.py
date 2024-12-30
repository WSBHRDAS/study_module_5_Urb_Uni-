class House () :
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__ (self) :
        return self.number_of_floors

    def __str__ (self) :
        str_temp = str(f'Название {self.name}, Количество этажей: {len(self)}')
        return str_temp

    def __eq__(self, other) :
        return self.name == other.name and self.number_of_floors == other.number_of_floors

    # def __lt__(<)  :
    #
    # def __le__(<=) :
    #
    # def __gt__(>) :
    #
    # def __ge__(>=) :
    #
    # def __ne__(!=) :
    #
    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1 :
            print ("Такого этажа не существует")
        else:
            for i in range(1, (new_floor+1)) :
                print (i)

h1 = House("ЖК Горки парк", 10)
h2 = House("ЖК Домик в деревне", 20)

str_temp2 = h1.__str__()
print(str_temp2)
print(h2)

print (len(h1))
print (len(h2))


from pyclbr import Class
from secrets import choice


class Database :
    instances = []
    def __init__(self):
        self.data = {}
        Database.instances.append(self)

    def __repr__(self):
        return f"{self.__class__}"

    def __str__(self):
        return f"{self.data}"


    def add_user (self, username, password) :
        self.data[username] = password

class  User :
    """
    класс пользователя, содержащий атрибуты: логин, пароль
    
    """
    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm :
            self.password = password

if __name__ == '__main__':
    database = Database()
    while True:
        choice = input ("приветствую! Выберите действие: \n1 - вход по логину\n2- регистрация\n3 - выход\n")
        if choice == '2' :


            user = User(login := input("Введите логин: "), password := input("Введите пароль: "), password2 := input("Повторите пароль: " ) )
            if password == password2 :
                database.add_user(user.username,user.password)
                print ("Добавлен пользователь ", login)
            else:
                print ("введенные пароли не совпадают!")
                # exit()
        elif choice == '1':
            print ("проверка на вход")
        elif choice == '3' :
            # break
            print(list(map(str,database.instances)))
            print ("вы вышли")
            exit()
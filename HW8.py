import time

""" 1. Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации
(отвечающий за добавку к выбираемому лимонаду). 
В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия
 добавки, а иначе отобразится следующая фраза: «Обычная газировка».
"""

print()
print("----------TASK 1 ------------------")
class ():

    def __init__(self, add):

        self.add = add

    def show_my_drink(self):
        if self.add:
            print("Газировка и", self.add)
        else:
            print("Cola")


drink1 = Soda("Lite")
drink2 = Soda("Vanila")
drink3 = Soda("Zero")

#print(drink2.add)

drink1.show_my_drink()
drink2.show_my_drink()
drink3.show_my_drink()

""" 2.Николай – оригинальный человек. 
Он решил создать класс Nikola, принимающий при инициализации 2 параметра: имя и возраст.
Но на этом он не успокоился. 
Не важно, какое имя передаст пользователь при создании экземпляра, оно всегда будет содержать “Николая”. 
В частности - если пользователя на самом деле зовут Николаем, то с именем ничего не произойдет,
 а если его зовут, например, Максим, то оно преобразуется в “Я не Максим, а Николай”.
Более того, никаких других атрибутов и методов у экземпляра не может быть добавлено, даже если кто-то
 и вздумает так поступить (т.е. если некий пользователь решит прибавить к экземпляру свойство «отчество»
  или метод «приветствие», то ничего у такого хитреца не получится).
Для ограничения количества наборов свойств и методов в экземпляре применяется специальный магический
 атрибут __slots__."""

print()
print("----------TASK 2 ------------------")

class Nikola():
    __slots__ = "name", "age"

    def __init__(self, age, name = "Николай"):
        self.name = name
        self.age = age

        if self.name != "Николай":
            print(f"Я не {self.name}, а Николай")


    def greeting(self):
        pass

person2 = Nikola(25, "Николай")
print(f"Я действительно {person2.name}")
print()
person1 = Nikola(21, "Виталик")
print(f"Я действительно {person1.name}")
person1.greeting() # Метод привет не работает, ничего не происходит
# person1.last_name = "Васильевич"  # присвоить отчество не получится
print()
print("----------TASK 3 ------------------")

""" 3.Напишите программу с классом Student, в котором есть три атрибута: name,
# groupNumber и age. По умолчанию name = Ivan, age = 18, groupNumber = 10A. 
# Необходимо создать пять методов: getName, getAge, getGroupNumber, setNameAge, setGroupNumber. 
# Метод getName нужен для получения данных об имени конкретного студента, метод getAge нужен для получения данных
# о возрасте конкретного студента, vетод setGroupNumberнужен для получения данных о номере группы конкретного студента.
# Метод SetNameAge позволяет изменить данные атрибутов установленных по умолчанию, 
# метод setGroupNumber позволяет изменить номер группы установленный по умолчанию. 
# В программе необходимо создать пять экземпляров класса Student, установить им разные имена, возраст и номер группы."""

class Student():

    def __init__(self, name = 'Ivan', groupnumber = '10A', age = 18):
        self.name = name
        self.groupnumber = groupnumber
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_groupnumber(self):
        return self.groupnumber

    def set_name_age(self, name, age):
        self.name = name
        self.age = age

    def set_groupnumber(self, groupnumber):
        self.groupnumber = groupnumber

    def print_details(self):
        print(f'Student {self.name} is {self.age} years old '
      f'and studies at {self.groupnumber} class')


student1 = Student()
student2 = Student()
student3 = Student()
student4 = Student()
student5 = Student()
# принтим для подтверждения, что по умолчанию имена Иван  и 18 лет и учится в 10А
Student.print_details(student1)
Student.print_details(student5)

print()
# создаем экземпляры класса Student
student1.set_name_age("Itachi", 11)
student1.set_groupnumber("6B")

student2.set_name_age("Kisame", 13)
student2.set_groupnumber("8D")

student3.set_name_age("Hakudzu", 14)
student3.set_groupnumber("9E")

student4.set_name_age("Daidara", 10)
student4.set_groupnumber("7B")

student5.set_name_age("Vovka", 13)
student5.set_groupnumber("8A")

# принтим результат
Student.print_details(student1)
Student.print_details(student2)
Student.print_details(student3)
Student.print_details(student4)
Student.print_details(student5)

print()
print("----------TASK 4 ------------------")



""" 4. Напишите программу с классом Math. Создайте два атрибута — a и b. 
Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание. 
При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.  """

class Math:

    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def addition(self):
        return self.a+self.b
    def multiplication(self):
        return self.a*self.b
    def division(self):
        return round((self.a/self.b), 2)
    def substraction(self):
        return self.a-self.b

my_number = Math(23, 12)
print(f'Numbers are {my_number.a} and {my_number.b}')
print('------------------------------')
print(f'Multiplication is {Math.multiplication(my_number)}')
print(f'Substraction is {Math.substraction(my_number)}')
print(f'Addition is {Math.addition(my_number)}')
print(f'Division {Math.division(my_number)}')
print()
print("----------TASK 5 ------------------")


""" 5.Напишите программу с классом Car. Создайте конструктор класса Car. 
Создайте атрибуты класса Car — color (цвет), type (тип), year (год). 
Напишите пять методов. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». 
Третий — присвоение автомобилю года выпуска.
Четвертый метод — присвоение автомобилю типа. 
Пятый — присвоение автомобилю цвета.       """

class Car:

    def __init__(self, colour = None, model = None, year = None):
        self.colour = colour
        self.model = model
        self.year = year

    def start_engine(self):
        print("Кчау")
        time.sleep(1)
        print("Макуин Готов")

    def stop_engine(self):
        stop_engine = input("Выключить двигатель? ... да/нет: ")
        if stop_engine.lower() == "да":
            time.sleep(1)
            print("Заглох")
        else:
            print("Тоби пизда,ты позэлениу")

    def set_year(self, year):
        self.year = year

    def set_type(self, model):
        self.model = model

    def set_colour(self, colour):
        self.colour = colour

    def print_details(self):
        print(f'Ваш автомобиль:\n'
              f'Тип: {self.model}\n'
              f'Год: {self.year}\n'
              f'Цвет: {self.colour}')

my_car = Car()
my_car.start_engine()
my_car.stop_engine()
my_car.set_type("Масл")
my_car.set_colour("Бамблби")
my_car.set_year(1997)
my_car.print_details()
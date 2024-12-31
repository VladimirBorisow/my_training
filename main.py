from datetime import datetime
# "Hello world"
print("Hello world")
print(5)
print(type(50)) # класс «int» сокращение от англ. «integer», что переводится, как «целое число»
print(11 % 3) #  найти остаток от деления
print(5 ** 6) # Возведение в степень
print(2.35, type(2.35)) # к типу «float», что переводится, как числа с плавающей точкой
print('name', type('name')) # class 'str' - сокращением от англ. «string», то есть «строка», строки пишутся в кавычках
print('Hello,' + 'world!') # над строками возможно только сложение, не воспринимает операции с разными типами данных
print('1' + '5') # не воспринимает операции с разными типами данных
print(True, False) # Логический тип данных (boolean) может принимать два значения – True и False, то есть верно и неверно
print(5 > 10) # bool
print(5 > 10, 10 > 5) # bool
print(5 >= 10, 10 >= 5) #  больше или равно и меньше или равно
print(5 != 10, 10 == 10) #  "==" равенство объектов, и «!=» неравенство объектов
print(5 > 6 and 10 < 11) # and, чтобы получить «True», должны быть истинны оба выражения
print(5 > 6 or 10 < 11) # чтобы получить «True», or достаточно, чтобы истинным было хотя бы одно.
print(int('5')) # изменить один тип данных на другой, со строки на число
print(str(5)) # изменить один тип данных на другой, с числа на строку
print(type(int('5'))) # изменить один тип данных на другой, с определением типа данных
print(type(str(5))) # изменить один тип данных на другой, с определением типа

# "1st program" Арифметика
print((9 ** 0.5 * 5)) # возведение числа 9 в степень 0.5, после умножение на 5
# "2nd program" Логика
print(9.99 > 9.98, 1000 != 1000.1) # 9.99 больше 9.98 и 1000 не равно 1000.1
# "3rd program" Загадка
print(2 * 2 + 2) #  2 умноженное на 2 плюс 2
print(2 * (2 + 2)) # 2 умноженное на 2 плюс 2 с приоритетом для сложения
print((2 * 2 + 2) == (2 * (2 + 2))) # сравниваем выражения
print((2 * 2 + 2) != (2 * (2 + 2))) # сравниваем выражения
# "4th program" Первый после точки
name1_ = '123.456'
print(name1_[- 3]) # Вывести на экран первую цифру после запятой - 4
print(float(name1_)) # преобразовал из стр в число с плавающей
print(int(float(name1_))) # отделил целую часть
print(float(name1_) * 10) # сместил запятую на один знак
print(float(name1_) // 10) # остаточное деление
print((float(name1_) * 10) // 10) # остаточное деление

name = 'Urban'
print(name, type(name)) # class 'str'
name = 5 # целочисленное число
print(name, type(name))
name = 5.5 # число с плавающей точкой
print(name, type(name))
name = [1, 2, 3, 4]
print(name, type(name))

'module_1_3.py'
name = 'Vladimir'
print(name, type(name))
name = 60
print(name, type(name))
name = 60.5
print(name, type(name))
age = '60'
print(age, type(age))
nev_age = '60'
print(age + nev_age)
age = 60
nev_age = 60.5
print(type(True), type(False)) # Правда, Лож
is_student = True
print(is_student, type(is_student))
print(age + is_student)
print(nev_age + is_student)

well_name = 'Python'
home_work = 12
hour_spent = 1, 5
print(12 // 1, 5) # целочисленное деление
print('Курс:', well_name, ',' 'использовано часов =', home_work, ',''на одно задание потрачено:', hour_spent,
      ',интенсивность:', 12 / 1.5)

# Правильно:

if 'x' == 1:
    print("x is 1")

# Правильно:

long_string = "This is a really long string that " \
              "spans multiple lines."

# Правильно:
x = 2 + 3
print(x)
y = (1 + 2) * 3
print(y)

age = 25
naumbers: "John"

example = 'Abracodabra'
print('Abracodabra'[0])
print('Abracodabra'[- 1]) # первый символ этой строки
print('Abracodabra'[- 11], 'Abracodabra'[- 9], 'Abracodabra'[- 7],\
      'Abracodabra'[- 5], 'Abracodabra'[- 3], 'Abracodabra'[- 1])
print('Abracodabra'[- 1], 'Abracodabra'[- 3], 'Abracodabra'[- 5],\
      'Abracodabra'[- 7], 'Abracodabra'[- 9], 'Abracodabra'[- 11])
print('Abracodabra'[- 1], 'Abracodabra'[- 2], 'Abracodabra'[- 3],\
      'Abracodabra'[- 4], 'Abracodabra'[- 5], 'Abracodabra'[- 6],\
      'Abracodabra'[- 7], 'Abracodabra'[- 8], 'Abracodabra'[- 9],\
      'Abracodabra'[- 10], 'Abracodabra'[- 11])
print('Abracodabra'[0:4]) # чтобы взять первые 4 символа в строке нужно написать stroka[0:4]
print('Abracodabra'[4:11])
print('Abracodabra'[::-1]) # если все слово целиком с конца в начало то stroka[: : -1]
print('Abracodabra'[::-5])
print('Abracodabra'[::-8])

#name = input("Введите Ваше имя: ")
#current_year = 2024
#date_of_birth = int(input("В каком году Вы родились? "))
#age = current_year - int(date_of_birth)
#print(type(name))
#print('Здавствуйте,', name)
#print('В этом году Вам' ,age, 'лет' )
print('привет,я строка в нижнем регистре')
print('привет,я строка в нижнем регистре'.upper())
print('привет,я строка в нижнем регистре'.upper().lower())
print('привет,я строка в нижнем регистре'.replace('привет', 'пока'))
print('привет,я строка в нижнем регистре'.replace(' ', '#'))
print('привет,я строка в нижнем регистре'.replace(' ', ''))

# 'module_1_4.py'
my_string = 'Они представляют собой'
print(my_string)
print(my_string.upper())
print(my_string.upper().lower())
print(my_string.upper().lower())
print(my_string.replace('Они', 'Все'))
print(my_string.replace(' ', '&'))
print(my_string.replace(' ', ''))
print(my_string[0])
print(my_string[21])
print(my_string[8],my_string[15])

tuple_ = 1, 2, 3, 4, 5
tuple_2 = (1, 2, 3, 4, 5)
tuple_3 = tuple([1, 2, 3, 4, 5])
print(tuple_)
print(tuple_2)
print(tuple_3)
print(type(tuple_3))

tuple_ = 1, 2, 3, True, 'String'
list_ = [1, 2, 3, True, 'String']
print(tuple_)
print(tuple_[4])
print(tuple_.__sizeof__()) # определяет объем памяти
print(list_.__sizeof__())

tuple_ = ([1, 2], 3, True, 'String')
print(tuple_)
tuple_ [0][0] = 8
print(tuple_)
tuple_ = ([1, 2], 3, True, 'String') + (4, 5)
print(tuple_)
tuple_ = ([1, 2], 3, True, 'String') * 4
print(tuple_)

food = ['apple', 'coconut', 'banana']
food.append(True)
print(food)
food.extend(['Kobucc', 11])
print(food)
food.extend('Kobucc')
print(food)
food.remove('apple')
print(food)
print(food[1:4])
print(food[1:2:4])

# 'module_1_5.py'
immutable_var = 1, 2, 3, 4, 5
mutable_list = (1, 2, 3, True, 'String')
immutable_var_3 = tuple([1, 2, 3, 4, 'bukka'])
print(immutable_var)
print(mutable_list)
print(immutable_var_3)
print(type(immutable_var_3))
immutable_var_4 = [1, 2, 3, 4, 'bukka']
print(immutable_var_3)
print(immutable_var_3[4])
print(immutable_var_3.__sizeof__())
print(immutable_var_4.__sizeof__())

phone_book = {'Vladimir': 8987321654, 'Max': 1234987} # словари
print(phone_book)
print(phone_book ['Vladimir'])
phone_book['Vladimir'] = 1234589 # заменяем значение ключа
print(phone_book ['Vladimir'])
phone_book['Kuzma'] = 987654 # обращаемся к несуществующему ключу он его добавляет
print(phone_book ['Vladimir'])
print(phone_book)
del phone_book['Max'] # удаление значения по ключу
print(phone_book)
phone_book.update({'Saha': 8987321654,
                   'Alexs': 1234987}) # обновление пары ключ-значение
print(phone_book)
print(phone_book.get('Vladimir')) # возвращает значение по указанному ключу
print(phone_book.get('Kamilla', 'Такого ключа нет'))
a = phone_book.pop('Kuzma') # удаляет указанный ключ и возвращает значение
print(phone_book)
print(a)
list_ = [1, 2, 3, 5, 9]
list_.pop(3)
print(list_)
print(phone_book.keys()) # позволит нам получить коллекцию ключей в нашем словаре
print(phone_book.values()) # будет возвращать значения из нашего словаря
print(phone_book.items()) # будет возвращать значения из нашего словаря
phone_book = {'Vladimir': [8987321654, 12345], 'Max': 1234987}
print(phone_book)
set_ = {1, 2, 9, 1, 4, 5, 9, 18, 7, 4, 'String', True, (1, 2, 3)} # множества хранят уникальные значения
list_ = [1, 2, 1, 4, 2, 3, 5, 9]
print(list_)
print(set_)
print(set(list_)) # получить множество из списка
list_ = set(list_) # заменить список полностью
print(list_)
print(list_.discard(9)) #  удалить какой-либо элемент
print(list_)
print(list_.remove(1)) #
print(list_)
print(list_.add(16))
print(list_)

# module_1_6.py
my_dict = {'Vladimir': 1964, 'Max': 1967, 'Sveta': 1568} # словари
print(my_dict)
print(my_dict ['Vladimir'])
my_dict['Vladimir'] = 2024 # заменяем значение ключа
print(my_dict ['Vladimir'])
my_dict['Kuzma'] = 1978 # обращаемся к несуществующему ключу он его добавляет
print(my_dict ['Vladimir'])
print(my_dict)
del my_dict['Max'] # удаление значения по ключу
print(my_dict)
my_dict.update({'Saha': 1458,
                   'Alexs': 2245}) # обновление пары ключ-значение
print(my_dict)
print(my_dict.get('Vladimir')) # возвращает значение по указанному ключу
print(my_dict.get('Karina', 'Такого ключа нет'))
a = my_dict.pop('Kuzma') # удаляет указанный ключ и возвращает значение
print(my_dict)
print(a)
list_ = [1, 2, 3, 5, 9]
list_.pop(3)
print(list_)
print(my_dict.keys()) # позволит нам получить коллекцию ключей в нашем словаре
print(my_dict.values()) # будет возвращать значения из нашего словаря
print(my_dict.items()) # будет возвращать значения из нашего словаря
my_dict = {'Vladimir': [8987321654, 12345], 'Max': 1234987}
print(my_dict)
my_set = {1, 2, 9, 1, 4, 5, 9, 18, 7, 4, 258.25, 'String', True, (1, 2, 3)} # множества хранят уникальные значения
list_ = [1, 2, 1, 4, 2, 3, 5, 9]
print(my_set)
print(set(my_set)) # получить множество из списка
my_set = set(my_set) # заменить список полностью
print(my_set)
print(my_set.discard(9)) #  удалить какой-либо элемент
print(my_set)
print(my_set.remove(2)) #
print(my_set)
print(my_set.add(16))
print(my_set)

#  'Itog po vvodomu kursu' "Средний балл"
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
slovar = {'Johnny': [5, 3, 3, 5, 4], 'Bilbo': [2, 2, 2, 3], 'Steve': [4, 5, 5, 2],
          'Khendrik': [4, 4, 3], 'Aaron': [5, 5, 5, 4, 5]}
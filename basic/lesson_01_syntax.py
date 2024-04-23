''' Reference Model of Data '''











'''  cascading assignment,  multiple purpose'''

x = z = y = 0



''' Tuple Assignment '''

a, b, c, = 1, 2, 3



''' immutable data types 

1) Неизменяемые типы данных
- Числовые (int, float, complex);
- Логический (bool)
- Строки (str) нельзя менять отдельные буквы в строке — только создав новую строку;
- Кортеж (tuple) не позволяет изменять набор, но может содержать изменяемые элементы;
- Замороженное множество (frozenset);
- Функции имя функции также является переменной, и может быть переопределено.
- Классы но не экземпляры классов

2) Изменяемые типы данных
- Список (list) — последовательность любых элементов
- Множество (set) — неповторяющийся набор неизменяемых элементов
- Словарь (dict) — таблица соответствия ключ → значение. Ключ обязательно неизменяемый, значение любое.

Для определения типа переменной (например x), использовать функцию type. Для проверти типа — используется оператор is.

type(x) is int.

'''


''' control constructs in python 
                while
before ///
while (condition):
    operator1
    operator2
    .........
    operator n
after ////

- Заголовок цикла (while, for)
- Условие (n < 10)
- Тело цикла
- итерация цикла

примеры:
'''

i = 0
while (i < 10):
    print(f"i = {i}")
    i += 1 

x = 0
while (x < 5):
    print(x)
    x += 1
else:
    print("Цикл завершён!")

start = int(input("Введите стартовое число: "))
step =  int(input("Введите шаг: "))
stop = int(input("Введите числовое значние кнопки стоп: "))
x = start

while (x < stop):
    print(f"x = {x}")
    x += step

'''
            for

'''

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

message = "Hello, World!"
for char in message:
    print(char)

for i in range(1, 6):
    print(i)

#1.Преобразование списка чисел в список их квадратов
numbers = [10, 25, 32, 64]

squared_numbers = []
for num in numbers:
    squared_numbers.append(num ** 2)

print(squared_numbers)

#2.Генераторы: Генератор для создания списка квадратов чисел
numbers = [10, 25, 32, 64]

squared_numbers = (num ** 2 for num in numbers)
for squared_num in squared_numbers:
    print(squared_num)

#3.Распаковка кортежей: Итерация по списку кортежей и распаковка их элементов
coordinates = [(1, 2), (3, 4), (5, 6)]

for x, y in coordinates:
    print(f"X: {x}, {y}")
'''
Вывод:
X: 1, Y: 2
X: 3, Y: 4
X: 5, Y: 6
'''

#4.Комбинация с условиями
number = [25, 24, 12, 31, 44]
print(f"В массиве {number} список чётных/нечёных чисел:")

for num in number:
    if num % 2 == 0:
        print(f"Чётное число: {num}")
    else:
        print(f"Число нечётное: {num}")

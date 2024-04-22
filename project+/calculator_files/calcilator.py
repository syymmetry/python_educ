import math

def main():
    while True:
        print("Добро пожаловать!")
        print("Пожалуйста, выбирете операцию:")
        print("1. Стандартный калькулятор")
        print("2. Инженерный калькулятор")
        print("3. Таблица умножения")
        print("4. Калькулятор дробей")
        print("5. ВЫход из программы")

        choice = input("Ваш выбор: ")

        if choice == '1':
            calculator()
        elif choice == '2':
            ingeneer_calc()
        elif choice == '3':
            number = int(input("Введите число для таблицы умножения: "))
            print(f"Таблица умножения для числа {number}:")
            multiplicationTable(number)
            print("Выйти в меню (m), выйти из программы (e)")
            menu_end = input(" m/e: ")
            if (menu_end == "m"):
                continue
            elif (menu_end == "e"):
                break 
        elif choice == '5':
            print("Выход из программы")
            break
        else:
            print("Неверная операция")

def calculator():
    while True:
        operation = input("Введите операцию (+, -, *, /): ")

        if operation not in ['+', '-', '*', '/']:
            print("Неверная операция")
            continue

        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка ввода!ПОжалуйста, введите числовое значение!")
            continue

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Деление на ноль невозможно!")
                continue
            else:
                result = num1 / num2
        print(f"Результат: {result}")

        choice = input("Выполнить ещё одну операцию? (y/n): ").lower()
        if choice != 'y':
            break

def multiplicationTable(number):
    
    for i in range(1, 11):
        result = number * i 
        print(f"{number} * {i} = {result}")


def sin(x):
    x_rad = math.radians(x)
    result = 0
    for n in range(10):
        result += ((-1) ** n) * (x_rad ** (2 * n + 1)) / factorial(2 * n + 1)
    return result

def cos(x):
    x_rad = math.radians(x)
    result = 0
    for n in range(10):
        result += ((-1) ** n) * (x_rad ** (2 * n)) / factorial(2 * n)
    return result

def tan(x):
    x_rad = math.radians(x)
    return sin(x_rad) / cos(x_rad)

def ctg(x):
    x_rad = math.radians(x)
    return cos(x_rad) / sin(x_rad)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def ingeneer_calc():
    while True:
        print("Введите операцию: ")
        print("1. Sin")   
        print("2. Cos")   
        print("3. Tan")
        print("4. Ctg")
        print("5. Назад")

        choice = input("Ваш выбор: ")

        if choice == '1':
            calculate_trig_function(sin, "sin")
        elif choice == '2':
            calculate_trig_function(cos, "cos")
        elif choice == '3':
            calculate_trig_function(tan, "tan")
        elif choice == '4':
            calculate_trig_function(ctg, "ctg")
        elif choice == '5':
            print("Возврат к предыдущему меню...")
            break
        else:
            print("Неверная операция!")

def calculate_trig_function(func, func_name):
    try:
        angle = float(input(f"Введите угол в градусах для функции {func_name}: "))
        result = func(angle)
        print(f"{func_name}({angle} градусов) = {result}")
    except ValueError:
        print("Ошибка ввода! Пожалуйста, введите числовое значние!")


if __name__ == "__main__":
    main()
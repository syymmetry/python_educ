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
    result = 0

    for n in range(10):
        result += ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n)

    return result



def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def ingeneer_calc():    



if __name__ == "__main__":
    main()
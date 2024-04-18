def multiplicationTable(number):
    for i in range(1, 11):
        result_match = number * i
        print(f"{number} * {i} = {result_match}")

def calculator():
    while True:
        operation = input("Введите операцию: (+, -, *, /): ")

        if operation not in ['+', '-', '*', '/']:
            print("Неверно введена операция!")
            continue

        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Деление на ноль невозможно!")
                continue

        print(result)

        choice = input("Хотите выполнять ещё одну операцию? (y/n): ")
        if choice.lower() != 'y':
            break

# Пример использования функции калькулятора
calculator()

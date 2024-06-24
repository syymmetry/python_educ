def find_square_root(num):

    number = float(input("Введите число для нахождения квадратного корня: "))
    result = find_square_root(number)
    print(f"Квадратный корень числа {number} равен {result}")



    if num < 0:
        return "Невозможно найти корень отрицательного числа!"


    if num == 0:
        return 0
    
    x = num / 2

    while True:
        new_x = 0.5 * (x + num / x)
        if abs(x - new_x) < 0.00001:
            break

        x = new_x

    return  new_x

print("КАЛЬКУЛЯТОР")
a = int(input("Введите первое число: "))

while(True):
    try:
        b = int(input("Введите второе число: "))
        print("Что вы хотите с ним сделать?")
        print("1. Сложить")
        print("2. Вычесть")
        print("3. Умножить")
        print("4. Разделить")
        print("5. Возведение в степень")
        print("6. Остаток от деления")
        print("Введите код действия:")
        c = input()

        print("Итог: ")
        match c:
            case '1':
                a = a + b
                print(a)
            case '2':
                a = a - b
                print(a)
            case '3':
                a = a * b
                print(a)
            case '4':
                if b == 0:
                    print("На 0 делить нельзя")
                else:
                    a = a / b
                    print(a)
            case '5':
                a = a ** b
                print(a)
            case '6':
                a = a % b
                print(a)
            case _:
                print("Необходимо ввести цифру, соответсвующую какой-либо операции")
    except:
        print("Произошла какая-то ошибка(")



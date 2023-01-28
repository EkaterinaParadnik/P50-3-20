while(True):
    print()
    try:
        nums = int(input("Введите количество чисел:\n"))
        if nums < 2:
            print("Калькулятор обрабатывает минимум 2 числа!")
        if nums == 2:
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
            print()
            func = int(input('''Выберите функцию:
            1 Сложение
            2 Вычитание
            3 Деление
            4 Умножение
            '''))
            if func == 1:
                print(x+y)
            if func == 2:
                print(x-y)
            if func == 3:
                print(x/y)
            if func == 4:
                print(x*y)
        if nums == 3:
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
            z = float(input("Введите третье число: "))
            print()
            func = int(input('''Выберите функцию:
            1 Сложение
            2 Вычитание
            3 Деление
            4 Умножение
            '''))
            if func == 1:
                print(x+y+z)
            if func == 2:
                print(x-y-z)
            if func == 3:
                print(x/y/z)
            if func == 4:
                print(x*y*z)
        if nums == 4:
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
            z = float(input("Введите третье число: "))
            w = float(input("Введите четвёртое число: "))
            print()
            func = int(input('''Выберите функцию:
            1 Сложение
            2 Вычитание
            3 Деление
            4 Умножение
            '''))
            if func == 1:
                print(x+y+z+w)
            if func == 2:
                print(x-y-z-w)
            if func == 3:
                print(x/y/z/w)
            if func == 4:
                print(x*y*z*w)
        if nums == 5:
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
            z = float(input("Введите третье число: "))
            w = float(input("Введите четвёртое число: "))
            v = float(input("Введите пятое число: "))
            print()
            func = int(input('''Выберите функцию:
            1 Сложение
            2 Вычитание
            3 Деление
            4 Умножение
            '''))
            if func == 1:
                print(x+y+z+w+v)
            if func == 2:
                print(x-y-z-w-v)
            if func == 3:
                print(x/y/z/w/v)
            if func == 4:
                print(x*y*z*w*v)
        if nums > 5:
            print("Калькулятор обрабатывает максимум 5 чисел!")
    except(ZeroDivisionError):
        print("Нельзя делить на ноль!")
    except(ValueError):
        print("Проверьте ввод.")
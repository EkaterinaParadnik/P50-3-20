while True:
    print ('Калькулятор')
    result = 0
    kol = int (input('Количество: '))
    while kol!=0:
        vvod = int (input('Введите число '))
        v = int (input('Какую операцию вы хотите выполнить? \n 1 Сложение \n 2 Вычитание \n 3 Деление \n 4 Умножение \n 5 Степень \n'))
        if v == 1:
            result = result + vvod
            p = 'Сложение'
            deystvie = p
            kol -=1
            print ('Результат ',deystvie,' = ',result)
        if v == 2:
            result = result - vvod
            l = 'Вычитание'
            deystvie = l
            kol -=1
            print ('Результат ',deystvie,' = ',result)
        if v == 3:
            if vvod != 0:
                result = result / vvod
                c = 'Деление'
                deystvie = c
                kol -=1
                print ('Результат ',deystvie,' = ',result)
            else:
                print("Деление на ноль!")
        if v == 4:
            result = result * vvod
            n = 'Умножение'
            deystvie = n
            kol -=1
            print ('Результат ',deystvie,' = ',result)
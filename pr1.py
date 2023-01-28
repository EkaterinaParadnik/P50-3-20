print("Калькулятор")
while True:
        print("Выберите действие, которое хотите выполнить:\n"
              "Сложение: +\n"
              "Вычетание: -\n"
              "Умножение: *\n"
              "Деление: /\n"
              "Степень: ^\n"
              "Выход: a\n")
        action = input("Действие: ")
        if action == "a":
            print("Выход из программы")
            break
        if action in ('+', '-', '*', '/', '^'):
            x = float(input("x = "))
            y = float(input("y = "))
            if action == '+':
                print('%.2f + %.2f = %.2f' % (x, y, x+y))
            elif action == '-':
                print('%.2f - %.2f = %.2f' % (x, y, x-y))
            elif action == '*':
                print('%.2f * %.2f = %.2f' % (x, y, x*y))
            elif action == '/':
                if y != 0:
                    print('%.2f / %.2f = %.2f' % (x, y, x/y))
                else:
                    print("Деление на ноль!")
            elif action == '^':
                print('%.2f pow %.2f = %.2f' % (x, y, pow(x,y)))
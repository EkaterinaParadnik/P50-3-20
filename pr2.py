import calendar
print ("Подсчёт суммы дат года")
while(True):
    god = int(input("Введите год: "))
    data = 0
    summa = 0
    while data != 28:
        data += 1
        chislo = sum(map(int, list(str(data))))
        summa = summa + chislo
    nevisokosny = (summa + (summa + 14) * 4 + (summa + 18) * 7)
    visokosny = ((summa + 11) + (summa + 14) * 4 + (summa + 18) * 7)
    if calendar.isleap (god):
        print ("Високосный - ", visokosny)
    else:
        print ("Невисокосный - ", nevisokosny)
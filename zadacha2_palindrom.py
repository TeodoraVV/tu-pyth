# Задача 2: Проверка дали число е палиндром

def e_palindrom(chislo):
    """Връща 1, ако числото е палиндром, и 0, ако не е."""
    original = chislo        # запазваме първоначалното число за сравнение
    n = original
    obarnato = 0

    # Обръщаме числото цифра по цифра
    while n > 0:
        cifra = n % 10                    # последната цифра
        obarnato = obarnato * 10 + cifra  # добавяме я отзад към обърнатото
        n = n // 10                       # махаме последната цифра

    if obarnato == original:
        return 1
    else:
        return 0


chislo = int(input("Въведете цяло число: "))
print(e_palindrom(chislo))

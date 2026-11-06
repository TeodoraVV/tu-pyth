# Задача 1: Лице на геометрична фигура (всичко в една функция)

def lice(izbor):
    """Пресмята лицето на фигурата според избраното число."""
    if izbor == 1:
        a = float(input("Въведете страната a: "))
        return a * a                    # квадрат: S = a * a
    elif izbor == 2:
        a = float(input("Въведете страната a: "))
        b = float(input("Въведете страната b: "))
        return a * b                    # правоъгълник: S = a * b
    elif izbor == 3:
        a = float(input("Въведете първия катет a: "))
        b = float(input("Въведете втория катет b: "))
        return (a * b) / 2              # прав. триъгълник: S = (a * b) / 2
    else:
        return None                     # невалиден избор


print("Изберете фигура:")
print("1 - квадрат")
print("2 - правоъгълник")
print("3 - правоъгълен триъгълник")
izbor = int(input("Вашият избор: "))

rezultat = lice(izbor)

if rezultat is None:
    print("Невалиден избор!")
else:
    print("Лицето е:", rezultat)

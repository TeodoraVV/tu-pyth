# Задача 3: Калкулатор за цели числа (всичко в една функция)

def kalkulator(operacia, a, b):
    """Изпълнява избраната операция върху a и b и връща резултата."""
    if operacia == "+":
        return a + b
    elif operacia == "-":
        return a - b
    elif operacia == "*":
        return a * b
    elif operacia == "/":
        if b == 0:
            return "Грешка: деление на нула!"
        return a // b               # целочислено деление
    else:
        return "Невалидна операция!"


operacia = input("Въведете операция (+, -, *, /): ")
a = int(input("Въведете първото число: "))
b = int(input("Въведете второто число: "))

print("Резултат:", kalkulator(operacia, a, b))

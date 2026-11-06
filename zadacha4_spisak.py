# Задача 4: Замяна на елементите, по-големи от дадено число, с 0

def zamesti_s_nula(spisak, chislo):
    """Променя всички елементи на списъка, по-големи от chislo, на 0."""
    for i in range(len(spisak)):
        if spisak[i] > chislo:
            spisak[i] = 0
    return spisak


elementi = input("Въведете числата от списъка, разделени с интервал: ")
spisak = [int(x) for x in elementi.split()]
chislo = int(input("Въведете числото: "))

print("Списък преди:", spisak)
zamesti_s_nula(spisak, chislo)
print("Списък след: ", spisak)

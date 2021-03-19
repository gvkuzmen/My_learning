#1.3 Функции и стек вызовов


def closest_mod_5 (x):
    while x % 5 != 0:
        x += 1
    return x

print(closest_mod_5(10))



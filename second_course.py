#1.2 Модель данных: объекты
Реализуйте программу, которая будет вычислять количество различных объектов в списке.
Два объекта a и b считаются различными, если a is b равно False.

Вашей программе доступна переменная с названием objects, которая ссылается на список, содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.



objects = [1, 2, 1, 2, 3]
ans = 0
total = []
for obj in objects: # доступная переменная objects
    if obj not in total:
        total.append(obj)
        ans += 1
print(ans)

"""
Определите, можно ли от шоколадки размером a × b долек отломить c долек,
 если разрешается сделать один разлом по прямой между дольками
  (то есть разломить шоколадку на два прямоугольника).

Выведите yes или no соответственно.

Пример:

a, b, c = 3, 2, 4 -> yes
a, b, c = 3, 2, 1 -> no

При отправке кода на Выполнение раскомментируйте строку ниже, чтобы задать значения `a`, `b`, `c`

При отправке решения на Проверку закомментируйте эту строку обратно - система автоматически подставит разные значения `a`, `b`, `c` для проверки
"""
a = 3
b = 2
c = 4
# Введите ваше решение ниже

if ((a * b) - c) % 2 == 0:
    print("Yes")
else:
    print("No")
#Реализуйте рекурсивную функцию нарезания прямоугольника
# с заданными пользователем сторонами a и b на квадраты
# с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и
# кол-во полученных квадратов.

def rec(a, b):
    if a > b :
        print(str(b) + " = b")
        return rec(a - b, b) + rec(a, a)
    elif a < b :
        print(str(a) + " = a")
        return rec(b - a, a) + rec(b, b)
    elif a == b:
        #print(str(a))
        return 1

a = int(input('Введите сторону прямоугольника А : '))
b = int(input('Введите сторону прямоугольника В : '))
print("количество квадратов =", rec(a, b))
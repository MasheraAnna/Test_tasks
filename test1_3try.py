'''
1. Расставьте знаки + между некоторыми цифрами числа 12345678910111213...N, чтобы в сумме получилось число M.
На вход получаем два натуральных числа N и M.
Вывод: верные примеры в строку.

Примеры:
1)Ввод: 5 15
Вывод: 1+2+3+4+5=15
2)Ввод: 4 46
Вывод: 12+34=46


Введите максимльное число N последовательности: 10
Введите число M, которое необходимо получить в качестве ответа: 46


'''


# Теперь попробуем исправить решение с рекурсией:


def sum_of(solution):
    running_number = 0
    sum = 0

    for n in solution:
        if n == "+":
            sum += running_number
            running_number = 0
        else:
            running_number *= 10
            running_number += int(n)

    sum += running_number

    return sum


def input_array(max_number):
    i = 1
    while i < max_number + 1:
        s = str(i)
        for c in s:
            yield c
        i += 1


def plusik_moves(tail):
    if not tail:
        return [""]

    return [
        str(tail[0]) + t for t in plusik_moves(tail[1:])
    ] + [
        str(tail[0]) + "+" + t for t in plusik_moves(tail[1:]) if t
    ]

def test_solutions(solutions, sum):
    for solution in solutions:
        list_x = list(solution)
        eq = "".join(list_x)

        if sum == sum_of(list_x):
            print("Solution found!", eq + " = " + str(sum))


def test(K, sum):
    solutions = plusik_moves(list(input_array(K)))

    test_solutions(solutions, sum)


"""
test(5, 1+2+3+4+5)
test(5, 12345)
test(5, 12+34+5)
test(10, 1+2+3+4+5+678910)
test(10, 1+2+3+4+5+67+8+910)
test(10, 12345678910)
test(10, 12+34+56+78+91+0)
test(10, 46)
test(15, 120)
"""

n = int(input("Введите максимльное число N последовательности: "))
m = int(input("Введите число M, которое необходимо получить в качестве ответа: "))
test(n, m)

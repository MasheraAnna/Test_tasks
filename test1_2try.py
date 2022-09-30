"""
Примеры:
1)Ввод: 5 15
Вывод: 1+2+3+4+5=15
2)Ввод: 4 46
Вывод: 12+34=46


Введите максимльное число N последовательности: 10
Введите число M, которое необходимо получить в качестве ответа: 46
"""

from typing import List
import numpy as np
import itertools

""" если посмотреть пристально на задачку, то можно заметить, что мы не плюсики расставляем между числами, а 0 и 1 в матрице перестановок.
как сгенерировать такую матрицу, содержащую все возможные перестановки 0 и 1 в векторе, размерностью N - гуглится очень быстро.
на этой идее основано решение"""



def input_array(max_number) -> List[int]:
    i = 1
    while i < max_number + 1:
        s = str(i)
        for c in s:
            yield c
        i += 1

def masks(K):
    for i in itertools.product([0, 1], repeat = K*1):
        yield np.reshape(np.array(i), (K, 1)).flatten()


def plusik_moves(max_number, solution):
    print(f"Searching for solution: {solution}")
    numbers = list(input_array(max_number))
    pluses = masks(len(numbers)-1)

    for mask in pluses:
        eq = ""
        sum = 0
        running_number = 0

        for i, n in enumerate(numbers):
            op = mask[i-1]

            if op:
                sum += running_number
                running_number = int(n)

                eq += (" + " if eq else "") + n
            else:
                running_number *= 10
                running_number += int(n)

                eq += n

        sum += running_number

        if sum == solution:
            print(f"Found solution: {eq} == {solution}")


n = int(input("Введите максимльное число N последовательности: "))
m = int(input("Введите число M, которое необходимо получить в качестве ответа: "))
plusik_moves(n, m)

"""
tests:

plusik_moves(5, 1+2+3+4+5)
plusik_moves(5, 12345)
plusik_moves(5, 12+34+5)
plusik_moves(10, 1+2+3+4+5+678910)
plusik_moves(10, 1+2+3+4+5+67+8+910)
plusik_moves(10, 12345678910)
plusik_moves(10, 12+34+56+78+91+0)
plusik_moves(10, 46)
plusik_moves(15, 120)

"""
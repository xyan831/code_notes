# math2: maximum minimum and factor
# zio800

from math import *


# maximum and minimum
def maxmin(lst):
    nummax = lst[0]
    nummin = lst[0]
    for item in lst:
        if item < nummin:
            nummin = item
        if item > nummax:
            nummax = item
    print('max = ', nummax, ', min = ', nummin)


# multiples of number in range
def factor(fac, first, last):
    multiple = []
    for item in range(first, last):
        if item % fac == 0:
            multiple.append(item)
    print('number of multiples = ', len(multiple))
    print('multiples: ', multiple)
    print('sum of multiples = ', sum(multiple))


# calculate
factor(9, 1, 100)

lst1 = [1, 2, 3, 4, 5]
maxmin(lst1)

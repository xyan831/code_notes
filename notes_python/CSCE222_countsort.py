# CSCE 222 counting and sorting
# Xiaochen Yan UIN: 327002462

# import module
from math import factorial, floor

# n=elements, r=permutation/combination
# permutation: P(n, r) = n! / [(n-r)!]
def P(n, r):
	return factorial(n) / factorial(n-r)
# permutation+repetition: PR(n, r) = n^r
def PR(n, r):
	return n**r
# combination: C(n, r) = n! / [r! * (n-r)!]
def C(n, r):
	return factorial(n) / (factorial(r)*factorial(n-r))
# combination+repetition: CR(n, r) = C(n-1+r, r) = (n-1+r)! / [r! * (n-1)!]
def CR(n, r):
	return factorial(n-1+r) / (factorial(r)*factorial(n-1))

# binomial theorum
# (r*x + s*y)^n = (j=0, j=n)∑{C(n, j) * [(r*x)^(n-j) * (s*y)^j]}
# coefficient of (x^a)*(y^b) in (r*x + s*y)^c is C(c, b)*(r^a)*(s*b)
def BT(r, s, a, b, c):
	return C(c, b)*(r**a)*(s**b)

# max-finding algorithm
def getMax(a):
  max = a[0]
  for i in range(len(a)):
    if max < a[i]:
      max = a[i]
    return max
# linear search algorithm
def LinGetNum(a, x):
  i = 0
  while (i<len(a) and x!=a[i]):
    i+=1
  if i<len(a):
    return i
  else:
    return -1
# binary search algorithm (input must be sorted)
def BinGetNum(a, x):
  left = 0
  right = len(a)-1
  while (left<right):
    mid = floor((left+right)/2)
    if x>a[mid]:
      left = mid+1
    elif x<a[mid]:
      right = mid-1
    elif x==a[mid]:
      return mid
  return -1
# bubble sort algorithm
def bubbleSort(a):
  for i in range(0, len(a)-2):
    for j in range(0, len(a)-i-1):
      if (a[j]>a[j+1]):
        temp = a[j]
        a[j] = a[j+1]
        a[j+1] = temp
        #print(a)
  return a
# insertion sort algorithm
def insertionSort(a):
  for i in range(1, len(a)):
    m = a[i]
    j = i-1
    while (j>=0 and m<a[j]):
      a[j+1] = a[j]
      j-=1
    a[j+1] = m
    #print(a)
  return a

# calculator
print(C(5, 2))
a = [45, 23, 26, 44, 55, 32, 10, 84]
print(f'maximum = {getMax(a)}')
print(f'linear: index = {LinGetNum(a, 3)}')
print(f'bubble sort: {bubbleSort(a)}')
print(f'insertion sort: {insertionSort(a)}')
print(f'binary: index = {BinGetNum(a, 3)}')

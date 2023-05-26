# import numpy

# def average(num):
#     if num < 0:
#         n = int(num) - 0.5
#         if num >= n:
#             return int(num)
#         else:
#             return int(num) - 1
#     else:
#         n = int(num) + 0.5
#         if num >= n:
#             return int(num) + 1
#         else:
#             return int(num)


# N = int(input())
# arr = [int(input()) for i in range(N)]
# halb = N//2

# arr.sort()

# idxArr = [arr.count(arr[i]) for i in range(len(arr))]
# idxArr = numpy.array(idxArr)
# idxArr = numpy.where(idxArr == max(idxArr))[0]
# keyArr = [arr[i] for i in idxArr]
# keyArr = list(set(keyArr))
# keyArr.sort()

# print('---')

# print(average(sum(arr)/N))
# print(arr[halb])
# if len(keyArr)==1:
#     print(keyArr[0])
# else:
#     print(keyArr[1])
# print(max(arr)-min(arr))


import sys


def average(num):
    if num < 0:
        n = int(num) - 0.5
        if num >= n:
            return int(num)
        else:
            return int(num) - 1
    else:
        n = int(num) + 0.5
        if num >= n:
            return int(num) + 1
        else:
            return int(num)


def merge(l, r):
    left = right = 0
    merged = []
    while len(l) > left and len(r) > right:
        if l[left] < r[right]:
            merged.append(l[left])
            left += 1
        else:
            merged.append(r[right])
            right += 1
    while len(l) > left:
        merged.append(l[left])
        left += 1
    while len(r) > right:
        merged.append(r[right])
        right += 1
    return merged

def divide(arr):
    if len(arr) <= 1:
        return arr
    m = len(arr)//2
    l = divide(arr[:m])
    r = divide(arr[m:])
    return merge(l, r)


def frequency(arr):
    dic = {}
    for value in arr:
        if value not in dic:
            dic[value] = arr.count(value)
    key = max(dic.values())
    temp = [k for k, v in dic.items() if v == key]
    if len(temp) == 1:
        return temp[0]
    else:
        return temp[1]


N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(N)]
arr = divide(arr)
m = len(arr)//2

print(average(sum(arr)/N))
print(arr[m])
print(frequency(arr))
print(max(arr)-min(arr))


# def frequency(arr):
#     cntArr = [arr.count(arr[i]) for i in range(len(arr))]
#     key=max(cntArr)
#     temp=[]
#     for i in range(len(cntArr)):
#         if key == cntArr[i] and arr[i] not in temp:
#             temp.append(arr[i])

#     if len(temp)==1:
#         return temp[0]
#     else:
#         return temp[1]


########################################

import sys


def average(num):
    if num < 0:
        n = int(num) - 0.5
        if num >= n:
            return int(num)
        else:
            return int(num) - 1
    else:
        n = int(num) + 0.5
        if num >= n:
            return int(num) + 1
        else:
            return int(num)

def frequency(arr):
    dic = {}
    for value in arr:
        if value not in dic:
            dic[value] = arr.count(value)
    key = max(dic.values())
    temp = [k for k, v in dic.items() if v == key]
    if len(temp) == 1:
        return temp[0]
    else:
        return temp[1]


N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(N)]
arr.sort()
m = len(arr)//2

print(average(sum(arr)/N))
print(arr[m])
print(frequency(arr))
print(max(arr)-min(arr))



import statistics
import sys
from collections import Counter

N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for i in range(N)]
fre= sorted(Counter(arr).items(), key=lambda x: (-x[1], x[0]))

print(round(statistics.mean(arr)))
print(statistics.median(arr))
if N ==1:
    print(arr[0])
else:
    if fre[0][1] == fre[1][1]:
        print(fre[1][0])
    else:
        print(fre[0][0])
print(max(arr)-min(arr))
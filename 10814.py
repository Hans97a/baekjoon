import sys

N=int(sys.stdin.readline())
arr=[ list(sys.stdin.readline().split()) for i in range(N)]
arr.sort(key= lambda x: int(x[0]))

for i in arr:
    for j in i:
        print(j, end=' ')
    print()

# import sys


# def merge(l, r):
#     temp = []
#     left = right = 0
#     while len(l) > left and len(r) > right:
#         if l[left][0] < r[right][0]:
#             temp.append(l[left])
#             left += 1
#         else:
#             temp.append(r[right])
#             right += 1
#     while len(l)>left:
#         temp.append(l[left])
#         left+=1
#     while len(r)>right:
#         temp.append(r[right])
#         right+=1
#     return temp


# def divide(arr):
#     if len(arr) == 1:
#         return arr
#     m = len(arr)//2
#     l = divide(arr[:m])
#     r = divide(arr[m:])
#     return merge(l, r)


# N = int(sys.stdin.readline())
# arr = [list(sys.stdin.readline().split()) for i in range(N)]

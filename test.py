import heapq

arr = [1, 3, 4, 53, 2, 3, 1, 2, 3, 4, 5, 6, 4, 2]

heapq.heapify(arr)

while arr:
    print(heapq.heappop(arr))

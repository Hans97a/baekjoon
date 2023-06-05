N = int(input())
books = dict()
for i in range(N):
    book = input()

    if book in books:
        books[book] += 1
    else:
        books[book] = 1
result = sorted(books.items(), key=lambda x: [-x[1], x[0]])
print(result)

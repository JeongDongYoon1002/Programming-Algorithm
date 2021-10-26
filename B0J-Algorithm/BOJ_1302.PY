n = int(input())
books = {}
for _ in range(n):
    book = input()
    if book not in books:
        books[book] = 1
    else:
        books[book] += 1
array =[]
array.append(books.keys())
print(array)

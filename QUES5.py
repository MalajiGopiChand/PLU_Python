# Insert New Book by Price
# A bookstore maintains a sorted list of book prices. A new book arrives, and its price needs to be placed at the correct position while keeping the list sorted. Write a program to perform this task

prices = []

n = int(input("Enter number of books: "))
for i in range(n):
    price = int(input("Enter price: "))
    prices.append(price)

new = int(input("Enter new book price: "))

prices.append(new)
prices.sort()

print("Updated Book Prices:",prices)
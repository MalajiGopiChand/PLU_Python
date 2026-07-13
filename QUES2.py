# Product ID Search
# An e-commerce website stores product IDs in ascending order. Write a program to find whether a customer-entered product ID exists in the inventory. If it exists, display its index; otherwise, display "Product Not Available"

products = [101,102,103,104,105,106,107,108,109,120]
search = int(input("Enter product ID: "))
low = 0
high =len(products)-1
while low <= high:
    mid = (low + high)//2
    if products[mid] == search:
        print("products ID found:", search)
        break
    elif products[mid] < search:
        low = mid + 1
    else: 
        high = mid - 1
else:
    print("product ID is not found")
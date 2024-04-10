import pickle

from product import Product

#name = input()
#cost = int(input())
#l, w, h = int(input()), int(input()), int(input())
#product1 = Product(name, cost, l, w, h)

products = [["шоколад", 25, 1, 2, 10], ["карамель", 10, 1, 1, 1]]
FILENAME = "data.bat"
with open(FILENAME, "wb") as file:
    pickle.dump(products, file)
products = []
with open(FILENAME, "rb") as file:
    prod_input = pickle.load(file)
    for prod in prod_input:
        products.append(Product(prod[0], prod[1], prod[2], prod[3], prod[4]))

file = open("data.txt", "r", encoding="utf-8")
content = file.readlines()
products2 = []
for line in content:
    line = line.strip().split()
    products2.append(Product(line[0], float(line[1]), int(line[2]), int(line[3]), int(line[4])))
print(*products)

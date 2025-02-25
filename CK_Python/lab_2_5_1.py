import os
files = os.listdir("example")
for file in files:
    file = file.replace(".txt", "")
string = input()
n = 0
for file in files:
    if string in file:
        n+=1
print(n)

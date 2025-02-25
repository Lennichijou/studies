import os
import random
from string import ascii_letters
nums = "0123456789"

os.mkdir("example")
os.chdir("example")
for i in range(1000):
    name = ""
    for j in range(5):
        name+=random.choice(ascii_letters)
        name+=random.choice(nums)
    f = open(f"{name}.txt", "x")
    f.write("sample text")
    f.close()

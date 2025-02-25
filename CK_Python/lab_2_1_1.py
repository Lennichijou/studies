from random import randint

FILENAME = "ip.log"
logs = []
i = 0

file = open(FILENAME, "w")

while (i < 10000):
    log = f"{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}.{randint(0, 255)}"
    logs.append(log)
    if (len(logs) == len(list(set(logs)))):
        print(log)
        file.write(log)
        file.write("\n")
        i+=1

file.close()

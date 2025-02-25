file = open("ip.log", "r")
content = file.readlines()
i = 0
solvefile = open("ip_solve.log", "w")
while (i < len(content)):
    content[i] = content[i].strip()
    log = content[i].split(".")
    for j in range(len(log)):
        log[j] = int(log[j])
        log[j] = f"{bin(log[j])[2:].zfill(8)}"
        print(log[j], end=" ")
        solvefile.write(log[j])
        solvefile.write(" ")
    solvefile.write("\n")
    print("\n")
    i+=1
solvefile.close()
file.close()

import string
letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

file = open("article_rus.txt", "r", encoding="utf8")
text = file.read()
file.close()
text = text.replace("\n", "").replace(" ", "").translate(dict.fromkeys(map(ord, string.punctuation))).lower()

solvefile = open("article_rus_solve.txt", "w")
for letter in letters:
    solvefile.write(f"{letter}: {text.count(letter)/len(text)}\n")
solvefile.close()

def alphabet(n):
    if n == 1:
        return "A"
    elif n == 2:
        return "B"
    elif n == 3:
        return "C"
    elif n == 4:
        return "D"
    elif n == 5:
        return "E"
    elif n == 6:
        return "F"
    elif n == 7:
        return "G"
    elif n == 8:
        return "H"
    elif n == 9:
        return "I"
    elif n == 10:
        return "J"
    elif n == 11:
        return "K"
    elif n == 12:
        return "L"
    elif n == 13:
        return "M"
    elif n == 14:
        return "N"
    elif n == 15:
        return "O"
    elif n == 16:
        return "P"
    elif n == 17:
        return "Q"
    elif n == 18:
        return "R"
    elif n == 19:
        return "S"
    elif n == 20:
        return "T"
    elif n == 21:
        return "U"
    elif n == 22:
        return "V"
    elif n == 23:
        return "W"
    elif n == 24:
        return "X"
    elif n == 25:
        return "Y"
    elif n == 0:
        return "Z"

initial = input("変換したい正の整数を入力してください(半角)：")
num = int(initial)
ln = []
#print("入力した数は", num, "です")

while num // 26 > 0:
    ln.append(num % 26)
    num = num // 26
ln.append(num)

ln.reverse()
#print(ln)
ln = [alphabet(i) for i in ln]
#print(ln)
str26 = " "
for i in range(len(ln)):
    str26 += ln[i]

print(str26)





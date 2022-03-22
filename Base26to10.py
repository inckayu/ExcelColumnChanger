def num(n):
    if n == "A" or n == "a":
        return "1"
    elif n == "B" or n == "b":
        return "2"
    elif n == "C" or n == "c":
        return "3"
    elif n == "D" or n == "d":
        return "4"
    elif n == "E" or n == "e":
        return "5"
    elif n == "F" or n == "f":
        return "6"
    elif n == "G" or n == "g":
        return "7"
    elif n == "H" or n == "h":
        return "8"
    elif n == "I" or n == "i":
        return "9"
    elif n == "J" or n == "j":
        return "10"
    elif n == "K" or n == "k":
        return "11"
    elif n == "L" or n == "l":
        return "12"
    elif n == "M" or n == "m":
        return "13"
    elif n == "N" or n == "n":
        return "14"
    elif n == "O" or n == "o":
        return "15"
    elif n == "P" or n == "p":
        return "16"
    elif n == "Q" or n == "q":
        return "17"
    elif n == "R" or n == "r":
        return "18"
    elif n == "S" or n == "s":
        return "19"
    elif n == "T" or n == "t":
        return "20"
    elif n == "U" or n == "u":
        return "21"
    elif n == "V" or n == "v":
        return "22"
    elif n == "W" or n == "w":
        return "23"
    elif n == "X" or n == "x":
        return "24"
    elif n == "Y" or n == "y":
        return "25"
    elif n == "Z" or n == "z":
        return "26"

alp = input("変換したいアルファベットを入力してください：")
ln = []

for i in range(len(alp)):
    ln.append(alp[i])
#print(ln)

ln = [num(i) for i in ln]
num10 = 0
#print(ln)

n = len(ln) - 1
for i in range(len(ln)):
    num10 += int(ln[i]) * 26**(n-i)

print(num10)



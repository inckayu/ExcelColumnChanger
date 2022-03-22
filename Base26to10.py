def num(n):
    if n == "A":
        return "1"
    elif n == "B":
        return "2"
    elif n == "C":
        return "3"
    elif n == "D":
        return "4"
    elif n == "E":
        return "5"
    elif n == "F":
        return "6"
    elif n == "G":
        return "7"
    elif n == "H":
        return "8"
    elif n == "I":
        return "9"
    elif n == "J":
        return "10"
    elif n == "K":
        return "11"
    elif n == "L":
        return "12"
    elif n == "M":
        return "13"
    elif n == "N":
        return "14"
    elif n == "O":
        return "15"
    elif n == "P":
        return "16"
    elif n == "Q":
        return "17"
    elif n == "R":
        return "18"
    elif n == "S":
        return "19"
    elif n == "T":
        return "20"
    elif n == "U":
        return "21"
    elif n == "V":
        return "22"
    elif n == "W":
        return "23"
    elif n == "X":
        return "24"
    elif n == "Y":
        return "25"
    elif n == "Z":
        return "26"
    elif n == "a":
        return "1"
    elif n == "b":
        return "2"
    elif n == "c":
        return "3"
    elif n == "d":
        return "4"
    elif n == "e":
        return "5"
    elif n == "f":
        return "6"
    elif n == "g":
        return "7"
    elif n == "h":
        return "8"
    elif n == "i":
        return "9"
    elif n == "j":
        return "10"
    elif n == "k":
        return "11"
    elif n == "l":
        return "12"
    elif n == "m":
        return "13"
    elif n == "n":
        return "14"
    elif n == "o":
        return "15"
    elif n == "p":
        return "16"
    elif n == "q":
        return "17"
    elif n == "r":
        return "18"
    elif n == "s":
        return "19"
    elif n == "t":
        return "20"
    elif n == "u":
        return "21"
    elif n == "v":
        return "22"
    elif n == "w":
        return "23"
    elif n == "x":
        return "24"
    elif n == "y":
        return "25"
    elif n == "z":
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



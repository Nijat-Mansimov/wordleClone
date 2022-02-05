import random
import time

letters = ["Jhony", "apple", "table", "center"]

time.sleep(1)
letter = random.choice(letters)
letter = letter.lower()
new = ""
for i in letter:
    new += i + "*"

print("""
Welcome to Wordle Clone
This Game:
` -> Symbol is a wrong letter   
^ -> Symbol is a true but wrong place 
* -> Symbol is a true and right place
""")

val = ""


def input_():
    global val
    user = input("\nEnter the word: ")
    user = user.lower()
    for i in range(len(user)):
        new_letter[i] = user[i]

    print()
    for i in new_letter:
        print(i, end="")
    print()

    for i in range(len(new_letter)):
        b = 0
        if letter[i] == new_letter[i]:
            new_letter[i] += "*"

        elif letter[i] != new_letter[i] and new_letter[i] in letter and new_letter[i] + "*" not in new_letter:
            if b == 0 and letter.count(new_letter[i]) == 1:
                new_letter[i] += "^"
                b = 1

            elif letter.count(new_letter[i]) > 1:
                new_letter[i] += "^"

            else:
                new_letter[i] += "`"

        else:
            new_letter[i] += "`"

    time.sleep(1)
    for i in new_letter:
        val += i
    print(val)


user = input("If you are ready let's start?(y/n): ")
new_letter = []
if user == "y":
    time.sleep(1)
    for i in range(len(letter)):
        new_letter.append("_ ")

    # print()
    for i in new_letter:
        print(i, end="")

    a = 1
    while a < 7:
        input_()
        print()

        if val == new:
            print()
            print("Good job!")
            break
        else:
            val = ""
            a += 1

else:
    print("Good bye!!!")

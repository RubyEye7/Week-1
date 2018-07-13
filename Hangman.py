
import random
count = 0


hangmen = ["hangman1", "hangman2", "hangman3", "hangman4", "hangman5", "hangman6", "hangman7"]

def guesser(word, word_blank):
    tries = 6
    while count < len(word):
        if word_blank.count("_") == 0:
            print("You win!")
            return
        if tries == 6:
            hangman2(word_blank)
        elif tries == 5:
            hangman3(word_blank)
        elif tries == 4:
            hangman4(word_blank)
        elif tries == 3:
            hangman5(word_blank)
        elif tries == 2:
            hangman6(word_blank)
        elif tries == 1:
            hangman7(word_blank)
        elif tries == 0:
            hangman1(word_blank)
            print("Game Over.")
            return

        letter = input("Enter 1 letter here: ")
        if word.count(letter) == 0 or word_blank.count(letter) > 0:
            tries -= 1
        else:
            new = list(word_blank)
            for i in range(len(word)):
                if word[i] == letter:
                    new[i] = letter
            word_blank = "".join(new)



def Easy():
    easy_list = ["cow", "pig", "horse", "sheep", "dog", "cat"]
    index = random.randint(0, 5)
    word = easy_list[index]
    word_blank = "_" * len(word)
    guesser(word, word_blank)
    return

def Medium():
    medium_list = ["io", "mars", "europa", "jupiter", "deimos", "phobos"]
    index = random.randint(0, 5)
    word = medium_list[index]
    word_blank = "_" * len(word)
    guesser(word, word_blank)
    return

def Hard():
    tries = 0
    hard_list = ["fizzled", "tyre", "jazz", "grazed", "id", "kwyjibo"]
    index = random.randint(0, 5)
    word = hard_list[index]
    word_blank = "_" * len(word)
    guesser(word, word_blank)
    return

def hangman1(word_blank):
    print(word_blank)
    print("")
    print(" ________")
    print(" |       |")
    print(" O       |")
    print("/|\      |")
    print(" |       |")
    print("/ \      |")
    print("         |")
    print("_________|")

def hangman2(word_blank):
    print(word_blank)
    print("")
    print(" ________")
    print(" |       |")
    print("         |")
    print("         |")
    print("         |")
    print("         |")
    print("         |")
    print("_________|")

def hangman3(word_blank):
    print(word_blank)
    print("")
    print(" ________")
    print(" |       |")
    print(" O       |")
    print("         |")
    print("         |")
    print("         |")
    print("         |")
    print("_________|")

def hangman4(word_blank):
    print(word_blank)
    print("")
    print(" ________")
    print(" |       |")
    print(" O       |")
    print(" |       |")
    print(" |       |")
    print("         |")
    print("         |")
    print("_________|")

def hangman5(word_blank):
    print(word_blank)
    print("")
    print(" ________")
    print(" |       |")
    print(" O       |")
    print("/|       |")
    print(" |       |")
    print("         |")
    print("         |")
    print("_________|")

def hangman6(word_blank):
    print(word_blank)
    print("")
    print(" ________")
    print(" |       |")
    print(" O       |")
    print("/|\      |")
    print(" |       |")
    print("         |")
    print("         |")
    print("_________|")

def hangman7(word_blank):
    print(word_blank)
    print("")
    print(" ________")
    print(" |       |")
    print(" O       |")
    print("/|\      |")
    print(" |       |")
    print("/        |")
    print("         |")
    print("_________|")


Start = input("Hello, welcome to Hangman! What mode would you like to use; Easy, Medium, Hard: ").lower()
if Start == "easy":
    Easy()

if Start == "medium":
    Medium()

if Start == "hard":
    Hard()

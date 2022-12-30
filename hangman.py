import random
from movies import movies
guesses=""
word=random.choice(movies)
chance=0

while chance >-1:
    failed=0
    for char in word:
        if char in guesses:
            print(char)
        else:
            print('-')
            failed+=1
    if failed == 0:
        print("You Win")
        print("The movie is:",word.upper())

    user = input("enter a movie name(all in  small letters): ")
    guesses+=user
    #if user==input():
    if user not in word:
        chance+=1
        if chance==1:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
        elif chance==2:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |      \ \n"
                  "  |        \n"
                  "__|__\n")

        elif chance ==3:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    / \ \n"
                  "  |        \n"
                  "__|__\n")
        elif chance==4:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |       \n"
                  "__|__\n")
        elif chance==5:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |      \ \n"
                  "__|__\n")
        elif chance==6:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "__|__\n")
            print("\nYOU LOSE")
            print(f"\n THE MOVIE NAME WAS {word.upper()}")
            break

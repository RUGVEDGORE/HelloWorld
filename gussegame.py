import random


# USER INPUT
def user_input():
    print("ENTER THE NUMBER TO GUSSE THE RANDOM NUMBER")
    entry = int(input())
    return entry

#RANDOM NUMBER GENERATION
def num_random():
    some_number = random.randint(1,10)
    print("SOME NUMBER BETWEEN 1 to 10 IS GENERATED")
    return some_number

def comparison(entry,some_number) :
    x = some_number
    while entry != some_number:
        if entry > some_number:
            print("VALUE : TOO HIGH")
            y = user_input()
            comparison(y, x)
        else:
            print("VALUE : TOO LOW")
            y = user_input()
            comparison(y,x)

    if entry == some_number:
        print("YOU GOT IT RIGHT")
    print("DO YOU WANT TO TRY AGAIN")
    answer = str(input().upper())
    if answer == "YES":
        some_number = num_random()
        entry = user_input()
        comparison(entry,some_number)
    else:
        print("YOU CHOOSE NO")
        exit()


print("GUSSING NUMBER GAME")
some_number = num_random()
entry = user_input()
comparison(entry,some_number)

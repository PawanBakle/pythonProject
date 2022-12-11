import random
def guess(x):
    rd=random.randint(1,x)
    opguess=0
    print("You get 4 guess")
    for i in range(0,4):

        opguess=int(input("Guess mar chote: "))

        if opguess<rd:
            print("Too low")
        elif opguess>rd:
            print("Too high")
        else:
            print(f"out of guess")
            break
    if opguess==rd:
        print(f"Congrats on guessing {rd}")
    else:
        print("Better luck mate :)")


guess(7)
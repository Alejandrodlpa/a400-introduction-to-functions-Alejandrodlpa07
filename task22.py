def game():
    import random
    import math
    rnum=random.randint(1,100)
    guess=0
    while guess!=rnum:
        guess=int(input("Enter your guess: "))
        if guess>rnum:
            print("The number is lower")
        if guess<rnum:
            print("The number is higher")
        if guess==rnum:
            print("DING DING DING, YOU WIN!!!")
            break
def title():
    print("""
          We will play a number guessing game, you try to guess a number from 1-100 
        and the program will tell you if the number is higher or lower, once you guess it you win. 
          """)


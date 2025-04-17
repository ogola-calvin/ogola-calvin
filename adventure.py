name = input("Hello, what's your name? ")
print("Welcome to the Game", name)

answer = input("Are you ready for the adventure?: ").upper()

if answer == "YES":
    print("Let's Gooo!")

    # Uncomment and complete the q1 question if needed
    # q1 = input("You're at a crossroad. Do you turn left or right? ").lower()
    # if q1 == "right":
    #     # Handle the 'right' case logic here if needed
    #     pass

    q2 = input("You've come across a wobbly bridge in the middle of the forest. Do you cross or swim? ").lower()

    if q2 == "cross":
        print("Correct, you proceed to the next level!")

    elif q2 == "swim":
        print("Game Over! You've been eaten by an alligator.")
        quit()
        
    else:
        print("Wrong option. Please try again.")
        
    q3 = input("After crossing the bridge, you come across a strange man. Do you greet him or proceed? ").lower()

    if q3 == "greet":
        print("Correct! You greet the man and he gives you gold to proceed to the next level!")

    elif q3 == "proceed":
        print("Game Over! You need gold to proceed to the next level.")
        quit()

    else:
        print("Wrong option. Please try again.")            

else:
    print("Goodbye!")

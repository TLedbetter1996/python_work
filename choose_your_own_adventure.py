name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way do you want to go? ").lower()

#left story path 

if answer == "left":
    answer = input("You have come to a river, you can walk around it or swim across?")
    if answer == "swim":
        print("You swam across and were eaten across by an Alligator...")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and lost the game.")
    else:
        print('Not a valid option... You lose.', str(name))


#right story path 
elif answer == "right":
    answer = input("You come to a bridge and it looks wobbly, do you want to cross it or go back? (cross/back) ")

    if answer == "back":
        print("You got back and were suddenly attacked. You lose. ")
        print("GAME OVER")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? ")
        if answer == "yes":
            print("They give you gold and escort you out of the jungle. You win")
        else:
            print("You wandered aimlessly forever... ")
else:
    print('Not a valid option... You lose.', str(name))

# welcome to the quiz game 
print("Welcome to my computer quiz!")

playing = input("Do you want to play? :) ")
score = 0

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")

#questions that we will include
#This covers the input method, lower method and if/else statements

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1  # the same as score = score + 1 
    
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1 

else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1 
else: 
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1 
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100 ) + "%.")


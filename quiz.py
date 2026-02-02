print("Welcome to the Quiz Game!")
playing = input("Do you want to play?\n").lower()
if playing != "yes":
    print("Maybe next time!")
    quit()
score = 0
q = 0
print("Great! Let's start the quiz.")

answer= input("What does CPU stand for?\n").lower()
q += 1
if answer == "central processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Central Processing Unit.")


answer= input("What does GPU stand for?\n").lower()
q += 1
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Graphics Processing Unit.")
    

answer= input("What does RAM stand for?\n").lower()
q += 1
if answer == "random access memory":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Random Access Memory.")
    

answer = input("What does PSU stand for?\n").lower()
q += 1
if answer == "power supply unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect! The correct answer is Power Supply Unit.")
print("You got  " + str(score) + " questions correct ")
print("You answered " + str((score /q) * 100) + "% ")
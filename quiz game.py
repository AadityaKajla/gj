print("Welcome to the Quiz!")
playing = input("Do you want to play? Type yes or no ")
if playing != "yes":
    quit()

print("Ok lets play! :)")
i = 0
answer = input("Is the coding language python named after a snake? ")

if answer == "no":
    print("Correct!")
    i = i+1
else:
    print("Incorrect! Guido named python after Monty Python's Flying Circus, a British com-edy series from the 70s.")

answer = input("What does C.P.U. Stand for? ")
if answer == "central processing unit":
    print("Correct!")
    i = i+1
else:
    print("Incorrect!The correct answer is Central Processing Unit")

answer = input("What do we call a minecraft water bucket clutch? ")

if answer == "MLG":
    print("Correct!")
    i = i+1
else:
    print("Incorrect! The correct answer is MLG")

print(f"score = {i}/3")
q = input("type q to quit")
if q == "q ":
    quit()



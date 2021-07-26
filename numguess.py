import random
secret_number = random.randint(1,100)
user_guess = 0
# Keep a counter for guesses

while True:
    # Read human input
    user_number = int(raw_input("Enter a number:"))
    user_guess += 1
    # Check if the input is High or Low (compare it with secret_number)
    if secret_number > user_number:
        print("enter big")
    elif secret_number < user_number:
        print("enter small")
    
    # If the number given is the secret_number break out!
    else:
        print("You guessed right number:",secret_number,"chances took",user_guess)
        break

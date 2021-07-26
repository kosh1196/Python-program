import random

with open("words.txt") as my_file:
    lines = my_file.readlines()
    secret_word = random.choice(lines)
    secret_word = secret_word.rstrip("\n").lower()

for index, char in enumerate(secret_word):
    if index == 0:
        print(char.upper())
    else:
        print(" _")
print()

correct_letters = ""
wrong_inputs = 0
threshold = 5
while True:
    user_input = raw_input("Please provide a letter or the solution: ")
    
    if len(user_input) > 1: # Is providing the solution
        if user_input.lower() != secret_word.lower():
            print("Game over, the secret word was" ,secret_word)
            break
        else:
            print("Correct!!!! The word was indeed ",secret_word)
            break
    elif len(user_input) == 1:
        if user_input in secret_word:
            print("Correct, the letter ",user_input," appears in the word!")
            correct_letters = correct_letters + user_input
        else:
            wrong_inputs += 1
            print("Wrong, the letter",user_input," does not appears in the word. Wrong inputs so far:", wrong_inputs/threshold)

    if wrong_inputs >= threshold:
        print("You have provided",threshold," wrong answers. Game over! The word was ",secret_word)
        break

    for index, char in enumerate(secret_word):
        if index == 0:
            print(char.upper())
        elif char in correct_letters:
            print(char)
        else:
            print(" _")
    print()



from art import logo
import random

guess_num = random.randint(1, 100)

#print(f"pssst: number random is {guess_num}")
print(logo)
print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

life = 0
if difficulty_level == "easy":
    life = 10
elif difficulty_level == "hard":
    life = 5
else:
    print("entered wrong value. Ending the game!")

def compare_guess(guess):
    global life
    if guess == guess_num:
        print(f"You are right!! The number is {guess}")
        return "You guessed it right! congratzzzz!!"
    elif guess < guess_num:
        print("Too low \nGuess again.")
        life = life -1
        return life
    elif guess > guess_num:
        print("Too high \nGuess again")
        life = life - 1
        return life


is_game = True

while is_game:
    print(f"You have {life} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if compare_guess(guess) == "You guessed it right! congratzzzz!!":
        is_game = False
    else:
        is_game = True
    if life == 0:
        is_game = False









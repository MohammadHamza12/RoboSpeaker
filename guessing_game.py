import random

easy_word = ["apple", "train", "tiger", "money", "india"]
medium_word = ["python", "bottle", "mpnkey", "planet", "laptop"]
hard_word = ["elephant", "diamond", "umbrella", "computer", "mountain"]


print("Welcome to the password guessing game")
print("Choose a difficulty level")

level = input("Enter Difficulty: ").lower()
if level == "easy":
    secret = random.choice(easy_word)
elif level == "medium":
    secret = random.choice(medium_word)
if level == "hard":
    secret = random.choice(hard_word)
else:
    print("Invalid choice. Defaulting to easy level")
    secret = random.choice(easy_word)

attempts = 0
print("\n guess the secret password")

while True:
    guess = input("Enter your guess : ").lower()
    attempts +=1

    if guess == secret:
        print(f"Congartulation! You guessed it in {attempts} attempts.")
        break
        
    hint = ""

    for i in range(len(secret)):
        if i < len(guess) and guess[i] == secret[i]:
            hint += guess[i]
        else:
            hint += "_"

    print("Hint:",hint)

print("game Over")
        
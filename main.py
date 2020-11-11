import random
import json
import datetime

secret = random.randint(1, 5)
attempts = 0

with open("score_list.txt", "r") as score_file:
    score_list = json.loads(score_file.read())
    print("Top scores: " + str(score_list))

    new_score_list = sorted(score_list, key=lambda k: k['attempts'])[:3]

    for score_dict in score_list:
        score_text = "Player {0} had {1} attempts on {2}. The secret number was {3}. The wrong guesses were: {4}".format(
            score_dict.get("player_name"),
            str(score_dict.get("attempts")),
            score_dict.get("date"),
            score_dict.get("secret_number"),
            score_dict.get("wrong_guesses"))
        print(score_text)

print("_______________________START_______________________")
player_name = input("Type your name: ")
wrong_guesses = []

while True:
    guess = int(input("Guess the secret number (between 1 and 5): "))
    attempts += 1

    if guess == secret:
        score_list.append({"player": player_name, "secret_number": guess, "attempts": attempts, "date": str(datetime.datetime.now()), "wrong_guesses": wrong_guesses})

        with open("score_list.txt", "w") as score_file:
                score_file.write(json.dumps(score_list))

        print("You've guessed it - congratulations! It's number " + str(secret))
        print("Attempts needed: " + str(attempts))

        print("_______________________END_______________________")

        break
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")

    wrong_guesses.append(guess)



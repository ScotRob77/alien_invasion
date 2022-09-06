import random, alien, string, sys
from countries import country


def intro():
    """
    Welcome message introducing the name of the game.
    Welcome text and instructions for gameplay.
    Enter name input to start game.
    """
    print("WELCOME TO ALIEN INVASION..!\n")
    print("Hello Earthling, I am from the planet Aldaran...\n")
    print("We have been watching Earth for many years...\n")
    print("You have not been doing a good job of keeping it safe...\n")
    print("So we are here to take over...\n")
    print("You need to stop us from invading. To do this...\n")
    print("You need to guess which country we intend to invade first.\n")
    print("But beware. you can only guess wrong 6 times...\n")
    print("Before you start you need to tell us your name.\n")
    
    user = input("What is your name Earthling?\n")

    print(f"Greetings {user}...\n")

    return user


def select_random_country(country):
    """
    Will randomly select a country from a list of countries
    """
    return random.choice(country)
print(select_random_country(country))

remaining_attempts = 6
already_guessed = ""


def create_guess_blanks(secret_country):
    """
    Will create same amount of blanks as the country to guess
    """
    print(" _ " * len(secret_country))


intro()


secret_country = select_random_country(country)
guess = input("Guess a letter of the country you think we will invade..")
print(alien.alien_stages(remaining_attempts))
create_guess_blanks(secret_country)


alphabet = list(string.ascii_uppercase)


def is_guess_correct(guess, secret_country):
    """
    Allows the user to guess a letter
    """
    if len(guess) != 1:
        print("Whoa there Earthling. One letter at a time..!\n")
    elif guess not in alphabet:
        print("That's not a letter... Try again...\n")
        sys.exit()
    else:
        if guess in secret_country:
            return True
        else:
            return False


guess_in_country = is_guess_correct(guess, secret_country)


if guess_in_country:
    if guess in already_guessed:
        print("You've already guessed that letter, choose another\n".format(guess))
    else:
        print("Well Done Earthling..! That letter is part of the country\n".format(guess))
else:
    print("Bad Luck foolish Earthling.. That is 1 guess gone".format(guess))
    remaining_attempts -= 1


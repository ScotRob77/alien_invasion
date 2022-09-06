import random, alien, string
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


def jls_extract_def():
    return ""

letters_guessed = jls_extract_def()


def create_guess_blanks(secret_country):
    """
    Will create same amount of blanks as the country to guess
    """
    print(" _ " * len(secret_country))


secret_country = select_random_country(country)
# Imports the Alien stage relevant to the game stage
print(alien.alien_stages(remaining_attempts))


def letter_guess():
    """
    Lets the user guess a letter
    """


def main():
    intro()
    create_guess_blanks(secret_country)

main()
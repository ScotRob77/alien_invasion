import random, alien
from countries import country


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
    print("_" * len(secret_country))


secret_country = select_random_country(country)
# Imports the Alien stage relevant to the game stage
print(alien.alien_stages(remaining_attempts))
create_guess_blanks(secret_country)


def letter_guess():
    """
    Lets the user guess a letter
    """


def is_guess_correct():
    """
    
    """

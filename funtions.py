# FUNCTIONS #

# Best for use in situations where you can REUSE the code
# Should use lowercase_words_separated_by_underscore as the naming convention
# Best practice to comment so the functionality is documented
# Receive input and return values
# Functions should do 1 or 2 tasks that are repeated multiple times.
# Can be used in another file/script and can be aggregated into one larger function that calls functions
# Comments that describe how a function is used along with examples should be encased in triple quotes
from time import sleep
import math

def typewriter_greeting(phrase):
    """
    Loop through the phrase to print each character like a typewriter by adding a half second sleep between
    characters
    """
    for char in phrase:
        sleep(.5)
        print(char, end='', flush=True)

typewriter_greeting('hello code warriors')

def fahrenheit_to_celsius(temperature):
    """
    Another way to use comments is to establish the parameters and the return statement of the function
    :param temperature in fahrenheit
    :return print statement with both values so users can see the conversion
    """
    celsius = round((temperature - 32) * (5/9))
    return print(f'Today the temperature is {temperature} fahrenheit or {celsius} celsius')

fahrenheit_to_celsius(50)

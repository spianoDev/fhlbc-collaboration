# FUNCTIONS #

# Best for use in situations where you can REUSE the code
# Should use lowercase_words_separated_by_underscore as the naming convention
# Best practice to comment so the functionality is documented
# Receive input and return values
# Functions should do 1 or 2 tasks that are repeated multiple times.
# Can be used in another file/script and can be aggregated into one larger function that calls functions
from time import sleep

def typewriter_greeting(phrase):
    # Loop through the phrase to print each character like a typewriter
    for char in phrase:
        sleep(.5)
        print(char, end='', flush=True)



typewriter_greeting('hello code warriors')

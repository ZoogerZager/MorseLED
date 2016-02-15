"""

A script to translate input strings into morse code to use in activating a LED
via a Raspberry Pi, its GPIO Pins, and a Breadboard. Short refresher on the
Rules of Morse Code from https://en.wikipedia.org/wiki/Morse_code:
1. The length of a dot is one unit.
2. A dash is three units.
3. The space between parts of the same letter is one unit.
4. The space between letters is three units.
5. The space between words is seven units.

"""
import RPi.GPIO as GPIO
from time import sleep


def morse_translate(input_text):
    """translates the input text into morse skipping special characters."""
    translated_text = []
    try:
        for letter in input_text:
            if letter == ' ':
                translated_text.append('space') # spaces = 7 dashes
            else:    
                translated_text.append(morse_dict[letter])
    except(KeyError):
        pass
    return translated_text
    
# GPIO setup code
LEDPin = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LEDPin, GPIO.OUT)
    
# Initialize the Morse Dictionary and get the key, value pairs.
morse_dict = {}
with open ('morse_dictionary.txt', 'r') as data:
    for line in data:
        letter = line.rsplit()
        morse_dict[letter[0]] = letter[1]

# Get the user's input and clean it.    
user_input = input('Enter a string: ')
# This isn't working with special chars in the middle of letters
user_input = user_input.strip('!@#$%^&*()')
user_input = user_input.upper()

# Print the cleaned and translated user_input
print(user_input)
morse_code = morse_translate(user_input)
print(morse_code)

# Blinking Logic and Output
try:
    for letter in morse_code:
        if letter == 'space':
            sleep(7) # Time between words.
        else:
            for blip in letter:
                if blip == '.':
                    GPIO.output(LEDPin, True)
                    sleep(1) # Length of Dot
                    GPIO.output(LEDPin, False)
                if blip == '-':
                    GPIO.output(LEDPin, True)
                    sleep(3) # Length of Dash
                    GPIO.output(LEDPin, False)
                sleep(1) # Time between each blip of the same letter.    
            sleep(3) # Time between letters of the same word.
finally:
    GPIO.cleanup()
                    
                 
            


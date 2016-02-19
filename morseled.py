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
    """translates the input_text into morsecode skipping special characters."""
    translated_text = []
    try:
        for letter in input_text:
            if letter == ' ':
                translated_text.append('space')
            else:    
                translated_text.append(morse_dict[letter])
    except(KeyError):
        pass
    return translated_text
    
def GPIO_output():
    """Handles the default GPIO Blinking Logic and Output"""
    try:
        for letter in morse_code:
            if letter == 'space':
                sleep(space_time) # Time between words.
            else:
                sleep(dash_time) # Time between letters of the same word.
                for blip in letter:
                    sleep(dot_time) # Time between each blip of the same letter. 
                    if blip == '.':
                        GPIO.output(LEDPin, True)
                        sleep(dot_time) # Length of Dot
                        GPIO.output(LEDPin, False)
                    if blip == '-':
                        GPIO.output(LEDPin, True)
                        sleep(dash_time) # Length of Dash
                        GPIO.output(LEDPin, False)
    finally:
        GPIO.cleanup()
        
def Console_output():
    """Outputs the Morse code as dots and dashes in the Console"""
            for letter in morse_code:
            if letter == 'space':
                sleep(space_time) # Time between words.
            else:
                sleep(dash_time) # Time between letters of the same word.
                for blip in letter:
                    sleep(dot_time) # Time between each blip of the same letter. 
                    if blip == '.':
                        GPIO.output(LEDPin, True)
                        sleep(dot_time) # Length of Dot
                        GPIO.output(LEDPin, False)
                    if blip == '-':
                        GPIO.output(LEDPin, True)
                        sleep(dash_time) # Length of Dash
                        GPIO.output(LEDPin, False)
    
    
# Initialize the Morse Dictionary and get the key, value pairs.
morse_dict = {}
with open ('morse_dictionary.txt', 'r') as data:
    for line in data:
        character = line.rsplit()
        morse_dict[character[0]] = character[1]

        
## Configuration
output_GPIO = True
output_Console = True
dot_time = .25 # Customize output speed
dash_time = dot_time * 3
space_time = dot_time * 7

# Run GPIO setup.
if output_GPIO: 
    LEDPin = 22
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LEDPin, GPIO.OUT)  

# Get the user's input, clean it, and uppercase it.    
user_input = input('Enter a string: ')
user_input = user_input.strip('!@#$%^&*()";/<>}]{[_`~ ')
user_input = user_input.upper()

# Print the cleaned and translated user_input
print(user_input)
morse_code = morse_translate(user_input)
print(morse_code)


if output_GPIO:
    GPIO_output()
if output_Console:
    Console_output()


# Blinking Logic and Output

import art
import json

# print intro
print("Welcome to:")
print(art.logo)

# load morse code dictionary
f = open("morse-code.json")
dictionary = json.load(f)
f.close()


# convert
def translator(message):
    """
    Translator funtion coverts strings to a list of morse code letters
    :param message: string to translate
    :return: list of morse code letters or None if some symbol wasn't found in the dictionary
    """
    morse_code = []
    for letter in message:
        try:
            letter_code = dictionary[letter]
            morse_code.append(letter_code)
        except KeyError:
            print(f"This symbol ({letter}) is in our dictionary, please try a different message.")
            return
    return morse_code


# start translation programme
keep_translating = True

while keep_translating:
    user_input = input("Type your message: ").lower()
    morse_code_list = translator(user_input)

    if morse_code_list:
        translation = ' '.join(morse_code_list)
        print(f"Translation: {translation} \n")

        if input("Do you want to keep translating? Y/n ").lower() == 'n':
            keep_translating = False





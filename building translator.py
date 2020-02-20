# Say we wanna translate all vowels to letter g
# Start by set a function with empty variable


def translate(phrase):

    translation = " "
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate("dog"))


# Say we wanna keep the upper case of the phrase
def translate(phrase):

    translation = " "
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


print(translate("Elephant"))
from art import logo
import string

print(logo)

alphabet = string.ascii_lowercase + "0123456789!@#$%^&*()_+-=[]{}|;':,.<>/?"
isTrue = True


def caesar(text, shift, direction):
    result = ""
    encrypted_alphabet = alphabet[shift:] + alphabet[:shift]

    for letter in text:
        if direction == 'encode':
            if letter == " ":
                result += " "
            else:
                index = alphabet.index(letter)
                result += encrypted_alphabet[index]
        elif direction == 'decode':
            if letter == " ":
                result += " "
            else:
                index = encrypted_alphabet.index(letter)
                result += alphabet[index]

    print(f"The {direction}d text is {result} \n")


while isTrue:
    direction = input(
        "\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)

    caesar(text, shift, direction)

    answer = input(
        "Do you want to restart the cipher program? [yes, no]: ").lower()
    if answer == 'no':
        isTrue = False
        print("Goodbye")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift):
    ausgabetext = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        new_letter = alphabet[new_position]
        ausgabetext += new_letter
    print (f"Der geheime Code lautet :{ausgabetext}")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "yes":
        ceasar()
    else:
        print("Goodbye")

def ceasar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))  
    if direction == "decode":
        encrypt(text, shift)
    else:
        shift = (26-shift)
        encrypt(text, shift)

ceasar()
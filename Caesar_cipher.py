alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']

def encrypt(orignal_text, shift_amount):
    coded=[]

    for char in orignal_text:
        position= alphabet.index(char)
        new_position= position + shift_amount

        new_position %= len(alphabet)
        new_letter= alphabet[new_position]
        coded.append(new_letter)

    print(f"The encypted message of your text is: {''.join(coded)}")

def decrypt(orignal_text, shift_amount):
    decoded=[]

    for letters in orignal_text:
        letter= alphabet.index(letters)
        new_position= letter - shift_amount

        new_position %=len(alphabet)
        new_letter= alphabet[new_position]
        decoded.append(new_letter)
    
    print(f"The decrypted message of your text is: {''.join(decoded)}")

def caesar():
    direction= input("Type 'encode' to encrypt and type 'decode' to decrypt: \n").lower()
    text= input("Enter your text: \n").lower()
    shift= int(input("Type the number you wanted to shift by: \n"))

    if direction=='encode':
        encrypt(text, shift)
        
    elif direction== 'decode':
        decrypt(text, shift)

    else:
        print("Invalid input!!!")

caesar()


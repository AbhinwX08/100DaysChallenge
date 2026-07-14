alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(orignal_text, shift_amount):
    direction= input("Type 'encode' to encrypt and type 'decode' to decrypt: \n").lower()

    coded=[]
    for char in range(len(text)):
        text[char]=alphabet_lower[char+2]
        coded.append(text[char])

    print(f"The encypted message of your text is: {coded}")
text= input("Enter your text: \n").lower()
shift= int(input("Type the number you wanted to shift the alphabets by: \n"))

encrypt(text,shift)

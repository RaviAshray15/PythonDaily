alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt.\n").lower()
if direction == 'encode' or direction == 'decode':
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
else:
    print("Enter either 'encode' or 'decode'!!")

def encrypt(original_text, shift_amount):
    cipher_text = ""
    if char not in alphabet:
        cipher_text += char
    else:
        for char in original_text:
            shifted_position = alphabet.index(char) + shift_amount
            
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded message: {cipher_text}")
    
def decrypt(original_text, shift_amount):
    cipher_text = ""
    if char not in alphabet:
        cipher_text += char
    else: 
        for char in original_text:
            shifted_position = alphabet.index(char) - shift_amount
            
            shifted_position %= len(alphabet)
            cipher_text += alphabet[shifted_position]

    print(f"Here is the decoded message: {cipher_text}")

if direction == 'encode':
    encrypt(text, shift)
elif direction == 'decode':
    decrypt(text, shift)

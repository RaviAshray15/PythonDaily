alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]


go_again = True


# ==========================================
# ENCRYPT
# ==========================================

def encrypt(original_text, shift_amount):

    cipher_text = ""

    for char in original_text:

        if char not in alphabet:
            cipher_text += char

        else:
            shifted_position = alphabet.index(char) + shift_amount

            shifted_position %= len(alphabet)

            cipher_text += alphabet[shifted_position]

    print(f"Here is the encoded message: {cipher_text}")


# ==========================================
# DECRYPT
# ==========================================

def decrypt(original_text, shift_amount):

    cipher_text = ""

    for char in original_text:

        if char not in alphabet:
            cipher_text += char

        else:
            shifted_position = alphabet.index(char) - shift_amount

            shifted_position %= len(alphabet)

            cipher_text += alphabet[shifted_position]

    print(f"Here is the decoded message: {cipher_text}")


# ==========================================
# MAIN PROGRAM
# ==========================================

while go_again:

    direction = input(
        "\nType 'encode' to encrypt, type 'decode' to decrypt:\n"
    ).lower()


    # --------------------------------------
    # CHECK DIRECTION
    # --------------------------------------

    if direction != 'encode' and direction != 'decode':

        print("Enter either 'encode' or 'decode'!!")

        continue


    # --------------------------------------
    # GET MESSAGE
    # --------------------------------------

    text = input(
        "Type your message:\n"
    ).lower()


    # --------------------------------------
    # GET SHIFT
    # --------------------------------------

    shift = int(input(
        "Type the shift number:\n"
    ))


    # --------------------------------------
    # ENCODE / DECODE
    # --------------------------------------

    if direction == 'encode':

        encrypt(text, shift)

    elif direction == 'decode':

        decrypt(text, shift)


    # --------------------------------------
    # PLAY AGAIN
    # --------------------------------------

    while True:
        choice = input(
        "Type 'yes' if you want to go again, type 'no' to exit:\n").lower()
        
        if choice == "yes":
            go_again = True
            break

        elif choice == "no":
            go_again = False
            break

        else:
            print("\nInvalid input. Please enter 'yes' or 'no'.")


print("\nGoodbye!")
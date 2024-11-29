def caesar_cipher(text, shift, mode='encrypt'):
    """
    Perform Caesar Cipher encryption or decryption.

    Parameters:
    text (str): The input text to encrypt or decrypt.
    shift (int): The number of positions to shift each letter.
    mode (str): 'encrypt' to encrypt the text, 'decrypt' to decrypt it.

    Returns:
    str: The resulting encrypted or decrypted text.
    """
    if mode == 'decrypt':
        shift = -shift

    result = []

    for char in text:
        if char.isalpha():
            # Determine if the character is uppercase or lowercase
            base = ord('A') if char.isupper() else ord('a')
            # Perform the shift
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result.append(shifted_char)
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)

    return ''.join(result)


if __name__ == "__main__":
    print("Welcome to Caesar Cipher")
    while True:
        print("\nChoose an option:")
        print("1: Encrypt a message")
        print("2: Decrypt a message")
        print("0: Exit")
        
        try:
            choice = int(input("Enter your choice [0-2]: "))
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 2.")
            continue

        if choice == 0:
            print("Exiting the program. Goodbye!")
            break
        elif choice not in [1, 2]:
            print("Invalid choice. Please select 1, 2, or 0.")
            continue

        message = input("Enter the message: ").strip()
        if not message:
            print("Message cannot be empty. Please try again.")
            continue

        try:
            shift_value = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter a valid integer.")
            continue

        if choice == 1:
            encrypted = caesar_cipher(message, shift_value, mode='encrypt')
            print(f"Encrypted message: {encrypted}")
        elif choice == 2:
            decrypted = caesar_cipher(message, shift_value, mode='decrypt')
            print(f"Decrypted message: {decrypted}")

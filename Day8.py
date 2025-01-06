# Define the extended alphabet
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def caesar(text, shift, direction):
    if direction == "decode":
        shift *= -1  # Reverse the shift for decoding
    
    result = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shifted_index = (alphabet.index(char) + shift) % 26
            result += alphabet[shifted_index]
        else:
            result += char  # Leave non-alphabetic characters unchanged

    print(f"Here's the {direction}d result: {result}\n")

# Main loop for user interaction
while True:
    direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26  # Normalize the shift value

    caesar(text, shift, direction)
    
    # Check if the user wants to run the program again
    if input("Do you want to run the program again? Type 'yes' or 'no':\n").lower() == 'no':
        print("Goodbye!")
        break


# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..',
    '9': '----.',
    ',': '--..--', '.': '.-.-.-', '?': '..--..',
    '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-',
    ' ': '/',
}


def text_to_morse(text):
    morse_text = ""
    for char in text.upper():
        if char in MORSE_CODE_DICT:
            morse_text += MORSE_CODE_DICT[char] + " "
        else:
            morse_text += "?" + " "  # unknown characters
    return morse_text


def main():
    print("Text to Morse Code Converter")
    print("Type 'exit' to quit.\n")
    while True:
        user_input = input("Enter text: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        morse = text_to_morse(user_input)
        print(f"Morse Code: {morse}\n")

main()
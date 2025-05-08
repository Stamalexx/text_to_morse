morse_dict = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..'
}
morse_output = ""
user_input = input("Enter the word that you want to convert to morse code: ").upper()
for letter in user_input:
    if letter in morse_dict:
        morse_output += morse_dict[letter]
    elif letter == " ":
        morse_output += " "

    else:
        print(f"Letter {letter} not in the morse dic")

print(morse_output)
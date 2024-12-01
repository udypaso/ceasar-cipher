import art
print(art.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f','g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def ceasar(original_text,shift_amount, encode_or_decode):
    decipher_text = ""
    if encode_or_decode == "decode":
                shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            decipher_text += letter
        else:

            
            shifted_position = alphabet.index(letter) + shift_amount

            shifted_position %= len(alphabet)
            decipher_text += alphabet[shifted_position]
        
    print(f"here is the {encode_or_decode}d result {decipher_text}")

should_continue = True

while should_continue:

    direction = input("Type 'encode' to encrpt, type 'decode' to decrypt:\n").lower()
    text = input("type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    ceasar(original_text=text, shift_amount=shift,encode_or_decode=direction)

    restart=input("Type 'yes' if you want to continue otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")



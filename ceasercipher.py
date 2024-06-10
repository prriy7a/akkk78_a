alphabet=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
def encryption(plain_text,shift_key):
    cipher_text=""
    for char in plain_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position+shift_key)%26
            cipher_text+=alphabet[new_position]
        else:
            cipher_text+=char
    print(f"Here is the text after encryption: {cipher_text}")
def decryption(cipher_text,shift_key):
    plain_text=""
    for char in cipher_text:
        if char in alphabet:
            position=alphabet.index(char)
            new_position=(position-shift_key)%26
            plain_text+=alphabet[new_position]
        else:
            plain_text+=char
    print(f"Here is the text after decryption: {plain_text}")
end=False
while not end:
    what_to_do=input("Type 'encrypt' for encryption, type 'decrypt' for decryption:\n").lower()
    text=input("Type your message:\n").upper()
    shift=int(input("Enter shift key:\n"))
    if what_to_do=="encrypt":
        encryption(plain_text=text,shift_key=shift)
    elif what_to_do=="decrypt":
        decryption(cipher_text=text,shift_key=shift)
    play_again=input("Type 'yes' to continue,'no' to exit").lower()
    if play_again=="no":
        end=True
        print("Have a nice day!Bye...")
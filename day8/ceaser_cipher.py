alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i', 'j', 'k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

print("Welcome to the Ceaser Cipher!")
choice = str(input("What do you want to do? encode, decode : "))
text = str(input("Please enter your message: "))
shift = int(input("Type the shift number: "))

def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        new_index = alphabet.index(letter) + shift_amount
        new_index = new_index % len(alphabet)
        encrypted_text += alphabet[new_index]
    print(encrypted_text)

def decrypt(cipher, shift_amount):
    plain_text = ""
    for letter in cipher:
        new_index = alphabet.index(letter) - shift_amount
        new_index = new_index % len(alphabet)
        plain_text += alphabet[new_index]
    print(plain_text)

if choice == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)
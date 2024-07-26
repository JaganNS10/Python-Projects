alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def encryption(get_encrypt_Message,get_encrypt_shift):
    ciper_encrypt=""
    for i in get_encrypt_Message:
        if i in alphabet:
            current_position=alphabet.index(i)
            get_position = (current_position+get_encrypt_shift)%26
            ciper_encrypt+=alphabet[get_position]
        else:
            ciper_encrypt+=i
    print(ciper_encrypt)
def decryption(get_decrypt_Message,get_decrypt_shift):
    ciper_decrypt=""
    for j in get_decrypt_Message:
        if j in alphabet:
            current_position=alphabet.index(j)
            new_position=(current_position-get_decrypt_shift)%26
            ciper_decrypt+=alphabet[new_position]
        else:
            ciper_decrypt+=j
    print(ciper_decrypt)
while True:
    userInput=input("Type 'encrypt' For encryption,Type 'decrypt' For decryption:\n")
    Message = input("Type the Message:\n").lower()
    shift = int(input("Enter the shift key:\n"))
    if userInput=="encrypt":
        encryption(get_encrypt_Message=Message,get_encrypt_shift=shift)
    elif userInput=="decrypt":
        decryption(get_decrypt_Message=Message,get_decrypt_shift=shift)
    continue_userInput=input("Do You want to continue or stop select yes or no:\n")
    if continue_userInput=="no":
        print("Thank you...")
        break

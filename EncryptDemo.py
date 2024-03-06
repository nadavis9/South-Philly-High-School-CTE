

#Input message data
message = input("Please provide the message you would like to encrypt: ")
session_key = input("Please provide a key to encrypt your message with: ")

#function to encrypt the message. Returns the cipher text
def encrypt_me(plain_text, key):
    cipher_text = "".join([chr(ord(c1)^ord(c2)) for (c1,c2) in zip(plain_text, key)])
    print("Your cipher text is ready for transmission:", cipher_text)
    return cipher_text

#function to decrypt the message. Must pass cipher text with the key used
def decrypt_me(plain_text, key):
    plain_message = "".join([chr(ord(c1)^ord(c2)) for (c1,c2) in zip(plain_text, key)])
    print("Your original message was successfully decrypted:", plain_message)





if (len(message)==len(session_key)):

    encrypted_text = encrypt_me(message, session_key)
    print(encrypted_text)

    decrypt_me(encrypted_text, session_key)

else:
    
    print("The length of your key does not match the length of your message. Please try again")
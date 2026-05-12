
 # PRACt2 
# #CEASER CIPHER

# def encrypt(text, s):
#     result = ""
#     for i in range(len(text)):
#         char = text[i]

#         if (char.isupper()):
#             result += chr((ord(char) + s - 65) % 26 + 65)
#         elif char.islower():
#             result += chr((ord(char) + s - 97) % 26 + 97)
#         else:
#             result += char

#     return result

# text = "CEASER CIPHER"
# s = 4
# print("Text : " + text)
# print("Shift : " + str(s))
# print("Cipher: " + encrypt(text, s))

# # Substitution Cipher


# import string

# all_letters = string.ascii_letters

# # A list of letters in a predefined order to use as a key
# dict1 = {'a': 'm', 'b': 'n', 'c': 'b', 'd': 'v', 'e': 'c', 'f': 'x', 'g': 'z',
#          'h': 'a', 'i': 's', 'j': 'd', 'k': 'f', 'l': 'g', 'm': 'h', 'n': 'j',
#          'o': 'k', 'p': 'l', 'q': 'p', 'r': 'o', 's': 'i', 't': 'u', 'u': 'y',
#          'v': 't', 'w': 'r', 'x': 'e', 'y': 'w', 'z': 'q'}

# plain_txt = "hello world"
# cipher_txt = []

# # --- ENCRYPTION ---
# # loop to apply substitution
# for char in plain_txt:
#     if char in all_letters:
#         temp = dict1[char.lower()]
#         cipher_txt.append(temp)
#     else:
#         temp = char
#         cipher_txt.append(temp)

# cipher_txt = "".join(cipher_txt)
# print("Plain Text is: ", plain_txt)
# print("Cipher Text is: ", cipher_txt)


# # --- DECRYPTION ---
# # reverse the dictionary mapping to create the decryption key
# dict2 = {}
# for key, value in dict1.items():
#     dict2[value] = key

# decrypt_txt = []
# for char in cipher_txt:
#     if char in all_letters:
#         temp = dict2[char.lower()]
#         decrypt_txt.append(temp)
#     else:
#         temp = char
#         decrypt_txt.append(temp)

# decrypt_txt = "".join(decrypt_txt)
# print("Recovered plain text : ", decrypt_txt)







# #pract1
# from cryptography.fernet import Fernet

# message = "hello world"

# key = Fernet.generate_key()

# fernet = Fernet(key)

# encMessage = fernet.encrypt(message.encode())

# print("original string: ", message)
# print("encrypted string: ", encMessage)

# decMessage = fernet.decrypt(encMessage).decode()

# print("decrypted string: ", decMessage)





# pract4 

# from PIL import Image
# import stepic
# original_image = Image.open("C:\\Users\\dell2\\OneDrive\\Pictures\\Screenshots\\adhar.png")

# message = b'Hello World, this is a hidden message!'

# encoded_img = stepic.encode(original_image, message)

# encoded_img.save('img2.png')

# print("Message successfully hidden and saved as img2.png")

# stego_image = Image.open("img2.png")
# decoded_msg = stepic.decode(stego_image)

# print("Extracted Message: ", decoded_msg)









# # pract7
# import secrets
# import string

# def generate_password(length: int) -> str:
#     """
#     Generate a secure random password of given length.

#     The password will contain:
#     - At least one lowercase letter
#     - At least one uppercase letter
#     - At least one digit
#     - At least one special character
#     """

#     if length < 4:
#         raise ValueError("Password length must be at least 4.")

#     # Character sets
#     lowercase = string.ascii_lowercase
#     uppercase = string.ascii_uppercase
#     digits = string.digits
#     special = string.punctuation

#     # Combine all characters
#     all_chars = lowercase + uppercase + digits + special

#     # Ensure password contains at least one of each type
#     password = [
#         secrets.choice(lowercase),
#         secrets.choice(uppercase),
#         secrets.choice(digits),
#         secrets.choice(special)
#     ]

#     # Fill remaining characters securely
#     password.extend(secrets.choice(all_chars) for _ in range(length - 4))

#     # Shuffle securely to remove pattern
#     secrets.SystemRandom().shuffle(password)

#     return ''.join(password)

# def main():
#     """
#     Main function to interact with the user and generate password.
#     """
#     print("=" * 50)
#     print("🔐 SECURE PASSWORD GENERATOR")
#     print("=" * 50)

#     while True:
#         try:
#             length = int(input("Enter desired password length (min 4): "))
#             password = generate_password(length)
#             break
#         except ValueError as e:
#             print(f"Error: {e}. Please try again.")

#     print("\n✅ Generated Password:")
#     print(password)
#     print("\n⚠️  Keep your password confidential and secure!")

# if __name__ == "__main__":
#     main()



# # pract9
# import hashlib
# # ==========================================
# # 1. SHA-256 Implementation
# # ==========================================
# # initializing string
# str_val = "Network Security"

# # encoding string using encode() then sending to SHA256()
# result = hashlib.sha256(str_val.encode())

# # printing the equivalent hexadecimal value.
# print("The hexadecimal equivalent of SHA256 is : ")
# print(result.hexdigest())
# print("\n")


# # ==========================================
# # 2. SHA-384 Implementation
# # ==========================================
# # initializing string
# str_val = "Cryptography"

# # encoding string using encode() then sending to SHA384()
# result = hashlib.sha384(str_val.encode())

# # printing the equivalent hexadecimal value.
# print("The hexadecimal equivalent of SHA384 is : ")
# print(result.hexdigest())
# print("\n")


# # ==========================================
# # 3. SHA-224 Implementation
# # ==========================================
# # initializing string
# str_val = "Cybersecurity"

# # encoding string using encode() then sending to SHA224()
# result = hashlib.sha224(str_val.encode())

# # printing the equivalent hexadecimal value.
# print("The hexadecimal equivalent of SHA224 is : ")
# print(result.hexdigest())
# print("\n")


# # ==========================================
# # 4. SHA-512 Implementation
# # ==========================================
# # initializing string
# str_val = "Hello World"

# # encoding string using encode() then sending to SHA512()
# result = hashlib.sha512(str_val.encode())

# # printing the equivalent hexadecimal value.
# print("The hexadecimal equivalent of SHA512 is : ")
# print(result.hexdigest())
# print("\n")















# # pract5

# # Symmetric Cryptography

# from cryptography.fernet import Fernet

# shared_key = Fernet.generate_key()

# fernet = Fernet(shared_key)

# message = "hello geeks"

# encMessage = fernet.encrypt(message.encode())

# print("original string: ", message)
# print("encrypted string: ", encMessage)

# decMessage = fernet.decrypt(encMessage).decode()

# print("decrypted string: ", decMessage)

## asymmetric cryptography
# import rsa

# publicKey, privateKey = rsa.newkeys(512)

# message = "This is a highly confidential message."
# print("Original string: ", message)

# encMessage = rsa.encrypt(message.encode(), publicKey)

# print("\nEncrypted string (Ciphertext):")
# print(encMessage)

# decMessage = rsa.decrypt(encMessage, privateKey).decode()

# print("\nDecrypted string (Plaintext):")
# print(decMessage)
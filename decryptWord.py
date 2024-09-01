import msoffcrypto
import itertools
from io import BytesIO
import scapy.all as scapy
from scapy import *
from art import *

tprint("Word Decryptor")
print("Word Unlocker Tool using provided base passwords by Toughrebel4041")
print("\n")

#Func to generate pass variations
def generate_variations(passwords):
    variations = set(passwords)
    
    for pwd in passwords:
        variations.add(pwd.lower())
        variations.add(pwd.upper())
        variations.add(pwd.capitalize())
        variations.add(pwd[::-1])  #Reversed
    
    return variations

#Func to unlock the Word file attempt
def try_passwords(file_path, passwords, output_file):
    for pwd in passwords:
        try:
            with open(file_path, "rb") as f:
                encrypted_file = msoffcrypto.OfficeFile(f)
                encrypted_file.load_key(password=pwd)
                
                decrypted = BytesIO()
                encrypted_file.decrypt(decrypted)

                with open(output_file, "wb") as out_file:
                    out_file.write(decrypted.getvalue())
                print(f"Success! The password is: {pwd}")
                return True
        except Exception as e:
            continue
    
    print("Failed to unlock the file with the provided passwords.")
    return False

#Main func
def main():
    base_passwords = input("Enter your base passwords separated by commas (e.g., password1,password2): ").split(',')
    file_path = input("Enter the name of the .docx file to decrypt (e.g., File.docx): ")
    output_file = input("Enter the desired name for the output file (e.g., Decrypted_File.docx): ")

    base_passwords = [pwd.strip() for pwd in base_passwords]

    all_passwords = generate_variations(base_passwords)

    try_passwords(file_path, all_passwords, output_file)

if __name__ == "__main__":
    main()

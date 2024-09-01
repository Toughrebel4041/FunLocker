import pikepdf
import itertools
import scapy.all as scapy
from scapy import *
from art import *

tprint("PDF Decryptor")
print("PDF File Unlocker Tool using provided base passwords by Toughrebel4041")
print("\n")

#Func to generate password variations
def generate_variations(passwords):
    variations = set(passwords)
    
    for pwd in passwords:
        variations.add(pwd.lower())
        variations.add(pwd.upper())
        variations.add(pwd.capitalize())
        variations.add(pwd[::-1])  # Reversed
    
    return variations
    
#Func to attempt decrypt password
def try_passwords(file_path, passwords, output_file):
    for pwd in passwords:
        try:
            with pikepdf.open(file_path, password=pwd) as pdf:
                pdf.save(output_file)
                print(f"Success! The password is: {pwd}")
                return True
        except pikepdf.PasswordError:
            continue
        except Exception as e:
            print(f"An error occurred: {e}")
            continue
    
    print("Failed to unlock the file with the provided passwords.")
    return False
    
#Main func
def main():
    base_passwords = input("Enter your base passwords separated by commas (e.g., password1,password2): ").split(',')
    file_path = input("Enter the name of the PDF file to decrypt (e.g., File.pdf): ")
    output_file = input("Enter the desired name for the output file (e.g., Decrypted_File.pdf): ")

    base_passwords = [pwd.strip() for pwd in base_passwords]

    all_passwords = generate_variations(base_passwords)

    try_passwords(file_path, all_passwords, output_file)

if __name__ == "__main__":
    main()


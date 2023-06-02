"""
CAESAR CIPHER
The key is an integer from 1 to 25.
This cipher rotates the letters of the alphabet (A to Z).
The encoding replaces each letter with the 1st to 25th next letter in the alphabet.
So key "2" encrypts "ABC" to "CDE" and "XYZ" to "ZAB".
"""

import sys


def main():
    # open and read file that has been specified in sys.argv or let user input text if no file has been specified
    if len(sys.argv) == 1:
        text = input_text()
    else:
        if sys.argv[1].endswith(".txt"):
            try:
                with open(sys.argv[1], "r") as textfile:
                    text = textfile.read().upper()
            except FileNotFoundError:
                print("File not found")
                sys.exit(1)
        else:
            print("Not a text file")
            sys.exit(1)
        
            
    encryptkey = input_key()
    mode = encrypt_decrypt()
    alphabet = make_dict()
    

    #encryption
    if mode == "encrypt":
        encrypttext = encrypt(text, encryptkey, alphabet)
        if len(sys.argv) == 1:
            print(encrypttext)
        else:
            with open(sys.argv[1].removesuffix(".txt") + "Encrypt.txt", "w") as textfile2:
                textfile2.write(encrypttext)
    
    
    #decryption        
    elif mode == "decrypt":
        decrypttext = decrypt(text, encryptkey, alphabet)
        if len(sys.argv) == 1:
            print(decrypttext)
        else:
            with open(sys.argv[1].removesuffix(".txt") + "Decrypt.txt", "w") as textfile2:
                textfile2.write(decrypttext)
    
    
    # reverse the operation
    rev = reverse()
    if rev == "yes":
        if mode == "encrypt":
            decrypttext = decrypt(encrypttext, encryptkey, alphabet)
            if len(sys.argv) == 1:
                print(decrypttext)
            else:
                with open(sys.argv[1].removesuffix(".txt") + "Decrypt.txt", "w") as textfile2:
                    textfile2.write(decrypttext)
        elif mode == "decrypt":
            encrypttext = encrypt(decrypttext, encryptkey, alphabet)
            if len(sys.argv) == 1:
                print(encrypttext)
            else:
                with open(sys.argv[1].removesuffix(".txt") + "Encrypt.txt", "w") as textfile2:
                    textfile2.write(encrypttext)
    else:
        sys.exit(0)
    
    
# input encryption key between 1 - 25
def input_key():
    count = 0
    while True:
        try:
            if count >= 5:
                print("Seriously? Just type a correct number already...")
            encryptkey = input("Give number between 1 and 25: ")
            if int(encryptkey) >= 1 and int(encryptkey) <= 25:
                return int(encryptkey)
            else:
                print("Please type a number between 1 and 25")
                count += 1
                continue
        except ValueError():
            continue
         
            
# choose mode encryption or decryption
def encrypt_decrypt():
    count = 0
    while True:
        try:
            if count >= 5:
                print("Seriously? Just type a correct mode already...")
            mode = input("Do you want to encrypt or decrypt? " ).strip().lower()
            if mode == "encrypt" or mode == "decrypt":
                return mode
            else:
                print("Please type encrypt or decrypt.")
                count += 1
                continue
        except ValueError():
            continue
    
    
# reverse the initial operation
def reverse():
    count = 0
    while True:
        try:
            if count >= 5:
                print("Seriously? Just type yes or no already...")
            rev = input("Do you want to reverse the process? yes/no ").strip().lower()
            if rev == "yes" or rev == "no":
                return rev
            else:
                print("Please type yes or no.")
                count += 1
                continue
        except ValueError():
            continue
      
        
# input text
def input_text():
    text = input("Give text to encrypt/decrypt: ").strip().upper()
    return text


# make dictionary with letters and number in alphabet
def make_dict():
    alphabet = {
        "A" : 1,
        "B" : 2,
        "C" : 3,
        "D" : 4,
        "E" : 5,
        "F" : 6,
        "G" : 7,
        "H" : 8,
        "I" : 9,
        "J" : 10,
        "K" : 11,
        "L" : 12,
        "M" : 13,
        "N" : 14,
        "O" : 15,
        "P" : 16, 
        "Q" : 17,
        "R" : 18,
        "S" : 19,
        "T" : 20,
        "U" : 21,
        "V" : 22,
        "W" : 23,
        "X" : 24,
        "Y" : 25,
        "Z" : 26   
    }
    return alphabet


# encrypt text
def encrypt(text, encryptkey, alphabet):
    encrypttext = ""
    for letter in text:
        if letter.isalpha() == False:
            key = letter
        else:    
            n = get_value(letter, alphabet)
            n = n + encryptkey
            if n > 26:
                n = n - 26
            key = get_key(n, alphabet)
        encrypttext += key
    return encrypttext


# decrypt text
def decrypt(text, encryptkey, alphabet):
    decrypttext = ""
    for letter in text:
        if letter.isalpha() == False:
            key = letter
        else:
            n = get_value(letter, alphabet)
            n = n - encryptkey
            if n <= 0:
                n = n + 26
            key = get_key(n, alphabet)
        decrypttext += key
    return decrypttext


# retrieve number in alphabet from given letter
def get_value(letter, alphabet):
    n = alphabet[letter]
    return n


#retrieve letter from given number in alphabet
def get_key(n, alphabet):
    key = list(filter(lambda x: alphabet[x] == n, alphabet))[0]
    return key
    
    
if __name__ == "__main__":
    main()

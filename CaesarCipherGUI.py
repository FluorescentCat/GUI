"""
CAESAR CIPHER
The key is an integer from 1 to 25.
This cipher rotates the letters of the alphabet (A to Z).
The encoding replaces each letter with the 1st to 25th next letter in the alphabet.
So key "2" encrypts "ABC" to "CDE" and "XYZ" to "ZAB".
"""

import sys
from guizero import App, Text, TextBox, ButtonGroup, Combo, CheckBox, PushButton, info


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



def encryptdecrypt(mode, MyText, encryptkey, alphabet):
    
    MyText = MyText.upper()
    encryptkey = int(encryptkey)
    
    # encryption is chosen
    if mode == "E":
        encrypttext = ""
        for letter in MyText:
            if letter.isalpha() == False:
                key = letter
            else:    
                n = get_value(letter, alphabet)
                n = n + encryptkey
                if n > 26:
                    n = n - 26
                key = get_key(n, alphabet)
            encrypttext += key
        result = encrypttext
        
    # decryption is chosen
    elif mode == "D":
        decrypttext = ""
        for letter in MyText:
            if letter.isalpha() == False:
                key = letter
            else:
                n = get_value(letter, alphabet)
                n = n - encryptkey
                if n <= 0:
                    n = n + 26
                key = get_key(n, alphabet)
            decrypttext += key
        result = decrypttext
        
    info("Result", f"{result}")
    
    

# retrieve number in alphabet from given letter
def get_value(letter, alphabet):
    n = alphabet[letter]
    return n


#retrieve letter from given number in alphabet
def get_key(n, alphabet):
    key = list(filter(lambda x: alphabet[x] == n, alphabet))[0]
    return key



def main():
    
    app = App(title="Caesar Cipher", width=600, height=300, layout="grid")
    
    WelcomeText = Text(app, text="Welcome to Caesar Cipher", size=20, font="Arial", color="lightblue", grid=[0,0], align="left")
    
    #TextType = Text(app, text="Do you want to type text or use a file to decrypt/encrypt? ", grid=[0,1], align="left")
    #TextTypeRadio = ButtonGroup(app, options=[["Text", "T"], ["File", "F"]], selected="T", horizontal=True, grid=[1,1], align="left")
    
    GiveText = Text(app, text="Please type your text: ", grid=[0,2], align="left")
    MyTextInput = TextBox(app, text="", width=30, grid=[1,2], align="left")
        
    #GiveFile = Text(app, text="Give file: ", grid=[0,3], align="left")
    #FileInput = TextBox(app, width=30, grid=[1,3], align="left")
        
    Choice = Text(app, text="Do you want do decrypt or encrypt? ", grid=[0,4], align="left")
    ChoiceRadio = ButtonGroup(app, options=[["Decryption", "D"], ["Encryption", "E"]], selected="E", horizontal=True, grid=[1,4], align="left")

    Key = Text(app, text="Please choose a key: ", grid=[0,5], align="left")
    KeyInput = Combo(app, options=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"], grid=[1,5], align="left")

    alphabet = make_dict()

        
        #if TextTypeRadio.value == "T":
    #MyText = str(MyTextInput.value)
            
        #elif TextTypeRadio.value == "F":
        #   if FileInput.value.endswith(".txt"):
        #      try:
        #         with open(FileInput.value, "r") as textfile:
            #            text = textfile.read().upper()
            #   except FileNotFoundError:
            #      print("File not found")
            #     sys.exit(1)
            #else:
            #   print("Not a text file")
            #  sys.exit(1)
    
    StartProcess = PushButton(app, command=lambda: encryptdecrypt(mode=ChoiceRadio.value, MyText=MyTextInput.value, encryptkey=KeyInput.value, alphabet=alphabet), text="Start encryption/decryption now", grid=[1,6], align="left")
    
    app.display()
        

    
    
if __name__ == "__main__":
    main()

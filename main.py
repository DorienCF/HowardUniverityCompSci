## Start UP
import functools
from colorama import Fore, Back, Style
import json
import time
from datetime import datetime
import os
import math



class Encryption: # This Class Will control the encrption of the data
    def __init__(self):
        self.hour = datetime.utcnow().hour;self.minute = datetime.utcnow().minute;self.seccond = datetime.utcnow().second
        print(f'The current UTC time is: {self.hour}:{self.minute}:{self.seccond}\n')
        print(f'Would you like to begin data preperation Yes or No?')
        DP_selection = input(">>")
        if DP_selection.upper() == "Yes" or "Y":
            Data_Preperation()
        elif DP_selection.upper() == "NO" or "N":
            exit()
        else:
            print("Error, you entered an incorrect phrase...")
        pass

class Data_Preperation(Encryption): # This class will organize the text into it's proper data structure for encryption
    def __init__(self):
        path = input("Enter the absolute path of the file you would like to encrypt\n>> ") # opening the .txt file
        self.s = open(path,'r')
        self.plaintext = self.s.read()
        self.seccond = datetime.utcnow().second
        cypher_text = open(f'{path}_encrypted.dor','x')
        cypher_text.write("[")
        #turning the .txt into ascii
        for x in range(len(self.plaintext)):
            loader = f'({ord(self.plaintext[x])},{self.seccond}),'
            cypher_text.write(loader)
            ##print(loader)
        ## Making the class generate a file
        cypher_text.write("]")



    def MESS_Encrypt(self):
        pass
    def RSA_Encrypt(self):
        pass
    def Preperation_and_submission(self):
        pass
    pass

class Decryption: # This class will control the decryption of the data
    def __init__(self):
        pass
    def RSA_Decrypt(self):
        pass
    def MESS_Decrypt(self):
        pass
    def Preperation_and_Submission(self):
        pass
    pass

### Program Selection zone _______________________________________________________________________________________________________
print("\t\t----------Welcome to the Program---------\n would you like to 'Encrypt', 'Decrypt' or 'Exit'?\n ")
selection = input(">> ")
if selection.upper() == 'DECRYPTION' or "D":
    ## this will be the decryption
    print(f'You entered {selection.upper()}\t Beginning Decryption...')
    Decryption()
elif selection.upper() == 'Encryption' or 'E':
    # This will be the Encryption
    print(f'You entered {selection.upper()}\nYou have chosen to encrypt ... Nice')
    Encryption()
else:
    print(f'you entered {selection.upper()}\nError: you have entered an invalid option ... please try agian. ')
    # this should return an
### ________________________________________________________________________________________________________________________

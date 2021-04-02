## Start UP
import functools
#from colorama import Fore, Back, Style
import json
import time
from datetime import date, datetime
import os
import math

#turning the .txt into ascii
'''
for x in range(len(self.plaintext)):
    loader = f'({ord(self.plaintext[x])},{self.seccond}),'
    cypher_text.write(loader)
    ##print(loader)
## Making the class generate a file
cypher_text.write("]")
'''
class Encryption(): # This Class Will control the encrption of the data ## uncer construction
    def __init__(self):
        self.hour = datetime.utcnow().hour;self.minute = datetime.utcnow().minute;self.seccond = datetime.utcnow().second
        print(f'The current UTC time is: {self.hour}:{self.minute}:{self.seccond}\n')
        self.cypher_txt = open(f'{path}_encrypted_temp.json','r+')
    
        self.long = 5219283133417550597608921138394131714748003987111696388844721857021695621345566328693730284546120701185550350229748838662252951341253421746795 # long prime number used later
    def MESS_Encrypt(self):
        #hour  = datetime.utcnow().hour; minit = datetime.utcnow().minute; sec = datetime.utcnow().seccond
        print(f'Time test\t Hour:{self.hour}\tMinute:{self.minute}\tsec:{self.seccond}')
        def upsil(long,):
            pass
        pass
    def RSA_Encrypt(self):
        def lcm(a,b):
            return abs(a*b)//math.gcd(a,b)
        p = 11; q = 7; n = p *q
        lam_n = lcm(p-1,q-1)
        e = 19
        d = e % n 
        #RSA_ENCRYPT =

        pass
    def Preperation_and_submission(self):
        pass
    pass

class Decryption: # This class will control the decryption of the data || under construction
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
print("\t\t----------Welcome to the Program---------\n ")

path = input("Enter the absolute path of the file you would like to encrypt\n>> ")
seccond = datetime.utcnow().second; minit = datetime.utcnow().minute; hour = datetime.utcnow().hour
s = open(path,'r'); plaintext = s.read()
selection = input("would you like to 'Encrypt', 'Decrypt' or 'Exit'?\n>> ")

if selection.upper() == 'DECRYPT' or selection.upper() == "D":
    ## this will be the decryption pathway
    print(f'You entered {selection.upper()}\t Beginning Decryption...Nice')
    Decryption()

elif selection.upper() == 'Encrypt' or selection.upper() == 'E':
    # This will be the Encryption pathway
    package = []
    print(f'You entered {selection.upper()}\nYou have chosen to encrypt ... Nice')
    with open(f'{path}_json_temp.json','w') as cypher_txt:
        data = []
        for i in range(len(plaintext)):
            data.append(ord(plaintext[i]))
            package = { 
            f'data_':data ,
            'Hour':f'{hour}',
            'Minute':f'{minit}',
            'Secconds':f'{seccond}'
             },
        json.dump(package,cypher_txt)
                            
                            
    cypher_txt.close()
    Encryption()
else:
    print(f'you entered {selection.upper()}\nError: you have entered an invalid option ... please try agian ')
    # this should return an
### _______________________________________________________________________________________________________________________________

 # opening the .txt file




#Basicly the section above creates the cypher text file and appends the 

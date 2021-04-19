## Start UP
import functools
#from colorama import Fore, Back, Style
import json
from datetime import date, datetime
import math
import Encryption_functions


class Encryption(): 
    def __init__(self):
        self.hour = datetime.utcnow().hour;self.minute = datetime.utcnow().minute;self.seccond = datetime.utcnow().second
        print(f'The current UTC time is: {self.hour}:{self.minute}:{self.seccond}\n')
        #self.cypher_txt = open(f'{path}_encrypted_temp.json','r+')
        f = open('test_Doc.txt_json_temp.json');data = json.load(f)
        g = open('ThetaList.json');Theta_list = json.load(g)

        Hour = data[0]["Hour"];Hour=int(Hour)
        Minute = data[0]['Minute'];Minute=int(Minute)
        Secconds=data[0]['Secconds'];Secconds=int(Secconds)
        self.cypher_txt =[]
        for i in range(len(data[0]['data_'])):				
            x = data[0]['data_'][i]
            y = Encryption_functions.MESS_Encrypt(x,Hour,Minute,Secconds)
            z = Encryption_functions.RSA_Encrypt(y)
            self.cypher_txt.append(z)
        # Preperation_and_Submission
        package = { 
            'data_':self.cypher_txt,
            'Hour':f'{hour}',
            'Minute':f'{minit}',
            'Secconds':f'{seccond}'
             },
        with open(f'{path}.encrypted.json','w') as h:
            json.dump(package,h)


class Decryption: # This class will control the decryption of the data || under construction
    def __init__(self):
        self.hour = datetime.utcnow().hour;self.minute = datetime.utcnow().minute;self.seccond = datetime.utcnow().second
        print(f'The current UTC time is: {self.hour}:{self.minute}:{self.seccond}\n')
        #self.cypher_txt = open(f'{path}_encrypted_temp.json','r+')
        f = open(path);data = json.load(f)
        g = open('ThetaList.json');Theta_list = json.load(g)
        Hour = data[0]["Hour"];Hour=int(Hour)
        Minute = data[0]['Minute'];Minute=int(Minute)
        Secconds=data[0]['Secconds'];Secconds=int(Secconds)
        self.cypher_txt =[]
        for i in range(len(data[0]['data_'])):				
            ## x,y,z calls all the nerd stuff from the other python file.
            x = data[0]['data_'][i]
            y = Encryption_functions.RSA_Decrypt(x)
            z=  Encryption_functions.MESS_Decrypt(y,Hour,Minute,Secconds)
            print(x,y,z)
            self.cypher_txt.append(z)
        # Preperation_and_Submission
        with open(f'{path}.txt','w') as h:
            for i in range(len(self.cypher_txt)):
                #h.write(chr(self.cypher_txt[i]))
                json.dump(self.cypher_txt[i])
        


print("\t\t----------Welcome to the Program---------\n")

path = input("Enter the absolute path of the file you would like to encrypt or decrypt\n>> ")

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
    ## pretty much data prep.. kinda boring
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


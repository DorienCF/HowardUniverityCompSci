# HowardUniverityCompSci
<h2>This is a repository of the semester project for CSCI-136</h2>
____________________________________________________
<p>This respository will contain the code and nessicary documentation for my Computer Science II project. </p> 
  <p> This project is currently in progress and will be updated periodicaly.</p>

____________________________________________________
<h2> Project Test Plan01:</h2>
Prior to runinng the program you will need to have a .txt file and enough space to store one .json file.
this program is NOT 100% operable and therefor it is not set to encrypt or decrypt messages. In this phase
the main effort is to build the cypher dataframe metioned in phase III. This is the biggest section of the 
project since with out it no message can be processed. 

- Procedure to test.

1.) Run the  .py file in an interpeter
2.) enter the path of the .txt file that you wish to test
3.) **important** enter e or encrypt (not case sensitive). the Decryption function is under construction.

After this you should find a file named "____json_temp.json" this is the dataframe. I have not found a solution to run the 
program in memory so I am using json current. 

Uppon completion you will recive an error message along the lines:

      self.cypher_txt = open(f'{path}_encrypted_temp.json','r+')
FileNotFoundError: [Errno 2] No such file or directory: 'test_Doc.txt_encrypted_temp.json'

This is normal, please see the json file which will house the data waiting to be encrypted. 
This format is identitcal to the encryped and decrypted informatiton. 
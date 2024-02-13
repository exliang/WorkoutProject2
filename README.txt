
Author: Emily Liang 
Email: exliang@uci.edu

Project Description: This project uses the Python programming language, multiple methods, loops, lists, and branching to create a program for users to encrypt and decrypt data from a text file using command line arguments. 3 modules are used: wp2.py (includes the main function and calls the encrypt and decrypt functions in cryptography.py), cryptography.py has the encrypy and decrypt functions, and key.py includes a private function that checks if the key inputted from the user is valid. In the encrypt and decrypt functions, the file is first opened and read, then the text is put into a matrix that is transposed, then using concatenation the new text is formed and written to the output file.

How to run this software: Type py (or python) -e w2.py originaltext.txt encryptedtext.txt key and py (or python) -d w2.py encryptedtext.txt decryptedtext.txt key in the Command Line/Windows Powershell/Terminal/Git Bash.

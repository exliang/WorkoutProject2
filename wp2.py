
# Emily Liang
# exliang@uci.edu
# 79453973

import sys
import cryptography 
import key


def main():

    option = sys.argv[1]  # either -e or -d
    file_input = sys.argv[2]
    file_output = sys.argv[3]
    key_value = sys.argv[4]

    # validate the key first
    if key.Key()._Key__key(key_value):  # calling the private key method in key.py
        if option == '-e':
            cryptography.encryption(file_input, file_output, int(key_value))
        elif option == '-d':
            cryptography.decryption(file_input, file_output, int(key_value))
        else:
            print("Invalid option: must type -e or -d. Try again.")
    else:  # invalid key
    	print("Invalid key: must be an integer. Try again.")


if __name__ == '__main__':
	main()

# Citations:
# - https://stackoverflow.com/questions/40852686/calling-a-private-class-member-function-in-python-from-another-module

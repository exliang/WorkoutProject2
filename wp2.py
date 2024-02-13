
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
    key = sys.argv[4]

    key.Key()  # validate the key first
    if option == '-e':
    	cryptography.encryption(file_input, file_output, key)
    elif option == '-d':
    	cryptography.decryption(file_input, file_output, key)
    else:
    	print("Invalid option: must type -e or -d. Try again.")


if __name__ == '__main__':
	main()


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
    key_val = sys.argv[4]

    # validate the key first
    try:
        if key.Key()._Key__key(key_val):  # call private key method in key.py
            if option == '-e':
                cryptography.encryption(file_input, file_output, int(key_val))
            elif option == '-d':
                cryptography.decryption(file_input, file_output, int(key_val))
            else:
                print("Invalid option: must type -e or -d. Try again.")
    except key.InvalidKeyException:  # invalid key
        print("Invalid key: must be an integer. Try again.")


if __name__ == '__main__':
    main()

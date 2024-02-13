# Emily Liang
# exliang@uci.edu
# 79453973

import math


def encryption(file_input, file_output, key_value):
    f = open(file_input, "r")  # open original text file to read
    text = f.read()  # read the text

    # put text in a matrix (2D list) using key
    matrix = []
    row = []
    for i in range(len(text)):
        if i + 1 == key_value or ((i + 1) % key_value == 0 and key_value < i):  # i = key_value or a multiple of key_value
            row.append(text[i])
            matrix.append(row)
            row = []
        elif text[i] == text[len(text)-1]:  # reached end of matrix
            row.append(text[i])
            matrix.append(row)
        else:  # i is any num in besides key_value or a multiple of key_value
            row.append(text[i])
    if len(matrix[len(matrix)-2]) != len(matrix[len(matrix)-1]):  # last row in matrix has empty spots
    	while len(matrix[len(matrix)-1]) < len(matrix[len(matrix)-2]):
    		matrix[len(matrix)-1].append("#")  # add a hashtag in place of the empty spots
    # printing_matrix(matrix) #DELETE AFTER TESTING

    # transpose the matrix using key
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    # printing_matrix(transposed_matrix) #DELETE AFTER TESTING

    # put text back into string format
    encrypted_text = ""
    for row in transposed_matrix:
        for col in row:
            if col != "#":
                encrypted_text += col

    # write the encrypted text to encryptedtext.txt
    f = open(file_output, "w")
    f.write(encrypted_text)


def decryption(file_input, file_output, key_value):
	pass


def printing_matrix(matrix): #DELETE AFTER PROGRAM WORKS
	for row in matrix:
		print(row)

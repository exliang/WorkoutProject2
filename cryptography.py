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
        # i = key_value or a multiple of key_value
        if i + 1 == key_value or ((i + 1) % key_value == 0 and key_value < i):
            row.append(text[i])
            matrix.append(row)
            row = []
        elif text[i] == text[len(text)-1]:  # reached end of matrix
            row.append(text[i])
            matrix.append(row)
        else:  # i is any num in besides key_value or a multiple of key_value
            row.append(text[i])
    # last row in matrix has empty spots
    if len(matrix[len(matrix)-2]) != len(matrix[len(matrix)-1]):
        while len(matrix[len(matrix)-1]) < len(matrix[len(matrix)-2]):
            # add a hashtag in place of the empty spots
            matrix[len(matrix)-1].append("#")

    # transpose the matrix using key
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

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
    f = open(file_input, "r")  # open original text file to read
    text = f.read()  # read the text

    num_cols = math.ceil(len(text) / key_value)
    matrix_spots = key_value * num_cols  # key_value = num rows
    emtpy_positions = matrix_spots - len(text)  # pos that shouldnt be filled

    # intialize matrix w/correct cols & rows
    matrix = [[0 for _ in range(num_cols)] for _ in range(key_value)]
    bottom_col = num_cols - 1
    bottom_row = key_value - 1

    # go up empty positon times, decrease row
    while emtpy_positions > 0:
        matrix[bottom_row][bottom_col] = "~~"
        emtpy_positions -= 1
        bottom_row -= 1

    i = 0
    for row in range(key_value):
        for col in range(num_cols):
            if matrix[row][col] == "~~":
                continue
            else:
                matrix[row][col] = text[i]
                i += 1

    # transpose the matrix using key
    transposed_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    # put text back into string format
    decrypted_text = ""
    for row in transposed_matrix:
        for col in row:
            if col != "~~":
                decrypted_text += col

    # write the decrypted text to decryptedtext.txt
    f = open(file_output, "w")
    f.write(decrypted_text)

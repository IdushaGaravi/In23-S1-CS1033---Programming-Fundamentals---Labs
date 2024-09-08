# Exercise L5.E4

matrix = []
len_rows = []

def get_matrix():
    ''' build a matrix using user inputs'''
    while True:
        try:
            row = input()
            if row == '-1':     # stop accepting the rows when -1 is entered as the input
                break

            row_elements = row.split()
            row_length = len(row_elements)
            len_rows.append(row_length)
            
            lst = list(map(int, row_elements))      # Use a 2D (two-dimensional) list to store the matrix
            matrix.append(lst)

        except ValueError:      # checking the invalid rows with an inconsistent number of elements
            print('Error')
            return

    set_row = set(len_rows)
    
    if len(set_row) != 1:       # for invalid rows with an inconsistent number of elements
        print('Invalid Matrix')     #Print “Invalid Matrix” as the error message
        return
    else:
        return matrix

matrix = get_matrix()

if matrix:
    transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]     # get transpose
    for row in transpose:
        print(' '.join(map(str, row)))      # print final matrix

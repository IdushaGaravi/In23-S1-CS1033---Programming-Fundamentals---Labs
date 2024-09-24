INPUT_FILE_NAME = input()
########################################################################################
# Do not change anything above this line
########################################################################################

# Use INPUT_FILE_NAME variable to read the file instead of 'matrix_data.txt'
# Enter your code here

def read_matrix_data_from_input_file(INPUT_FILE_NAME):
    """read matrix data from the user input file"""
    with open(INPUT_FILE_NAME, 'r') as input_file:      # open input file, read and close it
        initial_data = list(input_file.read().strip().split('\n'))
        return initial_data

def get_Minor_of_matrix(matrix_list, row, col):
    """ get minors of the matrix"""
    minor = [r[:col] + r[col+1:] for r in (matrix_list[:row] + matrix_list[row+1:])]
    return minor

def get_cofactor(matrix_list, row, col):
    """get cofactor corresponding to each minor"""
    minor = get_Minor_of_matrix(matrix_list, row, col)
    if (row + col)%2==0:        # multiply the determinant of each minor by + or - to get the cofactor
       cofactor = compute_determinant_of_matrix(minor)
    else:    
        cofactor = (-1) * (compute_determinant_of_matrix(minor))
    return cofactor

def get_transpose_matrix(matrix):
    """get the transpose of a given matrix"""
    transpose = [[matrix[m][n] for m in range(len(matrix))] for n in range(len(matrix[0]))]
    return transpose

def adjoint_matrix(matrix_list):
    """ compute the cofactor matrix and get adjoint matrix"""
    all_minors_cofactors = []
    for row in range(len(matrix_list)):
        row_minors_cofactors = []
        for col in range(len(matrix_list[0])):
            minor_cofactor = get_cofactor(matrix_list, row, col)
            row_minors_cofactors.append(minor_cofactor)
        all_minors_cofactors.append(row_minors_cofactors)       # get all cofactors

    transpose_of_all_cofactors = get_transpose_matrix(all_minors_cofactors)     # get the adjoint of cofactor matrix to build adjoint matrix
    return transpose_of_all_cofactors

def compute_determinant_of_matrix(matrix_list):
    """ calculate the determinant of the matrix"""
    if len(matrix_list) == 1:       # gat base case as 1x1 matrix
        return matrix_list[0][0]
    
    determinant = 0
    for k in range(len(matrix_list)):
        minor = get_Minor_of_matrix(matrix_list, 0, k)
        determinant += (matrix_list[0][k])*((-1)**(k)) * (compute_determinant_of_matrix(minor))
    return determinant

def compute_Inverse_matrix(adjoint_matrix, determinant):
    """ get inverse of the given matrix by using adjoint and the determinant"""
    inverse_matrix = []
    for row in adjoint:
        inverse_row = []
        for col in row:
            calculation = int(col)/int(determinant)
            if calculation == 0.0:
                calculation = 0
            inverse_row.append(calculation)
        inverse_matrix.append(inverse_row)
    return inverse_matrix
    
def display_resultant_inverse_matrices(inverse_matrix):
    """display the inverse matrix in given form"""
    formatted_rows = []
    for row in inverse:
        formatted_row = "".join(f"{elem:7.2f}" for elem in row) # when printing each row of the inverse matrix, use field width:7 and precision:2 to format each element of the row
        formatted_rows.append(formatted_row)
    return "\n".join(formatted_rows)

if __name__ == '__main__':      # run the file as main script
    get_input = read_matrix_data_from_input_file(INPUT_FILE_NAME)

    no_of_matrices = int(get_input[0])
    matrix_data = get_input[1:]

    i = 0  # Get each matrix from the input
    for n in range(no_of_matrices):
        matrix_list = []
        matrix_size = int(matrix_data[i])
        matrix = matrix_data[i + 1: i + 1 + matrix_size]
        for lines in matrix:
            matrix_list.append([float(num) for num in lines.split(',')])
        
        adjoint = adjoint_matrix(matrix_list)       # get adjoint matrix of the given matrix
        determinant = compute_determinant_of_matrix(matrix_list)    # calculate determinant of the given matrix
        
        inverse = compute_Inverse_matrix(adjoint, determinant)      # get the inverse_matrix of the matrix
        result = display_resultant_inverse_matrices(inverse)        # display the inverse mattrix in given form
        print(f'Inverse of Matrix {n+1}:')
        print(result)
        i += matrix_size  +1
    

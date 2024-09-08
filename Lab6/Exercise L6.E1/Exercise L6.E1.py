# Exercise L6.E1

def matrix():
    ''' get matrix A and B from the user'''
    M = []
    try:
        for r in range(row):
            row_M = list(map(int, input().split()))
            if len(row_M) != column:
                return 'Invalid Matrix'
            M.append(row_M)
        return M
    except ValueError:
        return 'Error'

def transpose(transpose_matrix):
    ''' get transpose matrix of B'''
    return [[B[j][k] for j in range(len(B))] for k in range(len(B[0]))]

def multiplication(A, B_transpose):
    ''' do matrix multiplication with A and transpose of B'''
    if column != len(B_transpose):      # check whether conditions are true for matrix multiplication
        print('Error')
        return None
    else:
        result = [[sum(a*b for a,b in zip(row_A, column_B_transpose)) for column_B_transpose in zip(*B_transpose)] for row_A in A]      # do matrix multiplication
        return result

def final_result(multiplied_result):
    ''' check whether multiplied matrix is not null.
        get the output in given form'''
    if multiplied_result!= None:
        for row in multiplied_result:       # print result in given form
            for col in row:
                print(col,end=' ')
            print()
    
if __name__ == '__main__':
    row, column = map(int, input('Enter the dimension: ').split(','))      # get number of rows and columns
    print('Enter Matrix A: ')
    A = matrix()
    if A == 'Invalid Matrix':
        print('Invalid Matrix')
    elif A == 'Error':
        print('Error')
    else:
        print('Enter Matrix B: ')
        B = matrix()

        if B == 'Invalid Matrix':
            print('Invalid Matrix')
        elif B == 'Error':
            print('Error')
        else:
            B_transpose = transpose(B)      # call transpose function
            multiplied_result = multiplication(A, B_transpose)      # call multiplication function
            final_matrix = final_result(multiplied_result)      # call final_result function
            final_matrix

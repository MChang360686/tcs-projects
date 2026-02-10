
def build_matrix():
    rows = int(input('Enter number of rows '))
    cols = int(input('Enter number of cols '))

    result = []
    for i in range(rows):
        l = []
        for j in range(cols):
            l.append(' ')
        result.append(l)

    return result

# Start with multiplying 2x2 matrices
def matrix_mult(a, b):
    if len(a[0]) == len(b) and len(a) == 2 and len(b) == 2:
        result = [[0, 0], [0, 0]]
        result[0][0] = a[0][0] * b[0][0] + a[0][1] * b[1][0]
        result[0][1] = a[0][0] * b[1][0] + a[0][1] * b[1][1]
        result[1][0] = a[1][0] * b[0][0] + a[1][1] * b[1][0]
        result[1][1] = a[1][1] * b[0][1] + a[1][1] * b[1][1]
        return result
    else:
        return 'Undefined matrices '
    
def print_matrix(matrix):
    for row in matrix:
        print(row)
    
print_matrix(matrix_mult([[2, 1], [80, 9]], [[1, 0], [0, 1]]))

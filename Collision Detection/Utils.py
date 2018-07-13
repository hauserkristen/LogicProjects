def create_2D_matrix(num_rows, num_cols):
    matrix = []
    for r in xrange(0,num_rows):
        matrix.append([])
        for c in xrange(0,num_cols):
            matrix[r].append(0.0)
    return matrix

def create_vector(length):
    vector = []
    for r in xrange(0,length):
        vector.append(0.0)
    return vector

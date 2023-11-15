def rotate_image(matrix) -> None:
    #Solution beats 97.51% on runtime (only 16.39% on memory, but that's ok)
    half_size = len(matrix) // 2 if len(matrix) % 2 == 0 else len(matrix) // 2 + 1
    for i in range(0, half_size):
        temp = matrix[i]
        matrix[i] = matrix[len(matrix) - 1 - i]
        matrix[len(matrix) - 1 - i] = temp
    #Matrix is now flipped vertically
    Three = 3
    offset = 1
    for i in range(0, len(matrix)):
        for j in range(i, len(matrix)):
            if i == j:
                continue
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    three = 3
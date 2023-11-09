def gauss_elimination(A, b):
    n = len(b)

    for i in range(n):
        # Find the pivot element
        max_row = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[max_row][i]):
                max_row = j
        A[i], A[max_row] = A[max_row], A[i]
        b[i], b[max_row] = b[max_row], b[i]

        # Make the diagonal elements 1
        pivot = A[i][i]
        for j in range(i, n):
            A[i][j] /= pivot
        b[i] /= pivot

        # Eliminate the entries below the pivot
        for j in range(i + 1, n):
            factor = A[j][i]
            for k in range(i, n):
                A[j][k] -= factor * A[i][k]
            b[j] -= factor * b[i]

    # Back-substitution to find the roots
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]

    return x

print("Enter the element one by one by pressing enter in row format.\n")

print("For Matrix A\n")
A = [[float(input("Enter the element :")) for _ in range(3)] for _ in range(3)]

# Get user input for vector b
print("For Matrix b\n")
b = [float(input()) for _ in range(3)]

roots = gauss_elimination(A, b)
print("Roots:", roots)

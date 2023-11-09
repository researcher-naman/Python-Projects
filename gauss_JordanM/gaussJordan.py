def print_matrix(A, b):
    n = len(b)
    for i in range(n):
        row = [f"{A[i][j]:.2f}" for j in range(n)]
        print(f"{row} | {b[i]:.2f}")

def gauss_jordan_elimination(A, b):
    n = len(b)

    for i in range(n):
        # Find the pivot element
        pivot = A[i][i]

        # Make the diagonal elements 1
        for j in range(n):
            A[i][j] /= pivot
        b[i] /= pivot

        print(f"\nStep {i + 1}:")
        print_matrix(A, b)
        print("\n")

        # Eliminate the entries above and below the pivot
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n):
                    A[k][j] -= factor * A[i][j]
                b[k] -= factor * b[i]

    return b

print("Enter the elements one by one by pressing enter in row format.\n")

print("For Matrix A\n")
A = [[float(input("Enter the element: ")) for _ in range(3)] for _ in range(3)]
print("\n")
# Get user input for vector b
print("For Matrix b\n")
b = [float(input("Enter the element: ")) for _ in range(3)]

print("\nInitial Augmented Matrix:")
print_matrix(A, b)
print("\n")

solutions = gauss_jordan_elimination(A, b)
print("\nFinal Augmented Matrix:")
print_matrix(A, solutions)
print("\nSolutions:", solutions)

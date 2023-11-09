def print_matrix_iteration(iteration, A, b):
    print(f"Iteration {iteration + 1} Augmented Matrix:")
    for i in range(len(b)):
        row = [f"{A[i][j]:.2f}" for j in range(len(b))]
        print(f"{row} | {b[i]:.2f}")
    print("\n")

def print_iteration(iteration, x):
    print(f"Iteration {iteration + 1}: {x}")

def gauss_seidel_method(A, b, initial_guess=None, max_iterations=100):
    n = len(b)
    x = initial_guess or [0] * n

    for iteration in range(max_iterations):
        prev_x = x.copy()

        for i in range(n):
            sum_ax = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_ax) / A[i][i]

        print_iteration(iteration, x)

        # Check for convergence
        if all(abs(x[i] - prev_x[i]) < 1e-4 for i in range(n)):
            break

    return x

# Your matrix and vector
A = [[1, 1, 1], [1, 3, 1], [1, 2, 2]]
b = [7, 13, 13]

initial_guess = [0] * len(b)
solutions = gauss_seidel_method(A, b, initial_guess)

print("\nFinal Solutions:")
print(solutions)

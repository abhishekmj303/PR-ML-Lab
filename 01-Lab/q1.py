import numpy as np

def input_matrix(m, n):
    A = []
    for i in range(m):
        row = list(map(int, input().split()))
        if len(row) != n:
            raise ValueError("Invalid number of elements in row")
        A.append(row)
    return np.array(A)

print("Operations related to Matrix:")
print("  1. Matrix Addition")
print("  2. Matrix Subtraction")
print("  3. Scalar Matrix Multiplication")
print("  4. Elementwise Matrix Multiplication")
print("  5. Matrix Multiplication")
print("  6. Matrix Transpose")
print("  7. Trace of a Matrix")
print("  8. Solve System of Linear Equations")
print("  9. Determinant")
print(" 10. Inverse")
print(" 11. Eigen Value and Eigen Vector")
print(" 12. Exit")

while True:
    opt = int(input("\nEnter your choice: "))
    if opt == 12:
        print("Exiting...")
        break
    
    m1, n1 = map(int, input("\nEnter space-separated dimension of matrix (m x n): ").split())

    if opt in (7, 9, 10, 11):
        if m1 != n1:
            print("Invalid dimensions: Square matrix required")
            continue

    if opt in (1, 2, 4):
        m2, n2 = m1, n1
    elif opt == 5:
        m2, n2 = map(int, input("\nEnter space-separated dimension of another matrix (n x l): ").split())
        if n1 != m2:
            print("Invalid dimensions: Matrix Multiplication not possible")
            continue

    print("Enter the elements of matrix A: ")
    try:
        mat1 = input_matrix(m1, n1)
    except ValueError as e:
        print(e)
        continue

    if opt in (1, 2, 4, 5):
        print("Enter the elements of matrix B: ")
        try:
            mat2 = input_matrix(m2, n2)
        except ValueError as e:
            print(e)
            continue
    
    if opt == 1:
        print("Matrix Addition: ")
        print(mat1 + mat2)
    
    elif opt == 2:
        print("Matrix Subtraction: ")
        print(mat1 - mat2)
    
    elif opt == 3:
        scalar = int(input("Enter the scalar value: "))
        print("Scalar Matrix Multiplication: ")
        print(mat1 * scalar)
    
    elif opt == 4:
        print("Elementwise Matrix Multiplication: ")
        print(mat1 * mat2)
    
    elif opt == 5:
        print("Matrix Multiplication: ")
        print(np.matmul(mat1, mat2))
    
    elif opt == 6:
        print("Matrix Transpose: ")
        print(mat1.T)
    
    elif opt == 7:
        print("Trace of a Matrix: ", end="")
        print(np.trace(mat1))
    
    elif opt == 8:
        b = np.array(list(map(int, input(f"Enter the elements of vetcor b (len={m1}): ").split())))
        if len(b) != m1:
            print("Invalid Dimensions: len(b) != m")
            continue
        print("Solve System of Linear Equations: ")
        print(np.linalg.solve(mat1, b))
    
    elif opt == 9:
        print("Determinant: ", end="")
        print(np.linalg.det(mat1))
    
    elif opt == 10:
        print("Inverse: ")
        print(np.linalg.inv(mat1))
    
    elif opt == 11:
        result = np.linalg.eig(mat1)
        print("Eigen Values: ", result.eigenvalues)
        print("Eigen Vectors: ", result.eigenvectors)

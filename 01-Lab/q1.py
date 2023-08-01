import numpy as np

def input_matrix(m, n):
    A = []
    for i in range(m):
        row = list(map(int, input().split()))
        if len(row) != n:
            raise ValueError("Invalid number of elements in row")
        A.append(row)
    return np.array(A)


print("Welcome to Matrix Calculator")

m1, n1 = map(int, input("\nDimensions of Matrix A (space-separated): ").split())
print(f"Enter the elements of Matrix A ({n1}-col, {m1}-row): ")
mat1 = input_matrix(m1, n1)

m2, n2 = map(int, input("\nDimensions of Matrix B (space-separated): ").split())
print(f"Enter the elements of Matrix B ({n2}-col, {m2}-row): ")
mat2 = input_matrix(m2, n2)

print("\nOperations related to Matrix:")
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

    if opt in (1, 2, 4):
        if m1 != m2 or n1 != n2:
            print("Invalid dimensions: Dimensions of both matrices must be same")
            continue
    # elif opt in (7, 9, 10, 11):
    #     if m1 != n1:
    #         print("Invalid dimensions: Square matrix required")
    #         continue
    elif opt == 5:
        if n1 != m2:
            print("Invalid dimensions: Matrix Multiplication not possible")
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
        print("Matrix A:", scalar * mat1, sep="\n")
        print("Matrix B:", scalar * mat2, sep="\n")
    
    elif opt == 4:
        print("Elementwise Matrix Multiplication: ")
        print(mat1 * mat2)
    
    elif opt == 5:
        print("Matrix Multiplication: ")
        print(np.matmul(mat1, mat2))
    
    elif opt == 6:
        print("Matrix Transpose: ")
        print("Matrix A:", mat1.T, sep="\n")
        print("Matrix B:", mat2.T, sep="\n")
    
    elif opt == 7:
        print("Trace of a Matrix:")
        print("Matrix A: ", end="")
        if m1 == n1:
            print(np.trace(mat1))
        else:
            print("Not a Square Matrix")
        print("Matrix B: ", end="")
        if m2 == n2:
            print(np.trace(mat2))
        else:
            print("Not a Square Matrix")
    
    elif opt == 8:
        print("Solve System of Linear Equations:")
        print("\nFor Matrix A: ")
        if m1 != n1:
            print("Solution not possible: m != n")
            continue
        b = np.array(list(map(int, input(f"Enter the elements of vetcor b (len={m1}): ").split())))
        if len(b) != m1:
            print("Invalid Dimensions: len(b) != m")
        else:
            print("Solution:", np.linalg.solve(mat1, b))
        print("\nFor Matrix B: ")
        if m2 != n2:
            print("Solution not possible: m != n")
            continue
        b = np.array(list(map(int, input(f"Enter the elements of vetcor b (len={m2}): ").split())))
        if len(b) != m2:
            print("Invalid Dimensions: len(b) != m")
        else:
            print("Solution:", np.linalg.solve(mat2, b))
    
    elif opt == 9:
        print("Determinant:")
        print("Matrix A: ", end="")
        if m1 == n1:
            print(np.linalg.det(mat1))
        else:
            print("Not a Square Matrix")
        print("Matrix B: ", end="")
        if m2 == n2:
            print(np.linalg.det(mat2))
        else:
            print("Not a Square Matrix")
    
    elif opt == 10:
        print("Inverse: ")
        print("Matrix A: ")
        if m1 == n1:
            print(np.linalg.inv(mat1))
        else:
            print("Not a Square Matrix")
        print("Matrix B: ")
        if m2 == n2:
            print(np.linalg.inv(mat2))
        else:
            print("Not a Square Matrix")
    
    elif opt == 11:
        print("Eigen Value and Eigen Vector: ")
        print("Matrix A: ")
        if m1 != n1:
            print("Not a Square Matrix")
        else:
            result = np.linalg.eig(mat1)
            print("Eigen Values: ", result.eigenvalues)
            print("Eigen Vectors: ", result.eigenvectors)
        print("Matrix B: ")
        if m2 != n2:
            print("Not a Square Matrix")
        else:
            result = np.linalg.eig(mat2)
            print("Eigen Values: ", result.eigenvalues)
            print("Eigen Vectors: ", result.eigenvectors)

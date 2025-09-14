import numpy as np

def input_matrix():
    """Takes user input to create a matrix"""
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    print(f"Enter elements row by row (space-separated, total {rows * cols} elements):")
    
    elements = []
    for i in range(rows):
        row = list(map(float, input(f"Row {i+1}: ").split()))
        while len(row) != cols:
            print(f"❌ You must enter exactly {cols} elements!")
            row = list(map(float, input(f"Row {i+1}: ").split()))
        elements.append(row)
    
    return np.array(elements)

def display_matrix(matrix, name="Result"):
    """Displays matrix in structured format"""
    print(f"\n{name}:")
    print(matrix)

def matrix_operations():
    print("=== Matrix Operations Tool ===")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Transpose")
    print("5. Determinant")
    print("6. Exit")
    
    while True:
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            print("\n--- Matrix Addition ---")
            print("Matrix A:")
            A = input_matrix()
            print("Matrix B:")
            B = input_matrix()
            if A.shape == B.shape:
                display_matrix(A + B, "A + B")
            else:
                print("❌ Matrices must have the same dimensions for addition!")
        
        elif choice == "2":
            print("\n--- Matrix Subtraction ---")
            print("Matrix A:")
            A = input_matrix()
            print("Matrix B:")
            B = input_matrix()
            if A.shape == B.shape:
                display_matrix(A - B, "A - B")
            else:
                print("❌ Matrices must have the same dimensions for subtraction!")
        
        elif choice == "3":
            print("\n--- Matrix Multiplication ---")
            print("Matrix A:")
            A = input_matrix()
            print("Matrix B:")
            B = input_matrix()
            if A.shape[1] == B.shape[0]:
                display_matrix(np.dot(A, B), "A × B")
            else:
                print("❌ Number of columns in A must equal number of rows in B for multiplication!")
        
        elif choice == "4":
            print("\n--- Matrix Transpose ---")
            A = input_matrix()
            display_matrix(A.T, "Transpose of A")
        
        elif choice == "5":
            print("\n--- Determinant ---")
            A = input_matrix()
            if A.shape[0] == A.shape[1]:
                display_matrix(np.linalg.det(A), "Determinant of A")
            else:
                print("❌ Determinant can only be calculated for square matrices!")
        
        elif choice == "6":
            print("✅ Exiting Matrix Operations Tool. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again!")

if __name__ == "__main__":
    matrix_operations()

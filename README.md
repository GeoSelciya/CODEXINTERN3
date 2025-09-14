🧮 Matrix Operations Tool

A simple Python CLI application built with NumPy that allows users to perform common matrix operations interactively.

🚀 Features

Matrix Addition

Matrix Subtraction

Matrix Multiplication

Matrix Transpose

Matrix Determinant Calculation

Interactive menu-driven interface

Validations for dimensions and square matrices

📂 Project Structure
matrix_operations.py   # Main Python script
README.md              # Project documentation

⚙️ Requirements

Python 3.8+

NumPy library

Install NumPy if not already installed:

pip install numpy

▶️ How to Run

Clone or download this project.

Open the project folder in VS Code or any terminal.

Run the script:

python matrix_operations.py

📝 Usage Example

Menu:

=== Matrix Operations Tool ===
1. Addition
2. Subtraction
3. Multiplication
4. Transpose
5. Determinant
6. Exit


Sample Run (Matrix Addition):

Enter your choice (1-6): 1

--- Matrix Addition ---
Matrix A:
Enter number of rows: 2
Enter number of columns: 2
Enter elements row by row (space-separated):
Row 1: 1 2
Row 2: 3 4
Matrix B:
Enter number of rows: 2
Enter number of columns: 2
Enter elements row by row (space-separated):
Row 1: 5 6
Row 2: 7 8

A + B:
[[ 6.  8.]
 [10. 12.]]

📌 Notes

For addition/subtraction, matrices must have the same dimensions.

For multiplication, the number of columns in A must equal the number of rows in B.

Determinant is only valid for square matrices.

🏆 Author

Developed as a Python practice project using NumPy for efficient matrix operations.

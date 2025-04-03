#include <iostream>
#include <vector>
#include <iomanip> // For setting precision

using namespace std;

// Function to multiply two matrices
vector<vector<float>> multiplyMatrices(const vector<vector<float>>& A, const vector<vector<float>>& B) {
    int rowsA = A.size();
    int colsA = A[0].size();
    int rowsB = B.size();
    int colsB = B[0].size();

    // Check if matrices can be multiplied
    if (colsA != rowsB) {
        cerr << "Error: Number of columns in A must equal the number of rows in B." << endl;
        exit(1);
    }

    // Initialize the result matrix with zeros
    vector<vector<float>> result(rowsA, vector<float>(colsB, 0.0));

    // Matrix multiplication
    for (int i = 0; i < rowsA; ++i) {
        for (int j = 0; j < colsB; ++j) {
            for (int k = 0; k < colsA; ++k) {
                result[i][j] += A[i][k] * B[k][j];
            }
        }
    }

    return result;
}

// Function to compute the transpose of a matrix
vector<vector<double>> transposeMatrix(const vector<vector<double>>& matrix) {
    int rows = matrix.size();
    int cols = matrix[0].size();

    // Initialize the transpose matrix
    vector<vector<double>> transpose(cols, vector<double>(rows, 0.0));

    // Compute the transpose
    for (int i = 0; i < rows; ++i) {
        for (int j = 0; j < cols; ++j) {
            transpose[j][i] = matrix[i][j];
        }
    }

    return transpose;
}

// Function to print a matrix
void printMatrix(const vector<vector<float>>& matrix) {
    for (const auto& row : matrix) {
        for (float val : row) {
            cout << fixed << setprecision(2) << val << " ";
        }
        cout << endl;
    }
}

int main() {
    // Example matrices with real values
    vector<vector<float>> A = {
        {1.5, 2.2, 3.0},
        {4.1, 5.3, 6.7}
    };

    vector<vector<float>> B = {
        {7.0},
        {9.1},
        {11.4}
    };

    cout << "Matrix A:" << endl;
    printMatrix(A);

    cout << "Matrix B:" << endl;
    printMatrix(B);

    // Multiply A and B
    vector<vector<float>> C = multiplyMatrices(A, B);

    cout << "Result of A * B:" << endl;
    printMatrix(C);

    return 0;
}
from sympy import symbols, Matrix, simplify, expand, cos, sin, pi, latex,sqrt

#%% simple case
# Define symbolic variables for matrices A and B
a11, a12, a21, a22 = symbols('a11 a12 a21 a22')
b11, b12, b21, b22 = symbols('b11 b12 b21 b22')

# Define 2x2 symbolic matrices
A = Matrix([[a11, a12], [a21, a22]])
B = Matrix([[b11, b12], [b21, b22]])

# Compute the dot product A * B
result = A * B

# Display the resulting matrix
result

#%% creating matrices automatically
# # Define symbolic variables for a 6x6 matrix 
# C = Matrix(6, 6, lambda i, j: symbols(f'C{i+1}{j+1}'))

# Define symbolic variables for a symmetric 6x6 matrix  (Stiffness)
C = Matrix(6, 6, lambda i, j: symbols(f'C{i+1}{j+1}') if j>=i else symbols(f'C{j+1}{i+1}'))


# Define symbolic variables for a 6x3 matrix gradient operator
d1, d2, d3 = symbols('d1 d2 d3') # space operator
l1, l2, l3 = symbols('l1 l2 l3') # wavenumber operator


nabla_s = Matrix([[d1,0,0,0,d3,d2],[0,d2,0,d3,0,d1],[0,0,d3,d2,d1,0]])
Gamma_s = nabla_s * C * nabla_s.T

for i in range(Gamma_s.shape[0]):
    for j in range(Gamma_s.shape[1]):
        if j>=i:
            print(f'Gamma_s[{i+1},{j+1}] = {Gamma_s[i,j]}')


nabla_k = Matrix([[l1,0,0,0,l3,l2],[0,l2,0,l3,0,l1],[0,0,l3,l2,l1,0]])
Gamma_k = nabla_k * C * nabla_k.T
# for i in range(Gamma_k.shape[0]):
#     for j in range(Gamma_k.shape[1]):
#         Gamma_k[i,j] = expand(Gamma_k[i,j])
#         if j>=i:
#             print(f'Gamma_k[{i+1},{j+1}] = {Gamma_k[i,j]}')


#%% Rotation vector

# Rz11, Rz12,Rz13 = symbols('cos(omega)'), symbols('sen(omega)'), 0
# Rz21, Rz22,Rz23 = symbols('-sen(omega)'), symbols('cos(omega)'), 0
# Rz31, Rz32,Rz33 = 0, 0, 1
# Rz = Matrix([[Rz11, Rz12, Rz13], [Rz21, Rz22, Rz23], [Rz31, Rz32, Rz33]])

# Ry11, Ry12,Ry13 = symbols('cos(chi)'), 0, symbols('-sen(chi)')
# Ry21, Ry22,Ry23 = 0, 1, 0
# Ry31, Ry32,Ry33 = symbols('sen(chi)'), 0, symbols('cos(chi)')
# Ry = Matrix([[Ry11, Ry12, Ry13], [Ry21, Ry22, Ry23], [Ry31, Ry32, Ry33]])

# Rzz11, Rzz12,Rzz13 = symbols('cos(phi)'), symbols('sen(phi)'), 0
# Rzz21, Rzz22,Rzz23 = symbols('-sen(phi)'), symbols(' cos(phi)'), 0
# Rzz31, Rzz32,Rzz33 = 0, 0, 1
# Rzz = Matrix([[Rzz11, Rzz12, Rzz13], [Rzz21, Rzz22, Rzz23], [Rzz31, Rzz32, Rzz33]])

# alpha =   Rzz * (Ry * Rz)  
# alpha = simplify(alpha)


from sympy import symbols, Matrix, simplify, expand, cos, sin, pi, latex,sqrt

#%% Rotation operator v2

chi = symbols('chi')

# chi = 0 #y-axis rotation


# Rotation about y-axis
Ry11, Ry13 = cos(chi), -sin(chi)
Ry31, Ry33 = sin(chi), cos(chi)
Ry = Matrix([[Ry11, Ry13],  [Ry31, Ry33]])


# General rotation matrix
a =   Ry

# print(latex(a))

# Bound Transformation
M = Matrix([[a[0,0]**2    , a[0,1]**2    , 2*a[0,1]*a[0,0]              ],
            [a[1,0]**2    , a[1,1]**2    , 2*a[1,1]*a[1,0]              ],
            [a[1,0]*a[0,0], a[1,1]*a[0,1], a[0,1]*a[1,0] + a[0,0]*a[1,1]]])

M = simplify(M)

# print(latex(M))

# # print each compoment of M matrix
# for i in range(M.shape[0]):
#     for j in range(M.shape[1]):
#         print(f'M[{i+1},{j+1}] = {latex(M[i,j])}')
        
#%% Stiffness matrix

# VTI
C11 = symbols('C11')
C13 = symbols('C13')
C33 = symbols('C33')
C55 = symbols('C55')


# # print(latex(C_iso))

# Thomsen parameters
epsilon = symbols('epsilon')
delta = symbols('delta')

# Vti parameters
C11 = C33*(2*epsilon + 1) 
#C13 = sqrt(2*delta*C33*(C33 - C55)+(C33 - C55)**2) - C55
C13 = (1+delta)*C33 -2*C55# Behera approximation

C_vti = Matrix([[C11, C13, 0   ],
                [C13, C33, 0   ],
                [ 0 , 0  , C55 ]])


C_tti = M * (C_vti * M.T)
C_tti = simplify(C_tti)

# # print(latex(C_tti))

# print each compoment of C_tti matrix
for i in range(C_tti.shape[0]):
    for j in range(C_tti.shape[1]):
        print(f'C_tti[{i+1},{j+1}] = {latex(C_tti[i,j])}')




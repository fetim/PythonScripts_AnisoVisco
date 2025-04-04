from sympy import symbols, Matrix, simplify, expand, cos, sin, pi, latex,sqrt

#%% Rotation operator v2

omega = symbols('omega') 
chi = symbols('chi')
phi = symbols('phi')

omega = 0 #z-axis rotation
# chi = 0 #y-axis rotation
phi = 0 #z-axis rotation

# Rotation about z-axis
Rz11, Rz12,Rz13 = cos(omega) ,sin(omega) , 0
Rz21, Rz22,Rz23 = -sin(omega),cos(omega), 0
Rz31, Rz32,Rz33 = 0, 0, 1
Rz = Matrix([[Rz11, Rz12, Rz13], [Rz21, Rz22, Rz23], [Rz31, Rz32, Rz33]])

# print(latex(Rz))

# Rotation about y-axis
Ry11, Ry12,Ry13 = cos(chi), 0, -sin(chi)
Ry21, Ry22,Ry23 = 0, 1, 0
Ry31, Ry32,Ry33 = sin(chi), 0, cos(chi)
Ry = Matrix([[Ry11, Ry12, Ry13], [Ry21, Ry22, Ry23], [Ry31, Ry32, Ry33]])

# print(latex(Ry))

# Rotation about modified z-axis 
Rzz11, Rzz12,Rzz13 = cos(phi), sin(phi), 0
Rzz21, Rzz22,Rzz23 = -sin(phi), cos(phi), 0
Rzz31, Rzz32,Rzz33 = 0, 0, 1
Rzz = Matrix([[Rzz11, Rzz12, Rzz13], [Rzz21, Rzz22, Rzz23], [Rzz31, Rzz32, Rzz33]])

#print(latex(Rzz))

# General rotation matrix
a =   Rzz * (Ry * Rz)  

# print(latex(a))

# Bound Transformation
M = Matrix([[a[0,0]**2    , a[0,1]**2    , a[0,2]**2    , 2*a[0,1]*a[0,2]              , 2*a[0,2]*a[0,0]              , 2*a[0,0]*a[0,1]],
            [a[1,0]**2    , a[1,1]**2    , a[1,2]**2    , 2*a[1,1]*a[1,2]              , 2*a[1,2]*a[1,0]              , 2*a[1,0]*a[1,1]],
            [a[2,0]**2    , a[2,1]**2    , a[2,2]**2    , 2*a[2,1]*a[2,2]              , 2*a[2,2]*a[2,0]              , 2*a[2,0]*a[2,1]],
            [a[1,0]*a[2,0], a[1,1]*a[2,1], a[1,2]*a[2,2], a[1,1]*a[2,2] + a[1,2]*a[2,1], a[1,0]*a[2,2] + a[1,2]*a[2,0], a[1,1]*a[2,0] + a[1,1]*a[2,1]],
            [a[2,0]*a[0,0], a[2,1]*a[0,1], a[2,2]*a[0,2], a[0,1]*a[2,2] + a[0,2]*a[2,1], a[0,2]*a[2,0] + a[0,0]*a[2,2], a[0,0]*a[2,1] + a[0,1]*a[2,0]],
            [a[0,0]*a[1,0], a[0,1]*a[1,1], a[0,2]*a[1,2], a[0,1]*a[1,2] + a[0,2]*a[1,1], a[0,2]*a[1,0] + a[0,0]*a[1,2], a[0,0]*a[1,1] + a[0,1]*a[1,0]]])

M = simplify(M)

# print(latex(M))

# # print each compoment of M matrix
# for i in range(M.shape[0]):
#     for j in range(M.shape[1]):
#         print(f'M[{i+1},{j+1}] = {latex(M[i,j])}')
        
#%% Stiffness matrix

# Orthorrombic components
C11 = symbols('C11')
C12 = symbols('C12')
C13 = symbols('C13')
C22 = symbols('C22')
C23 = symbols('C23')
C33 = symbols('C33')
C44 = symbols('C44')
C55 = symbols('C55')
C66 = symbols('C66')

C_iso = Matrix([[C33, C12, C12, 0  , 0  , 0  ],
                [C12, C33, C12, 0  , 0  , 0  ],
                [C12, C12, C33, 0  , 0  , 0  ],
                [ 0 ,  0 ,  0 , C55, 0  , 0  ],
                [ 0 ,  0 ,  0 , 0  , C55, 0  ],
                [ 0 ,  0 ,  0 , 0  , 0  , C55]])


# print(latex(C_iso))

# Thomsen parameters
epsilon = symbols('epsilon')
delta = symbols('delta')
gamma = symbols('gamma')

# Vti parameters
C11 = C33*(2*epsilon + 1)
C22 = C33*(2*epsilon + 1)
#C13 = sqrt(2*delta*C33*(C33 - C55)+(C33 - C55)**2) - C55
C13 = (1+delta)*C33 -2*C55
C66 = C55*(2*gamma + 1)

C_vti = Matrix([[C11, C12, C13, 0  , 0  , 0  ],
                [C12, C22, C13, 0  , 0  , 0  ],
                [C13, C13, C33, 0  , 0  , 0  ],
                [ 0 , 0  , 0  , C55 , 0  , 0 ],
                [ 0 , 0  , 0  , 0  , C55, 0  ],
                [ 0 , 0  , 0  , 0  , 0  , C66]])


C_tti = M * (C_vti * M.T)
C_tti = simplify(C_tti)

# print(latex(C_tti))

# print each compoment of C_tti matrix
for i in range(C_tti.shape[0]):
    for j in range(C_tti.shape[1]):
        print(f'C_tti[{i+1},{j+1}] = {latex(C_tti[i,j])}')




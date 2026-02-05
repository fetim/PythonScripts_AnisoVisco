from sympy import symbols, Matrix, simplify, expand, cos, sin, pi, latex,sqrt

        
#%% Stiffness matrix

# Orthorrombic components
C11 = symbols('C11')
C12 = symbols('C12')
C13 = symbols('C13')
C14 = symbols('C14')
C15 = symbols('C15')
C16 = symbols('C16')
C22 = symbols('C22')
C23 = symbols('C23')
C24 = symbols('C24')
C25 = symbols('C25')
C26 = symbols('C26')
C33 = symbols('C33')
C34 = symbols('C34')
C35 = symbols('C35')
C36 = symbols('C36')
C44 = symbols('C44')
C45 = symbols('C45')
C46 = symbols('C46')
C55 = symbols('C55')
C56 = symbols('C56')
C66 = symbols('C66')

C_iso = Matrix([[C33, C12, C12, 0  , 0  , 0  ],
                [C12, C33, C12, 0  , 0  , 0  ],
                [C12, C12, C33, 0  , 0  , 0  ],
                [ 0 ,  0 ,  0 , C55, 0  , 0  ],
                [ 0 ,  0 ,  0 , 0  , C55, 0  ],
                [ 0 ,  0 ,  0 , 0  , 0  , C55]])


C_vti = Matrix([[C11, C12, C13, 0  , 0  , 0  ],
                [C12, C22, C13, 0  , 0  , 0  ],
                [C13, C13, C33, 0  , 0  , 0  ],
                [ 0 , 0  , 0  , C55 , 0  , 0 ],
                [ 0 , 0  , 0  , 0  , C55, 0  ],
                [ 0 , 0  , 0  , 0  , 0  , C66]])

C_orth = Matrix(([C11, C12, C13, 0  , 0  , 0 ],
                 [C12, C22, C23, 0  , 0  , 0 ],
                 [C13, C23, C33, 0  , 0  , 0 ],
                 [0  , 0  , 0  , C44, 0  , 0 ],
                 [0  , 0  , 0  , 0  , C55, 0 ],
                 [0  , 0  , 0  , 0  , 0  , C66]))

C_Tilt = Matrix(([C11, C12, C13, C14, C15, C16 ],
                 [C12, C22, C23, C24, C25, C26 ],
                 [C13, C23, C33, C34, C35, C36 ],
                 [C14, C24, C34, C44, C45, C46 ],
                 [C15, C25, C35, C45, C55, C56 ],
                 [C16, C26, C36, C46, C56, C66 ]))


# define spatial derivative
dx, dy, dz = symbols('Dx Dy Dz')

nabla = Matrix(([dx, 0 , 0, 0, dz, dy],
                [0 , dy, 0, dz, 0, dx],
                [0 , 0 , dz, dy, dx, 0]))

vx, vy, vz = symbols('vx vy vz')

v = Matrix(([vx, vy, vz]))

Txx , Tyy, Tzz = symbols('Txx Tyy Tzz')

Txy, Txz, Tyz = symbols('Txy Txz Tyz')

dTdt =  C_Tilt * (nabla.T * v)



# print each compoment of C_tti matrix
for i in range(C_Tilt.shape[0]):
    for j in range(C_Tilt.shape[1]):
        print(f'C_Tilt[{i+1},{j+1}] = {latex(C_Tilt[i,j])}')


for i in range(dTdt.shape[0]):
    print(f'dTdt[{i+1}] = {latex(dTdt[i])}')


import numpy as np
import matplotlib.pyplot as plt


omega = 30 *np.pi/180  # rotation angle in radians
chi   = 30 *np.pi/180  # rotation angle in radians
phi   = 30 *np.pi/180  # rotation angle in radians

# Rotation about z-axis
Rz11, Rz12,Rz13 = np.cos(omega) ,-np.sin(omega) , 0
Rz21, Rz22,Rz23 = np.sin(omega),np.cos(omega), 0
Rz31, Rz32,Rz33 = 0, 0, 1
Rz = np.array([[Rz11, Rz12, Rz13], [Rz21, Rz22, Rz23], [Rz31, Rz32, Rz33]])

# print(Rz)

# Rotation about y-axis
Ry11, Ry12,Ry13 = np.cos(chi), 0, -np.sin(chi)
Ry21, Ry22,Ry23 = 0, 1, 0
Ry31, Ry32,Ry33 = np.sin(chi), 0, np.cos(chi)
Ry = np.array([[Ry11, Ry12, Ry13], [Ry21, Ry22, Ry23], [Ry31, Ry32, Ry33]])

# print(Ry)

# Rotation about modified z-axis
Rzz11, Rzz12,Rzz13 = np.cos(phi), -np.sin(phi), 0
Rzz21, Rzz22,Rzz23 = np.sin(phi), np.cos(phi), 0
Rzz31, Rzz32,Rzz33 = 0, 0, 1
Rzz = np.array([[Rzz11, Rzz12, Rzz13], [Rzz21, Rzz22, Rzz23], [Rzz31, Rzz32, Rzz33]])

# print(Rzz)

# General rotation matrix
a =   np.dot(Rzz, (np.dot(Ry, Rz)))

# print(a)

# Bound Transformation
M = np.array([[a[0,0]**2    , a[0,1]**2    , a[0,2]**2    , 2*a[0,1]*a[0,2]              , 2*a[0,2]*a[0,0]              , 2*a[0,0]*a[0,1]],
            [a[1,0]**2    , a[1,1]**2    , a[1,2]**2    , 2*a[1,1]*a[1,2]              , 2*a[1,2]*a[1,0]              , 2*a[1,0]*a[1,1]],
            [a[2,0]**2    , a[2,1]**2    , a[2,2]**2    , 2*a[2,1]*a[2,2]              , 2*a[2,2]*a[2,0]              , 2*a[2,0]*a[2,1]],
            [a[1,0]*a[2,0], a[1,1]*a[2,1], a[1,2]*a[2,2], a[1,1]*a[2,2] + a[1,2]*a[2,1], a[1,0]*a[2,2] + a[1,2]*a[2,0], a[1,1]*a[2,0] + a[1,1]*a[2,1]],
            [a[2,0]*a[0,0], a[2,1]*a[0,1], a[2,2]*a[0,2], a[0,1]*a[2,2] + a[0,2]*a[2,1], a[0,2]*a[2,0] + a[0,0]*a[2,2], a[0,0]*a[2,1] + a[0,1]*a[2,0]],
            [a[0,0]*a[1,0], a[0,1]*a[1,1], a[0,2]*a[1,2], a[0,1]*a[1,2] + a[0,2]*a[1,1], a[0,2]*a[1,0] + a[0,0]*a[1,2], a[0,0]*a[1,1] + a[0,1]*a[1,0]]])


rho = 1000  # density in kg/m^3
vp = 2000  # P-wave velocity in m/s
vs = 1000  # S-wave velocity in m/s

# 2-direction (about y-axis) 
epsilon2 = 0.1  # Thompsen parameter 
delta2 = 0.1  # Thompsen parameter
gamma2 = 0.1  # Thompsen parameter

# 1-direction (about x-axis)
epsilon1 = 0.1  # Thompsen parameter
delta1 = 0.1  # Thompsen parameter
gamma1 = 0.1  # Thompsen parameter

# 3-direction (about z-axis)
epsilon3 = 0.1  # Thompsen parameter
delta3 = 0.1  # Thompsen parameter
gamma3 = 0.1  # Thompsen parameter #?????

# Orthorrombic Stiffness matrix in Voigt notation
C33 = rho * vp**2 
C11 = C33 * (2*epsilon2 + 1)
C22 = C33 * (2*epsilon1 + 1)

C44 = rho * vs**2
C66 = C44 * (2*gamma2 + 1)
C55 = C66 / (2*gamma1 + 1)

C13 = np.sqrt(2*delta2*C33*(C33-C55)+(C33-C55)**2) - C55
C23 = np.sqrt(2*delta1*C33*(C33-C44)+(C33-C44)**2) - C44
C12 = np.sqrt(2*delta3*C11*(C11-C66)+(C11-C66)**2) - C66

C_ort = np.array([[C11, C12, C13, 0  , 0  , 0  ],
                  [C12, C22, C23, 0  , 0  , 0  ],
                  [C13, C23, C33, 0  , 0  , 0  ],
                  [0  , 0  , 0  , C44, 0  , 0  ],
                  [0  , 0  , 0  , 0  , C55, 0  ],
                  [0  , 0  , 0  , 0  , 0  , C66]])

C_tilt = np.dot(np.dot(C_ort,M.T),M)

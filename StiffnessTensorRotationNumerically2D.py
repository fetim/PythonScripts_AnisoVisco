import numpy as np
import matplotlib.pyplot as plt


chi   = 30 *np.pi/180  # rotation angle in radians


# Rotation about y-axis
Ry11, Ry13 = np.cos(chi), -np.sin(chi)
Ry31, Ry33 = np.sin(chi), np.cos(chi)
Ry = np.array([[Ry11, Ry13], [Ry31, Ry33]])

# print(Ry)


# General rotation matrix
a =  Ry

# print(a)

# Bound Transformation
M = np.array([[a[0,0]**2    , a[0,1]**2    , 2*a[0,1]*a[0,0]              ],
            [a[1,0]**2    , a[1,1]**2    , 2*a[1,1]*a[1,0]              ],
            [a[1,0]*a[0,0], a[1,1]*a[0,1], a[0,1]*a[1,0] + a[0,0]*a[1,1]]])


rho = 1000  # density in kg/m^3
vp = 2000  # P-wave velocity in m/s
vs = 1000  # S-wave velocity in m/s

# 2-direction (about y-axis) 
epsilon = 0.1  # Thompsen parameter 
delta = 0.1  # Thompsen parameter

# Orthorrombic Stiffness matrix in Voigt notation
C33 = rho * vp**2 
C11 = C33 * (2*epsilon + 1)

C55 = rho * vs**2

C13 = np.sqrt(2*delta*C33*(C33-C55)+(C33-C55)**2) - C55

C_vti = np.array([[C11, C13, 0   ],
                  [C13, C33, 0   ],
                  [0  , 0  , C55 ]])

C_tti = np.dot(np.dot(C_vti,M.T),M)

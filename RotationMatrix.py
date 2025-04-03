import numpy as np
import matplotlib.pyplot as plt

def RotationMatrix(th):
    r11 = np.cos(th)
    r12 = -np.sin(th)
    r22 = np.cos(th)
    r21 = np.sin(th)

    return np.array([[r11, r12], [r21, r22]])

def StiffnessMatrixVTI2D(vp, vs, rho, epsilon, delta):
    """
    Calculate the stiffness matrix for a VTI medium.
    """
    c11 = rho * vp**2 * (1 + 2 * epsilon)
    c33 = rho * vp**2
    c44 = rho * vs**2
    c13 = np.sqrt(2*delta*c33*(c33-c44) + (c33-c44)**2) - c44

    C = np.array([[c11, c13, 0], [c13, c33, 0], [0, 0, c44]])
    return C

def RotationMatrix_VoigtNotation(R):
    R_voigt = np.zeros((3, 3))
    R_voigt[0, 0] = R[0, 0]**2 #11
    R_voigt[0, 1] = R[0, 1]**2 #12
    R_voigt[0, 2] = 2*R[0, 0] * R[0, 1] #13
    R_voigt[1, 0] = R[1, 0]**2 #21
    R_voigt[1, 1] = R[1, 1]**2 #22
    R_voigt[1, 2] = 2*R[1, 0] * R[1, 1] #23
    R_voigt[2, 0] = R[0, 0] * R[1, 0] #31
    R_voigt[2, 1] = R[0, 1] * R[1, 1] #32
    R_voigt[2, 2] = R[0, 1] * R[1, 0] + R[0, 0] * R[1, 1] #33
    return R_voigt



# test rotation matrix
x = np.linspace(0, 1, 100)
y = x

th = 30 * np.pi / 180
R = RotationMatrix(th)

rot = np.dot(R, np.array([x, y]))
x_rot = rot[0]
y_rot = rot[1]

plt.figure()
plt.plot(x, y, label='Original')
plt.plot(x_rot, y_rot, label='Rotated')
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.legend()
plt.grid()
plt.savefig('rotation_matrix.png')

# test stiffness matrix
vp = 3000
vs = 2000
rho = 1000
epsilon = 0.2
delta = -0.2

C = StiffnessMatrixVTI2D(vp, vs, rho, epsilon, delta)

R_voigt = RotationMatrix_VoigtNotation(R)
C_rot = np.dot(np.dot(R_voigt, C), R_voigt.T)

# rotate the stiffness matrix

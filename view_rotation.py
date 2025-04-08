import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x_axis = np.linspace(-2, 2, 100)
y_axis = np.linspace(-2, 2, 100)
z_axis = np.linspace(-2, 2, 100)

X_axis = np.zeros([100,3])
X_axis[:,0] = x_axis
Y_axis = np.zeros([100,3])
Y_axis[:,1] = y_axis
Z_axis = np.zeros([100,3])
Z_axis[:,2] = z_axis

x = np.linspace(0, 1, 100)
y = np.linspace(0, 1, 100)
z = np.linspace(0, 1, 100)

X  = np.zeros([100,3])
X[:,0] = x 
Y = np.zeros([100,3])
Y[:,1] = y
Z = np.zeros([100,3])
Z[:,2] = z

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X_axis[:,0], X_axis[:,1], X_axis[:,2], c='r', marker='.', s=0.7)
ax.scatter(Y_axis[:,0], Y_axis[:,1], Y_axis[:,2], c='g', marker='.', s=0.7)
ax.scatter(Z_axis[:,0], Z_axis[:,1], Z_axis[:,2], c='b', marker='.', s=0.7)

# ax.scatter(X[:,0], X[:,1], X[:,2], c='r', marker='.', label='X-axis', s=0.7)
# ax.scatter(Y[:,0], Y[:,1], Y[:,2], c='g', marker='.', label='Y-axis', s=0.7)
# ax.scatter(Z[:,0], Z[:,1], Z[:,2], c='b', marker='.', label='Z-axis', s=0.7)
ax.legend()
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_title('3D Scatter Plot')
ax.set_xlim(xmin=-1.0, xmax=1.0)
ax.set_ylim(ymin=-1.0, ymax=1.0)
ax.set_zlim(zmin=-1.0, zmax=1.0)
ax.view_init(elev=30, azim=-75  )  # adjust these values as you like


omega = 45 *np.pi/180  # rotation angle in radians
chi = 45*np.pi/180  # rotation angle in radians
phi = 45*np.pi/180  # rotation angle in radians

# Create rotation matrices for each axis
rotation_z = np.array([[np.cos(omega), -np.sin(omega), 0],
                       [np.sin(omega), np.cos(omega), 0],
                       [0, 0, 1]])

rotation_y = np.array([[np.cos(chi), 0, -np.sin(chi)],
                       [0, 1, 0],
                       [np.sin(chi), 0, np.cos(chi)]])

rotation_z2 = np.array([[np.cos(phi), -np.sin(phi), 0],
                        [np.sin(phi), np.cos(phi), 0],
                        [0, 0, 1]])

Rotation  = np.dot(rotation_y, rotation_z)
Rotation = np.dot(rotation_z2, Rotation)

# Apply rotation matrices to the points
X_rotated = np.dot(X, Rotation)
Y_rotated = np.dot(Y, Rotation)
Z_rotated = np.dot(Z, Rotation)

ax.scatter(X_rotated[:,0], X_rotated[:,1], X_rotated[:,2], c='r', marker='*', s=5, label='X-axis rotated')
ax.scatter(Y_rotated[:,0], Y_rotated[:,1], Y_rotated[:,2], c='g', marker='*', s=5, label='Y-axis rotated')
ax.scatter(Z_rotated[:,0], Z_rotated[:,1], Z_rotated[:,2], c='b', marker='*', s=5, label='Z-axis rotated')


plt.savefig('X-axis.png', dpi=300, bbox_inches='tight')

# plt.show()
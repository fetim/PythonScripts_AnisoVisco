import numpy as np
import matplotlib.pyplot as plt

def velocity_vti(vp0, vs0, dl, ep, gm, th):
    """
    Calculate the P-wave, S-wave and SH-wave velocities for a VTI medium.
    """	

    vp = vp0 * (1 + dl * np.sin(th)**2 * np.cos(th)**2 + ep * np.sin(th)**4)
    vsv = vs0 * (1 + (vp0/vs0)**2 * (ep - dl) * np.sin(th)**2 * np.cos(th)**2)
    vsh = vs0 * (1 + gm * np.sin(th)**2)

    return vp, vsv, vsh


def plot_phase_velocity(theta, vp, vsv, vsh, tt=1.0):
    
    # distance 
    Rp_x = tt * vp * np.sin(theta)
    Rp_y = tt * vp * np.cos(theta)

    Rsv_x = tt * vsv * np.sin(theta)
    Rsv_y = tt * vsv * np.cos(theta)

    Rsh_x = tt * vsh * np.sin(theta)
    Rsh_y = tt * vsh * np.cos(theta)

    plt.figure()
    plt.plot(Rp_x, Rp_y, label='Vp')
    plt.plot(Rsv_x, Rsv_y, label='Vsv')
    plt.plot(Rsh_x, Rsh_y, label='Vsh')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(f'Travel time = {tt} s')
    plt.legend()
    plt.grid()
    plt.savefig('vti_velocity_cartesian.png')
    
if __name__ == '__main__':
    vp0 = 3000
    vs0 = 2000
    dl = -0.2
    ep = 0.2
    gm = 0.0

    theta = np.linspace(0,2 * np.pi, 100, endpoint=True)
    vp, vsv, vsh = velocity_vti(vp0, vs0, dl, ep, gm, theta) # polar coordinates

    # distance in polar coordinates
    tt = 2.0 # travel time
    Rp = tt * vp
    Rsv = tt * vsv
    Rsh = tt * vsh

    plot_phase_velocity(theta, vp, vsv, vsh, tt) # In cartesian coordinates



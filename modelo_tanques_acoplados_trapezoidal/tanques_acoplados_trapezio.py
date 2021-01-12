import math
from math import pi
# import random

# import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal

# def dvCord(x, ux, uy, t):

#     a0 = 16.6 # mm2
#     a1 = 37.4 # mm2
#     b = 78 # mm
#     c = 76 # mm
#     theta = pi * 23.5/180 # rad
#     Uin = (5 * ux + 200) if (5 * ux + 200) < 500 else 500
#     g = 9787.9 # mm/s2
#     A0= 11664 # mm2
#     A1 = b*(c+x[1]*math.tan(theta))

#     xd = np.array(np.zeros((2, 1)))


#     xd[0] = Uin - (a0/A0) * math.sqrt(2 * g * x[0])
#     xd[1] = (a0/A1) * math.sqrt(2 * g * x[0]) - (a1/A1) * math.sqrt(2 * g * x[1])
    
#     return xd.copy()

def dvCord(x, ux, uy, t):

    gamma1 = 0.75
    gamma2 = 0.75
    theta = 23.5
    k1 = 4470 * 10**(-9)
    k2 = 4190 * 10**(-9)
    b = 78 * 10**(-3)
    c = 76 * 10**(-3)
    a1 = 37.4 * 10**(-6)
    a2 = 37.4 * 10**(-6)
    a3 = 16.6 * 10**(-6)
    a4 = 16.6 * 10**(-6)
    g = 9787.9 * 10**(-3)
    A1 = 11664 * 10**(-6)
    A2 = b * (c + x[1] * np.tan(pi * theta/180))
    A3 = 11664 * 10**(-6)
    A4 = 11664 * 10**(-6)

    xd = np.array(np.zeros((4, 1)))
    
    z0 = 2*g*x[0] if 2*g*x[0] > 0 else 0
    z1 = 2*g*x[1] if 2*g*x[1] > 0 else 0
    z2 = 2*g*x[2] if 2*g*x[2] > 0 else 0
    z3 = 2*g*x[3] if 2*g*x[3] > 0 else 0

    xd[0] = -(a1/A1) * np.sqrt(z0) + (a3/A1) * np.sqrt(z2) + (gamma1*k1/A1) * ux
    xd[1] = -(a2/A2) * np.sqrt(z1) + (a4/A2) * np.sqrt(z3) + (gamma2*k2/A2) * uy
    xd[2] = -(a3/A3) * np.sqrt(z2) + ((1 - gamma2) * k2/A3) * uy
    xd[3] = -(a4/A4) * np.sqrt(z3) + ((1 - gamma1) * k1/A4) * ux

    return xd.copy()


def rk_cord(x0, ux, uy, h, t):
    # 1st evaluation
    xd = dvCord(x0, ux, uy, t)
    savex0 = x0.copy()
    phi = xd.copy()
    for i in range(len(x0)):
        x0[i] = savex0[i] + 0.5 * h * xd[i]

    # 2nd evaluation
    xd = dvCord(x0.T, ux, uy, t + 0.5 * h)
    phi = (phi + 2 * xd)
    for i in range(len(x0)):
        x0[i] = savex0[i] + 0.5 * h * xd[i]

    # 3rd evaluation
    xd = dvCord(x0, ux, uy, t + 0.5 * h)
    phi = phi + 2 * xd
    for i in range(len(x0)):
        x0[i] = savex0[i] + h * xd[i]

    # 4th evaluation
    xd = dvCord(x0, ux, uy, t + h)

    result_x = x0.copy()
    for i in range(len(x0)):
        result_x[i] = savex0[i] + (phi[i] + xd[i]) * h / 6

    return result_x


def run_rk(t:np.ndarray, x:np.ndarray, ux, uy, h):
    result = None
    
    for k in range(1, len(t)):
        result = rk_cord(x[:, k - 1].copy(), ux[k], uy[k], h, t[k])
        x[:, k] = result
    
    plt.subplot(411)
    plt.plot(x[0])
    plt.plot(ux)
    plt.subplot(412)
    plt.plot(x[1])
    plt.plot(uy)
    plt.subplot(413)
    plt.plot(x[2])
    plt.plot(uy)
    plt.subplot(414)
    plt.plot(x[3])
    plt.plot(ux)
        
    # print(x)
    
t0 = 0
tf = 400
h = 1
t = np.arange(t0, tf, h)

# [print(i) for i in t if i < 0.1]

x0 = np.array([[.8], [.8], [.9], [.9]])

z_x = np.zeros((len(x0), len(t) - 1))
x = x0.copy()
x = np.append(x, z_x, axis=1)

# print(x)    

# Degrau
# left_size = math.floor(len(t)/10)
# right_size = math.floor(len(t) - len(t)/10)
# print(f'L: {left_size}; R: {right_size}')
# left = np.zeros((left_size, 1))
# right = np.ones(right_size)
# # print(f'L: {left}; R: {right}')
# ux = 1 * np.append(left,right)
# uy = ux
# run_rk(t.copy() ,x.copy(), ux, uy, h)

#impulso
# u = signal.unit_impulse(len(t),'mid')
# run_rk(t.copy() ,x.copy(), u.copy(), u.copy() , h)

# Pulso
# u = 1 * np.append(np.append(np.zeros((math.floor(len(t)/3+1), 1)), 
#                              np.full((math.floor(len(t)/3), 1), 1)), 
#                    np.zeros((math.floor(len(t)/3), 1)))

# run_rk(t.copy() ,x.copy(), u.copy(), u.copy(), h)

# Pulso
# u = 1 * (signal.square(2 * np.pi * .002 * t)+1)
# run_rk(t.copy() ,x.copy(), u.copy() ,  u.copy(), h)

# Senoidal
u = 1 * abs(np.sin(np.array( t * 0.05)))  # np.zeros((len(t), 1))
run_rk(t.copy() ,x.copy(), u.copy() , u.copy(), h)
import math
import random

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

mpl.rcParams['legend.fontsize'] = 10


# import simpy as sp


def dvCord(x, ux, uy, t):
    # a = 0.258
    # b = 4.033
    # F = 8
    # G = 1
    epsilon = 8.53

    xd = np.array(np.zeros((3, 1)))

    xd[0] = x[1]
    xd[1] = -x[0] + epsilon * x[1] + ux - epsilon * x[0] ** 2 * x[1]
    # xd[2] = x[0]

    return (xd.copy())


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


if __name__ == "__main__":
    t0 = 900
    tf = 1000
    h = 0.01
    t = np.arange(t0, tf, h)
    [print(i) for i in t if i < 0.1]

    x0 = np.array([[0.1], [0.1]])

    z_x = np.zeros((len(x0), len(t) - 1))
    x = x0.copy()
    x = np.append(x, z_x, axis=1)
    print(x)
    Ts = 1 / 100
    omega = (2 * math.pi) / 10
    U = 1.2
    # Degrau
    u = np.append(np.zeros((math.floor(len(t)/2), 1)), np.full((math.floor(len(t)/2)+1, 1), 1))

    # Pulso
    # u = np.array([U * math.sin(omega * i * Ts) for i in t])  # np.zeros((len(t), 1))
    # Senoidal
    # u = np.array([U * math.sin(omega * i * Ts) for i in t])  # np.zeros((len(t), 1))

    for k in range(1, len(t)):
        result = rk_cord(x[:, k - 1].copy(), u[k], u[k], h, t[k])
        x[:, k] = result

    fig, ax = plt.subplots(constrained_layout=True, figsize=(8, 4))
    ax.set(xlabel='time')
    ax.set(ylabel='x_1')
    color = ['red', 'green', 'blue', 'yellow', 'orange']
    ax.plot(t, x[0, :], color=color[random.randint(0, len(color) - 1)])
    ax.grid()
    fig.savefig(f'x_1.png')
    fig1, ax1 = plt.subplots(constrained_layout=True, figsize=(4, 8))
    ax1.set(xlabel='time')
    ax1.set(ylabel='x_2')
    ax1.plot(t, x[1, :], color=color[random.randint(0, len(color) - 1)])
    ax1.grid()
    fig1.savefig(f'x_2.png')
    plt.show()
    # fig2 = plt.figure(constrained_layout=True, figsize=(8, 8))
    # ax2 = fig2.gca(projection='3d')
    # ax2.plot(x[0, 1000:], x[1, 1000:], x[2, 1000:], color=color[random.randint(0, len(color) - 1)])
    # ax2.grid()
    # fig2.savefig(f'x_3.png')

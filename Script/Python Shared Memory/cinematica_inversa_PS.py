import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def inverse_kin(g, h, p, psi, theta, phi):
    a1 = [g,0,0]
    a2 = [-1/2*g, np.sqrt(3)/2 * g, 0]
    a3 = [-1/2*g, -np.sqrt(3)/2 * g, 0]
    origem_fixa = [0,0,0]

    psi = psi*np.pi/180
    theta = theta*np.pi/180
    phi = phi*np.pi/180

    rot_matrix = [
    [np.cos(phi)*np.cos(theta), np.cos(phi)*np.sin(theta)*np.sin(psi) - np.sin(phi)*np.cos(psi), np.cos(phi)*np.sin(theta)*np.sin(psi) + np.sin(phi)*np.cos(psi)],
    [np.sin(phi)*np.cos(theta), np.sin(phi)*np.sin(theta)*np.sin(psi) + np.cos(phi)*np.cos(psi), np.sin(phi)*np.sin(theta)*np.cos(psi) - np.cos(phi)*np.sin(psi)],
    [-np.sin(theta), np.cos(theta)*np.sin(psi), np.cos(theta)*np.cos(psi)]
    ]

    ux = rot_matrix[0][0]
    uy = rot_matrix[1][0]
    uz = rot_matrix[2][0]

    vx = rot_matrix[0][1]
    vy = rot_matrix[1][1]
    vz = rot_matrix[2][1]

    wx = rot_matrix[0][2]
    wy = rot_matrix[1][2]
    wz = rot_matrix[2][2]


    q1 = [
        p[0] + h*ux,
        p[1] + h*uy,
        p[2] + h*uz
    ]

    q2 = [
        p[0] -1/2*h*ux + np.sqrt(3)/2*h*vx,
        p[1] -1/2*h*uy + np.sqrt(3)/2*h*vy,
        p[2] -1/2*h*uz + np.sqrt(3)/2*h*vz,
    ]

    q3 = [
        p[0] -1/2*h*ux - np.sqrt(3)/2*h*vx,
        p[1] -1/2*h*uy - np.sqrt(3)/2*h*vy,
        p[2] -1/2*h*uz - np.sqrt(3)/2*h*vz,
    ]

    # Definir as coordenadas da plataforma fixa e móvel
    # Suponha que os pontos da base da plataforma (fixos) sejam conhecidos:
    base_points = np.array([
        a1,   # Ponto 1
        a2,  # Ponto 2
        a3, # Ponto 3
        origem_fixa,   # Ponto 5 (centro da plataforma)
    ])

    # Definir as coordenadas da plataforma móvel (nós)
    # Posição fictícia para a plataforma móvel
    mobile_points = np.array([
        q1,  # Ponto 1
        q2, # Ponto 2
        q3,# Ponto 3
        p,    # Ponto 4 (centro)
    ])


    return [base_points, mobile_points]

# Calcular a distância entre os pontos da base e a plataforma móvel (simulação de pistões)
def calculate_distances(base_points, mobile_points):
    distances = []
    for i in range(3):
        distance = np.linalg.norm(base_points[i] - mobile_points[i])
        distances.append(distance)
    return distances


base, mob = inverse_kin(120,115,[0,0,118], 0,0,0)

#print(base)
#print(mob)

print(calculate_distances(base,mob))


print(mob)


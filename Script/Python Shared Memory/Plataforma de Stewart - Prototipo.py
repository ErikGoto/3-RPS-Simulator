import time
from pyaccsharedmemory import accSharedMemory
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import serial as se

from cinematica_inversa_PS import inverse_kin, calculate_distances

#Variáveis importantes
#Propriedades físicas
g, h, p = 120,115, [0,0,125]
raio_braco = 70

arduino = se.Serial(port='COM7', baudrate=115200, timeout=.1)

def conversao_arduino(theta_0, h_0, h_f, r):
    theta_f = 180- (theta_0 + (h_f - h_0)*r*np.pi/180)
    return theta_f

def conversao_arduino_tratado(angulo):
    limite_max = 130
    limite_min = 180

    if angulo < limite_max:
        angulo = limite_max
    if angulo >= limite_min:
        angulo = limite_min

    return np.round(angulo,0)



print('Inicializando script...')

while(True):
    sm = accSharedMemory().read_shared_memory()
    if (sm is not None):
        # Memoria compartilhada
        forca_g = str(sm.Physics.g_force).split()
        lateral_g = float(forca_g[1][:-1])
        acel_g = float(forca_g[5])
        

        # Input para o modelo
        #Converte de força G para angulo
        angulo_lim_max = 25
        angulo_lim_min = -25
        acel_grau = np.interp(acel_g, [-2, 2], [angulo_lim_max, angulo_lim_min])
        lateral_grau = np.interp(lateral_g, [-2, 2], [angulo_lim_max, angulo_lim_min])

        print(f"Lateral:{acel_grau} \nAcel:{lateral_grau}")


        #Guarda o valor da posição dos pontos da base móvel
        cinematica_ivnersa = inverse_kin(g,h,p,acel_grau,lateral_grau,0)
        base_movel = cinematica_ivnersa[1]
        base_fixa = cinematica_ivnersa[0]
        comprimento_atuadores = calculate_distances(base_fixa, base_movel)

        braco_1 = conversao_arduino(30, p[2], calculate_distances(base_fixa, base_movel)[0], raio_braco)
        braco_2 = conversao_arduino(30, p[2], calculate_distances(base_fixa, base_movel)[1], raio_braco)
        braco_3 = conversao_arduino(30, p[2], calculate_distances(base_fixa, base_movel)[2], raio_braco)

        
 

        braco_1_angulo = np.round(conversao_arduino_tratado(braco_1),1)
        braco_2_angulo = np.round(conversao_arduino_tratado(braco_2),1)
        braco_3_angulo = np.round(conversao_arduino_tratado(braco_3),1)

        mensagem = f'{braco_2_angulo};{braco_1_angulo};{braco_3_angulo};111\n'
        #Envia infos para o Arduino
        arduino.write(mensagem.encode())

        print(f"Comprimento|Angulo: {np.round(comprimento_atuadores[0],1)}|{np.round(braco_1,1)}|{braco_1_angulo}")
        print(f"Comprimento|Angulo: {np.round(comprimento_atuadores[1],1)}|{np.round(braco_2,1)}|{braco_2_angulo}")
        print(f"Comprimento|Angulo: {np.round(comprimento_atuadores[2],1)}|{np.round(braco_3,1)}|{braco_3_angulo}")
        print('')
        print(mensagem)

    #Precisa fechar a Memória Compartilhada?
    accSharedMemory().close()
    time.sleep(0.2)


  
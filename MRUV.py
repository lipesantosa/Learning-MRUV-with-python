#Este programa irá gerar dados de Posição x Tempo no MRUV 
#Aceleração Constante
#Por Felipe Santos Araujo

#Bibliotecas
import numpy as np
import matplotlib.pyplot as plt
import os 

#Entrada de dados
x0 = float(input('Posição de repouso: '))   #Em m
v0 = float(input('Velocidade: '))           #Em m/s
a = float(input('Aceleração: '))            #Em m/s²
t0 = float(input('Tempo inicial: '))        #Em s
t1 = float(input('Tempo final: '))          #Em s

#Equações
t = np.linspace(t0, t1)                                    
x = x0 + v0*t + (a * t**2)/2                #Função horária da posição

print(x, "metros")

#Salvar os dados em um arquivo CSV
data = np.vstack((t, x)).T  # Empilhar tempo e posição e transpor para formato (n, 2)
np.savetxt("dados_mruv.csv", data, delimiter=",", header="Tempo (s), Posição (m)", comments="")

#Gerar gráfico
plt.figure(figsize=(8, 6))

t = data[:, 0]  # Coluna de tempo
x = data[:, 1]  # Coluna de posição
plt.plot(t, x, label=f"Arquivo {len('dados_mruv.csv')}")

plt.xlabel("Tempo (s)")
plt.ylabel("Posição (m)")
plt.title("Gráfico MRUV S x T")
plt.legend()
plt.grid(True)
plt.show()

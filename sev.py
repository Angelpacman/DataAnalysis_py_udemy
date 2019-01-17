import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

datos_input = pd.read_csv('sev_examen.csv')
#print(datos_input)

#AB/2 estara representada en el programa por AB
AB = datos_input.iloc[:,0]

#MN/2 estara representada en el programa por MN
MN = datos_input.iloc[:,1]

I = datos_input.iloc[:,2]

V = datos_input.iloc[:,3]

KG=np.pi*((AB-MN)*(AB+MN)/(2*MN))

Rhoa = V*KG/I
#print("\n", datos_input)
#print(KG)
print(Rhoa)

plt.plot(AB,Rhoa)
plt.semilogy(AB,Rhoa)
plt.grid(True, which = 'both')
plt.scatter(AB,Rhoa)
#
plt.yscale("log")
plt.xscale('log')

plt.ylim([1,1000])
plt.xlim([1,1000])

plt.xlabel('AB/2')
plt.ylabel('Resistividad aparente')
plt.title('Sondeo Electrico Vertical EXAMEN')
plt.show()

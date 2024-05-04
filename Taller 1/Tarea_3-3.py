<<<<<<< HEAD
import numpy as np
import matplotlib.pyplot as plt

V_max = float(input("Ingrese el voltaje inicial (V): "))
R = float(input("Ingrese la resistencia (Ω): "))
C = float(input("Ingrese la capacitancia (F): "))
    
tiempo = np.linspace(0, 5 * R * C, 1000)

# Calcular la carga y descarga del capacitor
carga = V_max * (1 - np.exp(-tiempo / (R * C)))
descarga = V_max * np.exp(-tiempo / (R * C))

# Graficar la carga y descarga del capacitor
plt.plot(tiempo, carga, label='Carga')
plt.plot(tiempo, descarga, label='Descarga')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.title('Carga y Descarga de un Capacitor en un Circuito RC')
plt.legend()
plt.grid(True)
=======
import numpy as np
import matplotlib.pyplot as plt

V_max = float(input("Ingrese el voltaje inicial (V): "))
R = float(input("Ingrese la resistencia (Ω): "))
C = float(input("Ingrese la capacitancia (F): "))
    
tiempo = np.linspace(0, 5 * R * C, 1000)

# Calcular la carga y descarga del capacitor
carga = V_max * (1 - np.exp(-tiempo / (R * C)))
descarga = V_max * np.exp(-tiempo / (R * C))

# Graficar la carga y descarga del capacitor
plt.plot(tiempo, carga, label='Carga')
plt.plot(tiempo, descarga, label='Descarga')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (V)')
plt.title('Carga y Descarga de un Capacitor en un Circuito RC')
plt.legend()
plt.grid(True)
>>>>>>> 93bd2c0f80925fbafb79295064af358832d2eac4
plt.show()
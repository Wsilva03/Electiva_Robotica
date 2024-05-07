import numpy as np

# Longitudes de los eslabones del robot
l1 = 7.5
l2 = 8.5

def direct_kinematics(theta1, theta2):
    # Transformaciones DH
    T01 = np.array([
        [np.cos(theta1), -np.sin(theta1), 0, 0],
        [np.sin(theta1), np.cos(theta1), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

    T12 = np.array([
        [np.cos(theta2), -np.sin(theta2), 0, l1],
        [0, 0, -1, 0],
        [np.sin(theta2), np.cos(theta2), 0, 0],
        [0, 0, 0, 1]
    ])

    # Transformación homogénea del efector final
    T02 = np.dot(T01, T12)

    return T02

# Ejemplo de uso
theta1 = np.deg2rad(45)  # Ángulo de la articulación 1 (en radianes)
theta2 = np.deg2rad(30)  # Ángulo de la articulación 2 (en radianes)

# Calcular la cinemática directa para los ángulos dados
T_efector = direct_kinematics(theta1, theta2)

# Extraer la posición y orientación del efector final
posicion = T_efector[:3, 3]
orientacion = T_efector[:3, :3]

print("Posición del efector final:", posicion)
print("Orientación del efector final:")
print(orientacion)

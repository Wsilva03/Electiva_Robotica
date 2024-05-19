import RPi.GPIO as GPIO
import time

# Configurar el modo de los pines GPIO
GPIO.setmode(GPIO.BCM)

# Definir el pin GPIO al que está conectado el sensor infrarrojo
IR_SENSOR_PIN = 20

# Configurar el pin del sensor como entrada
GPIO.setup(IR_SENSOR_PIN, GPIO.IN)

try:
    print("Probando el sensor infrarrojo. Presiona Ctrl+C para salir.")

    # Bucle principal
    while True:
        # Leer el estado del pin del sensor
        if GPIO.input(IR_SENSOR_PIN) == GPIO.HIGH:
            print("Objeto detectado")
        else:
            print("Ningún objeto detectado")

        # Esperar un segundo antes de volver a leer
        time.sleep(0.3)

except KeyboardInterrupt:
    # Limpiar los pines GPIO antes de salir
    GPIO.cleanup()
    print("\nPrograma detenido.")
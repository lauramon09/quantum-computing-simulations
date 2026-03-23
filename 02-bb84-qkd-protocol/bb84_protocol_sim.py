import random
import matplotlib.pyplot as plt

def simular_bb84():
    print("\n" + "="*40)
    print("   SIMULADOR BB84 - ATAQUE CUÁNTICO")
    print("="*40)
    
    # Configuración inicial
    while True:
        try:
            n_bits = int(input(">> Número de bits a enviar (ej. 1000): "))
            agresividad = int(input(">> Porcentaje de ataque del espía (0-100): "))
            
            if 0 <= agresividad <= 100 and n_bits > 0:
                break 
            else:
                print("Por favor, introduce valores válidos.")
        except ValueError:
            print("Error: Introduce solo números enteros.")

    print(f"\nIniciando transmisión de {n_bits} fotones...")
    print(f"Nivel de agresividad de Eve: {agresividad}%")
    print("Simulando", end="")

    bits_cribados = 0
    errores = 0

    # Simulación del envío de fotones
    for i in range(n_bits):
        # Barra de progreso simple
        if i % (n_bits // 10) == 0:
            print(".", end="", flush=True)

        # Alice genera bit y base
        bit_alice = random.choice([0, 1])
        base_alice = random.choice(["+", "x"])

        # Intervención de Eve
        foton_alterado = False
        if random.randint(1, 100) <= agresividad:
            base_eve = random.choice(["+", "x"])
            if base_eve != base_alice:
                foton_alterado = True

        # Bob mide
        base_bob = random.choice(["+", "x"])

        if foton_alterado:
            bit_bob = random.choice([0, 1])
        else:
            bit_bob = bit_alice

        # Proceso de cribado (sifting)
        if base_alice == base_bob:
            bits_cribados += 1
            if bit_alice != bit_bob:
                errores += 1

    print(" ¡Listo!\n")

    # Cálculos
    tasa_error = 0
    if bits_cribados > 0:
        tasa_error = (errores / bits_cribados) * 100

    # Mostrar informe
    print("-" * 40)
    print("RESULTADOS DE LA SIMULACIÓN")
    print("-" * 40)
    print(f"Bits enviados:            {n_bits}")
    print(f"Bits cribados (útiles):   {bits_cribados}")
    print(f"Bits erróneos:            {errores}")
    print(f"Tasa de Error (QBER):     {tasa_error:.2f}%")
    print("-" * 40)

    if tasa_error > 11:
        print(">>> ALERTA: INTRUSO DETECTADO <<<")
        print("El error supera el 11%. El canal no es seguro.")
    else:
        print(">>> CANAL SEGURO <<<")
        print("Transmisión exitosa.")

    # Generación de la gráfica
    print("\nGenerando gráfico de resultados...")
    
    etiquetas = ['Bits Correctos', 'Bits Erróneos']
    valores = [bits_cribados - errores, errores]
    colores = ['#4CAF50', '#F44336'] # Verde y Rojo

    plt.figure(figsize=(8, 6))
    plt.bar(etiquetas, valores, color=colores)
    plt.title(f'Resultados BB84 - Agresividad: {agresividad}%')
    plt.ylabel('Número de Bits')

    if errores > 0:
        plt.text(1, errores, f"{tasa_error:.1f}% Error",
                 ha='center', va='bottom', fontweight='bold')

    plt.grid(axis='y', alpha=0.3)

    # Línea del límite de seguridad (11%)
    if bits_cribados > 0:
        limite = bits_cribados * 0.11
        plt.axhline(y=limite, color='blue', linestyle='--', label='Límite Seguridad (11%)')
        plt.legend()

    plt.show()

if __name__ == "__main__":
    while True:
        simular_bb84()
        opcion = input("\n¿Otra simulación? (s/n): ").lower()
        if opcion != 's' and opcion != 'si':
            break
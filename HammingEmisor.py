
def calcular_paridad(bits, parity_bits):
    n = parity_bits
    
    # Calculamos paridad para cada bit de paridad
    for i in range(n):
        val = 0
        for j in range(1, len(bits) + 1):
            if(j & (2**i) == (2**i)):
                val = val ^ int(bits[-1 * j]) # -1 * j es usado debido al esquema de orden inverso
            
        # Insertando bits de paridad en las posiciones correctas
        # bits = bits[:len(bits)-2**i] + str(val) + bits[len(bits)-2**i+1:]
        bits = bits[:2**i-1] + str(val) + bits[2**i:]
    return bits

def hamming_codificar(msg):
    # num. de bits de paridad necesarios para el mensaje
    parity_bits = 4
    
    # length of final bit string
    n = len(msg) + parity_bits
    
    # Crear un arreglo para almacenar el mensaje final con bits de paridad
    encoded_msg = [0] * n
    
    # Insertar los bits del mensaje en las posiciones correctas
    j = 0
    for i in range(n):
        if(i == (2**j - 1)):
            # Si la posición es potencia de 2, insertamos un bit de paridad
            encoded_msg[i] = 0
            j += 1
        else:
            # Si la posición no es potencia de 2, insertamos el bit del mensaje
            # encoded_msg[i] = int(msg[-1 * (i-j+1)])
            encoded_msg[i] = int(msg[i-j])

            
    encoded_msg = ''.join([str(bit) for bit in encoded_msg])
    
    # Calcular los bits de paridad
    encoded_msg = calcular_paridad(encoded_msg, parity_bits)
    
    return encoded_msg


# Testing
msg = '1000001'  # mensaje de 7 bits para codificar
encoded_msg = hamming_codificar(msg)
print(f"\nMensaje original: {msg}\n")
print(f"Mensaje codificado: {encoded_msg}\n")


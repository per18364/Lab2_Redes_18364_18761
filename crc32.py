def calculateCRC32(data):
    crc_table = [0] * 256
    polynomial = 0xEDB88320

    for i in range(256):
        crc = i
        for j in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ polynomial
            else:
                crc >>= 1
        crc_table[i] = crc

    crc = 0xFFFFFFFF
    for byte in data:
        crc = crc_table[(crc ^ byte) & 0xFF] ^ (crc >> 8)

    return crc & 0xFFFFFFFF

def verifyCRC32(data, crc):
    return crc == 0xFFFFFFFF - calculateCRC32(data)

# Example received_message and received_crc
received_message = "011011002CB29632"
received_crc = int(received_message[-8:], 16)

# Parse data correctly (assuming data is a hexadecimal string representation)
received_data = bytes.fromhex(received_message[:-8])

if verifyCRC32(received_data, received_crc):
    print("CRC-32 Check: Passed")
    print("Received Data:", received_data.decode('utf-8'))
else:
    print("CRC-32 Check: Failed")

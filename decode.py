def decryption(cin):
    listt = []
    
    for i in range(0, len(cin), 2):  # Process every 2 hex digits (1 byte)
        byte = cin[i:i+2]
        listt.append(int(byte, 16) - 21)  # Convert from hex to int and decrement ASCII value
    
    decoder = ""

    for val in listt:
        decoder += chr(val)  # Convert back to character

    return decoder

# a = str(input("Enter the encrypted text: "))
# res = decryption(a)
# print(res)

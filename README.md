# HexGuard-My-Enhanced-Encryption-Algorithm
In today’s digital landscape, data security is paramount. I’m thrilled to introduce HexGuard, my improved encryption-decryption algorithm designed to ensure data integrity and confidentiality. 
How HexGuard Works:
Encryption

Each character is converted to its ASCII value and incremented by 1.
The incremented values are transformed into a 2-character hexadecimal string.
All hexadecimal strings are concatenated to form a secure encoded message.
Decryption

The hexadecimal string is split into 2-character chunks.
Each chunk is converted back to its ASCII value and decremented by 1.
The adjusted ASCII values are converted back to characters to retrieve the original text.
HexGuard offers a seamless and efficient way to protect sensitive information. Here’s a peek at the code behind HexGuard:

python
Copy code
def encryption(cin):
    listt = [] 
    for i in cin:
        listt.append(ord(i) + 1)
    
    encoder = ""
    for val in listt:
        encoder += hex(val)[2:].zfill(2)
    
    return encoder

def decryption(cin):
    listt = []
    for i in range(0, len(cin), 2):
        byte = cin[i:i+2]
        listt.append(int(byte, 16) - 1)
    
    decoder = ""
    for val in listt:
        decoder += chr(val)
    
    return decoder

# Input and Output
a = str(input("Enter any text: "))
ey = encryption(a)
print(f"AFTER ENCRYPTION : {ey}")
dy = decryption(ey)
print(f"AFTER DECRYPTION : {dy}")
I’m eager to hear your thoughts and feedback on HexGuard!

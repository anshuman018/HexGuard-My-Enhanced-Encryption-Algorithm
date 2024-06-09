from encode import encyption
from decode import decryption

a = str(input("Enter any text: "))

ey = encyption(a)

print()

print(f"AFTER ENCRYPTION : {ey}")

print()

dy = decryption(ey)

print(f"AFTER DECRYPTION : {dy}")


def encyption(cin):
    listt = [] 
    for i in cin:
        listt.append(ord(i) + 21)  # Increment ASCII value by 1
    
    encoder = ""

    for val in listt:
        encoder += hex(val)[2:].zfill(2)  # Convert to hexadecimal and remove '0x' prefix, then pad with zeros if needed

    return encoder

# a = input("Enter a string to encrypt: ")
# res = encryption(a)
# print(res)

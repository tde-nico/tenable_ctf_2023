import base64

flag = 'Zm1jZH92N2tkcFVhbXs6fHNjI2NgaA=='
flag = base64.b64decode(flag)

output = ''.join([chr(flag[i] ^ i) for i in range(len(flag))])

print(output)

# flag{s1lly_jav4scr1pt}

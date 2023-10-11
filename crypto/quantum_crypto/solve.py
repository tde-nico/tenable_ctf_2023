import requests

URL = 'https://nessus-quantumcrypto.chals.io'

payload = {
	"state_list": [[0.0, 1.0]] * 1024,
	"basis_list": ["X"] * 1024,
}

print(payload)
r = requests.post(URL + "/quantum_key", json=payload)
print(r)
print(r.text)


'''
{
	"basis": ["H", "H", "H", "X", "H", "H", "H", "H", "H", "X", "X", "X", "X", "X", "H", "H", "X", "H", "H", "H", "X", "X", "H", "X", "H", "X", "H", "H", "X", "X", "X", "X", "X", "H", "X", "H", "H", "H", "H", "X", "H", "H", "X", "H", "X", "H", "H", "X", "H", "X", "X", "X", "X", "H", "H", "H", "H", "X", "H", "H", "H", "X", "H", "H", "H", "H", "X", "X", "X", "X", "H", "H", "X", "X", "H", "X", "H", "X", "X", "X", "H", "X", "H", "H", "X", "H", "X", "H", "X", "X", "H", "X", "H", "H", "H", "H", "X", "H", "H", "H", "H", "X", "H", "X", "H", "X", "H", "H", "X", "X", "X", "H", "X", "H", "X", "X", "H", "H", "X", "H", "H", "H", "X", "X", "X", "H", "X", "X", "H", "X", "H", "X", "X", "X", "H", "H", "H", "X", "H", "H", "H", "H", "X", "X", "X", "X", "H", "H", "X", "H", "X", "X", "X", "X", "X", "H", "X", "X", "X", "X", "X", "H", "X", "X", "H", "H", "X", "H", "H", "H", "H", "X", "H", "X", "X", "X", "X", "H", "X", "X", "X", "H", "H", "H", "X", "X", "H", "H", "H", "H", "H", "X", "X", "X", "X", "X", "H", "H", "H", "X", "X", "H", "X", "H", "H", "H", "H", "X", "X", "H", "H", "H", "H", "H", "H", "X", "X", "H", "X", "H", "H", "X", "X", "H", "H", "X", "X", "X", "X", "H", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "X", "H", "H", "X", "X", "X", "X", "X", "H", "H", "X", "X", "H", "X", "H", "H", "H", "H", "H", "H", "X", "X", "X", "X", "X", "H", "H", "H", "X", "X", "X", "H", "X", "H", "H", "X", "X", "H", "X", "X", "H", "X", "H", "H", "H", "H", "X", "H", "X", "H", "X", "H", "H", "H", "X", "X", "X", "H", "H", "H", "H", "X", "H", "X", "H", "H", "H", "X", "H", "H", "H", "H", "H", "X", "H", "H", "H", "H", "X", "X", "X", "H", "X", "X", "H", "H", "H", "X", "X", "H", "H", "X", "H", "X", "X", "H", "X", "H", "H", "H", "H", "X", "H", "H", "X", "H", "X", "X", "X", "X", "X", "X", "X", "H", "H", "X", "X", "H", "H", "H", "H", "H", "X", "X", "H", "H", "H", "X", "H", "H", "X", "X", "X", "H", "H", "H", "X", "X", "X", "X", "X", "X", "X", "X", "X", "H", "X", "X", "H", "X", "X", "X", "X", "X", "H", "H", "X", "X", "X", "H", "H", "H", "X", "X", "X", "X", "X", "X", "H", "X", "X", "X", "H", "X", "X", "X", "X", "X", "H", "X", "X", "H", "X", "X", "H", "X", "X", "X", "X", "X", "X", "H", "H", "H", "X", "H", "H", "X", "X", "H", "X", "X", "H", "X", "X", "X", "H", "H", "X", "H", "X", "X", "X", "H", "H", "H", "X", "X", "H", "X", "H", "X", "H", "X", "H", "H", "H", "X", "H", "H", "H", "H", "X", "X", "X", "H", "H", "H", "H", "H", "X", "H", "X", "H", "H", "H", "H", "H", "X", "H", "X", "H", "X", "X", "H", "X", "H", "H", "H", "H", "H", "X", "X", "H", "X", "X", "H", "H", "H", "X", "X", "X", "H", "X", "X", "X", "X", "X", "H", "X", "H", "X", "X", "H", "X", "X", "X", "X", "H", "X", "H", "X", "H", "X", "X", "X", "H", "H", "X", "H", "X", "X", "X", "X", "H", "H", "H", "X", "X", "H", "X", "H", "X", "X", "H", "H", "H", "X", "H", "H", "X", "H", "X", "H", "H", "H", "X", "H", "H", "X", "X", "H", "H", "X", "X", "H", "H", "H", "X", "X", "H", "H", "H", "X", "X", "X", "X", "H", "X", "X", "H", "H", "H", "H", "X", "X", "H", "X", "X", "H", "X", "X", "H", "X", "H", "H", "X", "H", "H", "H", "X", "X", "X", "X", "H", "X", "X", "H", "X", "X", "X", "H", "H", "X", "H", "H", "X", "X", "H", "H", "X", "H", "H", "X", "H", "H", "H", "H", "H", "X", "H", "H", "H", "H", "X", "X", "X", "X", "X", "X", "H", "X", "H", "H", "H", "X", "X", "H", "H", "X", "X", "H", "X", "H", "H", "X", "X", "H", "H", "H", "X", "H", "X", "H", "H", "X", "H", "X", "H", "H", "H", "X", "X", "X", "X", "H", "X", "X", "H", "H", "X", "X", "X", "H", "X", "H", "X", "X", "X", "X", "H", "H", "H", "X", "H", "X", "X", "H", "H", "H", "H", "H", "H", "H", "X", "X", "X", "X", "X", "H", "X", "X", "H", "H", "X", "X", "H", "X", "H", "X", "H", "H", "X", "X", "H", "X", "X", "X", "H", "H", "H", "H", "X", "H", "X", "H", "X", "H", "H", "H", "X", "X", "X", "X", "H", "H", "H", "H", "X", "H", "X", "H", "X", "X", "X", "X", "H", "X", "H", "X", "H", "H", "H", "X", "X", "X", "H", "H", "X", "H", "X", "H", "X", "X", "H", "X", "H", "X", "X", "X", "X", "H", "X", "H", "X", "X", "H", "X", "X", "H", "X", "X", "X", "X", "H", "X", "H", "X", "X", "X", "H", "X", "H", "X", "H", "X", "X", "H", "H", "H", "H", "H", "H", "H", "X", "H", "H", "X", "X", "H", "X", "H", "H", "H", "H", "H", "X", "X", "X", "H", "H", "X", "H", "H", "H", "H", "X", "H", "X", "H", "X", "H", "X", "H", "X", "H", "X", "H", "X", "H", "X", "H", "X", "X", "H", "H", "H", "X", "X", "H", "H", "X", "X", "X", "X", "X", "H", "H", "X", "X", "H", "X", "H", "X", "H", "X", "H", "X", "X", "H", "H", "H", "X", "X", "X", "X", "X", "H", "H", "X", "H", "X", "X", "X", "X", "H", "X", "X", "H", "X", "H", "H", "X", "X", "X", "X", "X", "X", "H", "X", "X", "H", "H", "X", "X", "H", "X", "X", "X", "H", "X", "X", "H", "X", "H", "X", "X", "X", "X", "H", "X", "X", "X", "X", "H", "H", "H", "H", "H", "X", "X", "X", "X", "X", "H", "H", "X", "X", "X", "X", "X", "H", "X", "X", "X", "X", "H", "X", "X", "H", "X", "X", "H", "X", "H", "H", "X", "H", "H", "H", "X", "H", "X", "X", "X", "H", "X", "H", "X", "X", "H", "H", "X", "H", "X", "H", "X", "X", "H", "H", "H", "H", "H", "X", "X", "X", "H", "X", "X", "X", "H", "H", "X", "X", "X", "X", "X", "H", "X", "X", "H", "X", "H"],
	"iv": "iVW8AJgp/AZv5HpK+2W66Q==",
	"ciphertext": "Rn70UmG12y27YpNYdmfiXMXjDNnGrmNghhGB/pZ2yIEVz4w1Hn1B4/SGEPCgcv/Y"
}
'''

import json
import base64
from Crypto.Cipher import AES


content = json.loads(r.text)

key = b'\xff' * 16
iv = base64.b64decode(content['iv'])
c = base64.b64decode(content['ciphertext'])

cipher = AES.new(key, AES.MODE_CBC, iv)
p = cipher.decrypt(c)

print(p)

# b'flag{d0nT_T0uch_QB17s_ar3_FraG1l3}\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e\x0e'

# flag{d0nT_T0uch_QB17s_ar3_FraG1l3}

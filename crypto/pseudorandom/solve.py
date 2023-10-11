import random
import time
import datetime  
import base64

from Crypto.Cipher import AES
iv = b"\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0\0"

flag = "lQbbaZbwTCzzy73Q+0sRVViU27WrwvGoOzPv66lpqOWQLSXF9M8n24PE5y4K2T6Y"
c = base64.b64decode(flag)

for hour in range(24):
	time_stamp = datetime.datetime(2023, 8, 2, hour, 27).timestamp()
	print(time_stamp)
	seed = round(time_stamp * 1000)

	for ms in range(60 * 1000):
		random.seed(seed + ms)

		key = [random.randint(0, 255) for _ in range(16)]
		key = bytearray(key)

		cipher = AES.new(key, AES.MODE_CBC, iv)
		p = cipher.decrypt(c)

		if b'flag' in p:
			print(p)
			print(hour, ms)
			exit()

'''
1690928820.0
1690932420.0
1690936020.0
1690939620.0
1690943220.0
1690946820.0
1690950420.0
1690954020.0
1690957620.0
1690961220.0
1690964820.0
1690968420.0
1690972020.0
1690975620.0
1690979220.0
1690982820.0
1690986420.0
b'flag{r3411y_R4nd0m_15_R3ally_iMp0r7ant}\x00\x00\x00\x00\x00\x00\x00\x00\x00'
16 14439
'''

# flag{r3411y_R4nd0m_15_R3ally_iMp0r7ant}

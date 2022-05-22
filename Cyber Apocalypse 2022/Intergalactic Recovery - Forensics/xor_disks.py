# open disks
d1 = bytearray(open('disk1.img', 'rb').read())
d2 = bytearray(open('disk2.img', 'rb').read())

# new disk to be written
d3 = bytearray(len(d1))

# xor disks and write to new disk
for i in range(len(d1)):
	d3[i] = d1[i] ^ d2[i]

open('disk3_new.img', 'wb').write(d3)
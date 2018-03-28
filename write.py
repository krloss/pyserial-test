from sys import argv
from serial import Serial

# Main
# Serial<id=0xa81c10, open=False>(port='COM1', baudrate=19200, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=0, rtscts=0)
serial = Serial(port=argv[1])

print serial.name
serial.write('--> %s\n' % (argv[2]))
serial.close()


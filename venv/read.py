import serial

n = serial.Serial("COM4",2000000,timeout=1)
data = n.read(100)
for x in data:

    print("0x%x"%x)


from time import sleep
import requests
import json

# Testing
from random import randint

'''
# Open serial connections
s0 = Serial("/dev/ttyUSB0", baudrate=9600, timeout=1)
s1 = Serial("/dev/ttyUSB1", baudrate=9600, timeout=1)
s2 = Serial("/dev/ttyUSB2", baudrate=9600, timeout=1)

s3 = Serial("/dev/ttyUSB3", baudrate=9600, timeout=1)
s4 = Serial("/dev/ttyUSB4", baudrate=9600, timeout=1)
s5 = Serial("/dev/ttyUSB5", baudrate=9600, timeout=1)

s6 = Serial("/dev/ttyUSB6", baudrate=9600, timeout=1)
'''

# Read sensor data
def readSensor():
	'''
	r0 = s0.readline().rstrip().decode("utf-8")
	r1 = s1.readline().rstrip().decode("utf-8")
	r2 = s2.readline().rstrip().decode("utf-8")
	
	r3 = s3.readline().rstrip().decode("utf-8")
	r4 = s4.readline().rstrip().decode("utf-8")
	r5 = s5.readline().rstrip().decode("utf-8")
	
	r6 = s6.readline().rstrip().decode("utf-8")
	'''
	

	# Testing with random data
	r0 = str(randint(300, 400))
	r1 = [
		str(randint(250, 350)),
		str(randint(250, 350)),
		str(randint(250, 350)),
		str(randint(250, 350)),
		str(randint(250, 350)),
		str(randint(250, 350))
	]
	r2 = [str(randint(1, 15)), str(randint(1, 15))]
	r3 = [str(randint(0, 2)), str(randint(0, 2))]
	r4 = [str(randint(0, 100)), str(randint(25, 35)), str(randint(0, 100))]
	r5 = [str(randint(1, 15)), str(randint(1, 15))]
	r6 = [str(randint(1, 20)), str(randint(1, 20))]


	# Return everything as a list of strings
	return [r0, r1, r2, r3, r4, r5, r6]

'''
# Delay start of data reading
sleep(2.5)

# Debugging
for i in range(0, 10):
	for j in readSensor():
		print(j)
		
		# Store as test data
		data = open("data.txt", "a")
		data.write("{}\n".format(j))
		data.close()
'''
while True:
	#for i in range(0,1):	
	sleep(5)
	
	# Read data from sensor
	reads = readSensor()
	
	# Placing sensor data in a dictionary
	sensorData = {
		"water": reads[0],
		"earthquake": reads[1],
		"parking_1": reads[2],
		"garbage": reads[3],
		"parking_2": reads[5],
		"soil": reads[6]
	}
	
	# Convert dictionary to json format
	sensorData = json.dumps(sensorData)
	
	# Send to AWS machine
	res = requests.post("http://18.139.222.15:8000/setAll", sensorData)
	print("{}: {}".format(res.status_code, res.content.decode("utf-8")))


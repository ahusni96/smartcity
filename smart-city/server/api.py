# MODULE IMPORTS
import pymysql as mysql
import numpy
import json
import hug

# OPENING MYSQL CONNECTION
try:
	con = mysql.connect("localhost", "basic", "basic", "smartcity", 6606)

except:
	con.close()
	exit()

# ========== SAVING TO DATABASE ========== #

# QUERY TEMPLATE:
query = "INSERT INTO {} VALUES ({}) {};"

# EXECUTING SQL QUERIES
def executeQuery(query):

	cur = con.cursor()

	if cur.execute(query) > 0:
		cur.close()
		return True

	else:
		cur.close()
		return False

# === SET FUNCTIONS FOR ALL TABLES === #

# data: 2 sets, movementX, movementY, movementZ [0, 1, 2]
@hug.post()
def setEarthquake(input):

	index = 1
	status = []
	input = input.rstrip().split(",")

	for i in range(0, 2):

		value = [
			float(input[index - 1]),
			float(input[index]),
			float(input[index + 1])
		]

		table = "earthquake (sensorID, movementX, movementY, movementZ)"
		values = "'S{}', {}, {}, {}".format(i + 1, value[0], value[1], value[2])
		conditions = ""

		sql = query.format(table, values, conditions)

		status.append(executeQuery(sql))

		index += 2

	if False in status:
		return False
	else:
		return True


# data: humidity, temperature, quality [0, 1, 2]
@hug.post()
def setAir(input):

	input = input.rstrip().split(",")

	for i in range(0, len(input)):
		input[i] = float(input[i])

	table = "air (airHumidity, airTemperature, airQuality)"
	values = "{}, {}, {}".format(float(input[0]), float(input[1]), float(input[2]))
	conditions = ""

	sql = query.format(table, values, conditions)

	return executeQuery(sql)

# data: turbidity [0]
@hug.post()
def setWater(input):

	input = float(input)

	if input < 400:
		status = "dirty"

	else:
		status = "clean"

	table = "water (waterTurbidity, waterStatus)"
	values = "{}, '{}'".format(input, status)
	conditions = ""

	sql = query.format(table, values, conditions)

	return executeQuery(sql)

# data: moisture1, moisture2 [0, 1]
@hug.post()
def setSoil(input):

	input = input.rstrip().split(",")

	for i in range(0, len(input)):
		input[i] = float(input[i])

	mean = (input[0] + input[1]) / 2

	if mean > 15:
		status = "Wet"

	else:
		status = "Dry"

	table = "soil (soilMoisture, soilStatus)"
	values = "{}, '{}'".format(mean, status)
	conditions = ""

	sql = query.format(table, values, conditions)

	return executeQuery(sql)

# data: ultrasonic1, ultrasonic2 [0, 1]
@hug.post()
def setParking(input):

	status = []

	input = input.rstrip().split(",")

	for i in range(0, len(input)):
		input[i] = float(input[i])

		table = "parking (spaceID, spaceStatus)"
		values = "'S{}', '{}'".format(i + 1, input[i])
		conditions = ""

		sql = query.format(table, values, conditions)

		status.append(executeQuery(sql))

	if False in status:
		return False
	else:
		return True

# data: weight1, weight2 [0, 1]
@hug.post()
def setGarbage(input):

	status = []

	input = input.rstrip().split(",")

	for i in range(0, len(input)):
		input[0] = float(input[i])

		if input[i] > 20:
			status = "full"
		else:
			status = "empty"

		table = "garbage (garbageID, garbageWeight, garbageStatus)"
		values = "'G{}', {}, {}".format(i + 1, input[i], status)
		conditions = ""

		sql = query.format(table, values, conditions)

		status.append(executeQuery)

	if False in status:
		return False
	else:
		return True


# === REQUEST HANDLER (HTTP_POST) === #
@hug.post()
def setAll(body):

	# Convert body to dictionary
	body = json.loads(body)


	# Get boolean from functions
	air = setAir(body["air"])
	earthquake = setEarthquake(body["earthquake"])
	#garbage = setGarbage(body["garbage"])
	parking = setParking(body["parking_1"] + "," + body["parking_2"])
	soil = setSoil(body["soil"])
	water = setWater(body["water"])

	message = "This is the default message! Please change!"

	if air and earthquake and parking and soil and water: #and garbage
		message = "Success"
		con.commit()

	else:
		message = "Fail"
		con.rollback()

	return message

# ========== FETCHING FROM DATABASE ========== #

# QUERY TEMPLATE:
select = "SELECT {} FROM {} ORDER BY logID DESC LIMIT {};"

def executeGet(columns, table, limit):
	try:
		cur = con.cursor()

		try:
			cur.execute(select.format(columns, table, limit))

			try:

				if limit > 1:
					results = cur.fetchall()

				else:
					results = cur.fetchone()

				cur.close()
				return results

			except:
				cur.close()
				return "Fetch fail"
		except:
			cur.close()
			return "Execute fail"
	except:
		return "Cursor fail"

@hug.get()
def getAir():

	columns = "airHumidity, airTemperature, airQuality"
	table = "air"
	limit = 1

	datas = executeGet(columns, table, limit)
	return {
		"humidity": datas[0],
		"temperature": datas[1],
		"quality": datas[2]
	}

@hug.get()
def getEarthquake():

	count = 1
	datas = {}

	cur = con.cursor()
	cur.execute("SELECT DISTINCT sensorID FROM earthquake;")
	sensorID = cur.fetchall()
	cur.close()

	for i in range(0, len(sensorID)):

		columns = "movementX, movementY, movementZ"
		table = "earthquake WHERE sensorID = 'S{}'".format(count)
		limit = 1

		data = executeGet(columns, table, limit)
		datas["S{}".format(count)] = { "x": data[0], "y": data[1], "z": data[2] }

		count += 1

	return datas

@hug.get()
def getWater():

	columns = "waterTurbidity, waterStatus"
	table = "water"
	limit = 1

	datas = executeGet(columns, table, limit)

	return {
		"turbidity": datas[0],
		"status": datas[1]
	}

@hug.get()
def getSoil():

	columns = "soilMoisture, soilStatus"
	table = "soil"
	limit = 1

	datas = executeGet(columns, table, limit)

	return {
		"moisture": datas[0],
		"status": datas[1]
	}

@hug.get()
def getParking():

	count = 1
	datas = {}

	cur = con.cursor()
	cur.execute("SELECT DISTINCT spaceID FROM parking;")
	parkingID = cur.fetchall()
	cur.close()

	for i in range(0, len(parkingID)):

		id = "S{}".format(count)
		columns = "spaceStatus"
		table = "parking WHERE spaceID = '{}'".format(id)
		limit = 1

		data = executeGet(columns, table, limit)
		datas[id] = { "status": data }

		count += 1

	return datas

@hug.get()
def getGarbage():

	count = 1
	datas = {}

	cur = con.cursor()
	cur.execute("SELECT DISTINCT garbageID FROM garbage;")
	garbageID = cur.fetchall()
	cur.close()

	for i in range(0, len(garbageID)):

		id = "G{}".format(count)
		columns = "garbageWeight, garbageStatus"
		table = "garbage WHERE garbageID = '{}'".format(id)
		limit = 1

		data = executeGet(columns, table, limit)
		datas[id] = { "weight": data[0], "status": data[1] }

		count += 1

	return datas

# REQUEST HANDLER (HTTP_GET)
@hug.get()
def getAll():

	all = {}

	all["air"] = getAir()
	all["earthquake"] = getEarthquake()
	all["parking"] = getParking()
	all["soil"] = getSoil()
	all["water"] = getWater()
	all["garbage"] = getGarbage()

	all = json.dumps(all)

	return all

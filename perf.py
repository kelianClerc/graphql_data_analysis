class Perf:
	className = ""
	timestampSent = 0
	timestampReceive = 0
	requestSize = 0
	responseSize = 0
	roundTrips = 0
	utileRatio = 0
	requestType = 0
	endpoint = ""

	def __init__(self, fileData):
		data = fileData.split("###")
		if len(data) == 9 :
			self.className = data[0]
			self.timestampSent = int(data[1])
			self.timestampReceive = int(data[2])
			self.requestSize = int(data[3])
			self.responseSize = int(data[4])
			self.roundTrips = int(data[5])
			self.utileRatio = int(data[6])
			self.requestType = int(data[7])
			self.endpoint = data[8]

	def getDuration(self):
		return self.timestampReceive - self.timestampSent

	def exists(self, pref):
		return pref.className == self.className and pref.requestType == self.requestType #and pref.endpoint == self.endpoint

	def isMirrorOf(self, pref):
		return pref.className == self.className and pref.requestType != self.requestType #and pref.endpoint == self.endpoint

	def __str__(self):
		result = "In activity " + self.className + ", query duration : "+ str(self.timestampReceive - self.timestampSent)
		result += "(" + str(self.timestampReceive) + ", " + str(self.timestampSent) + ")";
		result += " - of type : " + str(self.requestType)
		return  result
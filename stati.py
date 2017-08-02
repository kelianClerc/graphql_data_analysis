class Stati:
	def __init__(self, firstData):
		self.durations = []
		self.durations.append(firstData.getDuration());
		self.realDuration = []
		self.realDuration.append(firstData.realDuration);
		self.sizes = []
		self.sizes.append(firstData.responseSize);
		self.roundTrip = []
		self.roundTrip.append(firstData.roundTrips);

	def calculateDurationMean(self):
		return sum(self.durations) / len(self.durations);

	def calculateRealDurationMean(self):
		return sum(self.realDuration) / len(self.realDuration);

	def addValue(self,value):
		self.durations.append(value.getDuration());
		self.realDuration.append(value.realDuration);
		self.sizes.append(value.responseSize);
		self.roundTrip.append(value.roundTrips);

	def getTotalDurations(self):
		result = []
		last = 0
		for val in self.durations:
			result.append(val + last)
			last += val
		return result

	def getTotalRealDuration(self):
		result = []
		last = 0
		for val in self.realDuration:
			result.append(val + last)
			last += val
		return result

	def getTotalResponseSize(self):
		result = []
		last = 0
		for val in self.sizes:
			result.append(val + last)
			last += val
		return result

	def getTotalRoundTrip(self):
		result = []
		last = 0
		for val in self.roundTrip:
			result.append(val + last)
			last += val
		return result
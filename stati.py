class Stati:
	def __init__(self, firstData):
		self.durations = []
		self.durations.append(firstData.getDuration());
		self.sizes = []
		self.sizes.append(firstData.responseSize);

	def calculateDurationMean(self):
		return sum(self.durations) / len(self.durations);

	def addValue(self,value):
		self.durations.append(value.getDuration());
		self.sizes.append(value.responseSize);

	def getTotalDurations(self):
		result = []
		for val in self.durations:
			result.append(val + sum(result))
		return result

	def getTotalResponseSize(self):
		result = []
		for val in self.sizes:
			result.append(val + sum(result))
		return result
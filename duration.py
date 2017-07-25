
from stati import Stati
class Duration:
	pref = ""
	stat = ""

	def __init__(self, pref):
		self.pref = pref
		self.stat = Stati(pref);

	def addValue(self, pref):
		self.stat.addValue(pref)

	def getDurationMean(self):
		return self.stat.calculateDurationMean()

	def exists(self, pref):
		return self.pref.exists(pref);
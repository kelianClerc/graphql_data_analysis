from perf import Perf
from duration import Duration
import matplotlib.pyplot as plt

defaultPath = "../data/mock1.graphdata"
dataPerf = []
dataSample = []

def readFile(path):
	file = open(path, "r"); 
	return file.readlines()

def buildObjects(lines):
	for line in lines:
		dataPerf.append(Perf(line.rstrip()))

def getTimePerActivity():
	durations = []
	for perf in dataPerf:
		exists = False
		for duration in durations:
			if duration.exists(perf):
				duration.addValue(perf)
				exists = True
		if exists:
			pass
		else:
			duration = Duration(perf)	
			durations.append(duration)
	return durations

def getMirrorMesure(toCompare):
	if len(dataSample) <= 0:
		return 
	for sample in dataSample:
		if sample.pref.isMirrorOf(toCompare):
			return sample
	return None;

def appendTotalValue(vals, toAppends):
	for toAppend in toAppends :
		vals.append(toAppend + sum(vals));
	return vals;

def getTypeEvolution():
	graphql =[0]
	rest = [0]
	for sample in dataSample:
		if sample.pref.requestType == 2:
			continue;
		rest = appendTotalValue(rest, sample.stat.getTotalDurations())
		graphql = appendTotalValue(graphql, getMirrorMesure(sample.pref).stat.getTotalDurations())

	print graphql
	print rest

	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.plot(graphql, marker="o", label="GraphQL")
	ax.plot(rest, marker="o", label="Rest")
	ax.legend(loc="upper right")
	ax.set_xlabel("Screen navigation")
	ax.set_ylabel("Cumulated query duration")
	plt.xticks(range(1, len(rest)))
	plt.show()

def getSizeReceivedEvolution():
	graphql =[0]
	rest = [0]
	for sample in dataSample:
		if sample.pref.requestType == 2:
			continue;
		rest = appendTotalValue(rest, sample.stat.getTotalResponseSize())
		graphql = appendTotalValue(graphql, getMirrorMesure(sample.pref).stat.getTotalResponseSize())

	print graphql
	print rest

	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.plot(graphql, marker="o", label="GraphQL")
	ax.plot(rest, marker="o", label="Rest")
	ax.legend(loc="upper right")
	ax.set_xlabel("Screen navigation")
	ax.set_ylabel("Cumulated response size")
	plt.xticks(range(1, len(rest)))
	plt.show()

def meanByActivity():
	#Take a duration calculate mean and plot array of means


buildObjects(readFile(defaultPath))
dataSample = getTimePerActivity()

#plt.plot(dataSample[0].stat.getTotalValues())
#plt.plot(getMirrorMesure(dataSample[0].pref).stat.getTotalValues())
#plt.show()

getTypeEvolution();
getSizeReceivedEvolution();

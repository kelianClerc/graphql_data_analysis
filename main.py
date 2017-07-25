from perf import Perf
from duration import Duration
import numpy as np
import matplotlib.pyplot as plt

defaultPath = "./data/mock1.graphdata"
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

def sortResultAndDisplay():
	graphqlDurationEvolution =[0]
	restDurationEvolution = [0]	
	graphqlSizeEvolution =[0]
	restSizeEvolution = [0]
	graphqlTimeByActivity = []
	restTimeByActivity = []
	xLabel = []

	for sample in dataSample:
		if sample.pref.requestType == 2:
			continue;
		restDurationEvolution = appendTotalValue(restDurationEvolution, sample.stat.getTotalDurations())
		graphqlDurationEvolution = appendTotalValue(graphqlDurationEvolution, getMirrorMesure(sample.pref).stat.getTotalDurations())
		restSizeEvolution = appendTotalValue(restSizeEvolution, sample.stat.getTotalResponseSize())
		graphqlSizeEvolution = appendTotalValue(graphqlSizeEvolution, getMirrorMesure(sample.pref).stat.getTotalResponseSize())
		restTimeByActivity.append(sample.stat.calculateDurationMean())
		graphqlTimeByActivity.append(getMirrorMesure(sample.pref).stat.calculateDurationMean())
		xLabel.append(sample.pref.className)

	showDurationEvolution(graphqlDurationEvolution, restDurationEvolution)
	showCumulatedSizeEvolution(graphqlSizeEvolution, restSizeEvolution)
	showDurationByActivity(graphqlTimeByActivity, restTimeByActivity, xLabel)

def showDurationEvolution(graphqlDurationEvolution, restDurationEvolution):
	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.plot(graphqlDurationEvolution, marker="o", label="GraphQL")
	ax.plot(restDurationEvolution, marker="o", label="Rest")
	ax.legend(loc="upper right")
	ax.set_xlabel("Screen navigation")
	ax.set_ylabel("Cumulated query duration")
	plt.xticks(range(1, len(restDurationEvolution)))
	plt.show()

def showCumulatedSizeEvolution(graphqlSizeEvolution, restSizeEvolution):
	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.plot(graphqlSizeEvolution, marker="o", label="GraphQL")
	ax.plot(restSizeEvolution, marker="o", label="Rest")
	ax.legend(loc="upper right")
	ax.set_xlabel("Screen navigation")
	ax.set_ylabel("Cumulated response size")
	plt.xticks(range(1, len(restSizeEvolution)))
	plt.show()

def showDurationByActivity(graphqlTimeByActivity, restTimeByActivity, xLabel):
	n_groups = len(graphqlTimeByActivity)
	index = np.arange(n_groups)
	bar_width = 0.25

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.bar(index, graphqlTimeByActivity, bar_width, color="b", label="GraphQL")
	ax.bar(index + bar_width, restTimeByActivity, bar_width, color="r", label="Rest")
	ax.legend(loc="upper right")
	ax.set_xlabel("Activity Name")
	ax.set_ylabel("Mean waiting time")
	plt.xticks(index + bar_width, xLabel)
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
	print "wip"
	graphql = []
	rest = []


	#Take a duration calculate mean and plot array of means


buildObjects(readFile(defaultPath))
dataSample = getTimePerActivity()

#plt.plot(dataSample[0].stat.getTotalValues())
#plt.plot(getMirrorMesure(dataSample[0].pref).stat.getTotalValues())
#plt.show()

sortResultAndDisplay();

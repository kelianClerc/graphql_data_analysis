from perf import Perf
from duration import Duration
import numpy as np
import matplotlib.pyplot as plt
import sys

defaultPath = "./data/mockgen.graphdata"
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

def getIndividualMirrorMesure(toCompare):
	if len(dataPerf) <= 0:
		return 
	for sample in dataPerf:
		if sample.isMirrorOf(toCompare):
			return sample
	return None;


def appendTotalValue(vals, toAppends):
	last = vals[len(vals) - 1]
	for toAppend in toAppends :
		vals.append(last + toAppend);
		last += toAppend;
	return vals;

def SortChronologicaly():
	graphqlDurationEvolution =[0]
	restDurationEvolution = [0]
	graphqlSizeEvolution =[0]
	restSizeEvolution = [0]
	graphqlRequestSizeEvolution =[0]
	restRequestSizeEvolution = [0]
	graphqlRoundTripEvolution = [0]
	restRoundTripEvolution = [0]
	annotation = [""]
	for sample in dataPerf:
		if sample.requestType == 2:
			continue
		restDurationEvolution = appendEvolutionValue(restDurationEvolution, sample.getDuration())
		restSizeEvolution = appendEvolutionValue(restSizeEvolution, sample.responseSize)
		restRequestSizeEvolution = appendEvolutionValue(restRequestSizeEvolution, sample.requestSize)
		restRoundTripEvolution = appendEvolutionValue(restRoundTripEvolution, sample.roundTrips)
		toCompare = getIndividualMirrorMesure(sample);
		if toCompare == None:
			graphqlDurationEvolution = appendEvolutionValue(graphqlDurationEvolution, 0)
			graphqlSizeEvolution = appendEvolutionValue(graphqlSizeEvolution, 0)
			graphqlRequestEvolution = appendEvolutionValue(graphqlRequestSizeEvolution, 0)
			graphqlRoundTripEvolution = appendEvolutionValue(graphqlRoundTripEvolution, 0)
		else:
			graphqlDurationEvolution = appendEvolutionValue(graphqlDurationEvolution, toCompare.getDuration())
			graphqlSizeEvolution = appendEvolutionValue(graphqlSizeEvolution, toCompare.responseSize)
			graphqlRequestSizeEvolution = appendEvolutionValue(graphqlRequestSizeEvolution, toCompare.requestSize)
			graphqlRoundTripEvolution = appendEvolutionValue(graphqlRoundTripEvolution, toCompare.roundTrips)
		annotation.append(sample.endpoint)

	showDurationEvolution(graphqlDurationEvolution, restDurationEvolution, annotation)
	showCumulatedSizeEvolution(graphqlSizeEvolution, restSizeEvolution, annotation)
	showRequestSizeEvolution(graphqlRequestSizeEvolution, restRequestSizeEvolution, annotation)
	showRoundTripEvolution(graphqlRoundTripEvolution, restRoundTripEvolution, annotation)

def appendEvolutionValue(lastValue, toAdd):
	total = lastValue[len(lastValue) - 1];
	lastValue.append(toAdd + total)
	return lastValue;


def showDurationEvolution(graphqlDurationEvolution, restDurationEvolution, annotation):
	fig = plt.figure()
	ax = fig.add_subplot(111)

	print(restDurationEvolution)

	ax.plot(graphqlDurationEvolution, marker="o", label="GraphQL")
	ax.plot(restDurationEvolution, marker="o", label="Rest")
	ax.legend(loc="upper left")
	ax.set_xlabel("Screen navigation")
	ax.set_ylabel("Cumulated query duration (ms)")
	plt.xticks(range(1, len(restDurationEvolution)))

	for i in xrange(1,len(graphqlDurationEvolution)):
		print graphqlDurationEvolution[i], i, annotation[i]
		offset = -1 if i % 2 == 0 else 1
		ax.annotate(annotation[i], xy=(i - 0.5, graphqlDurationEvolution[i]+100 * offset))
		ax.annotate(annotation[i], xy=(i - 0.5, restDurationEvolution[i]+100 * offset))


	plt.show()

def showCumulatedSizeEvolution(graphqlSizeEvolution, restSizeEvolution, annotation):
	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.plot(graphqlSizeEvolution, marker="o", label="GraphQL")
	ax.plot(restSizeEvolution, marker="o", label="Rest")
	ax.legend(loc="upper left")
	ax.set_xlabel("Screen navigation")
	ax.set_ylabel("Cumulated response size")
	plt.xticks(range(1, len(restSizeEvolution)))
	for i in xrange(1,len(graphqlSizeEvolution)):
		print graphqlSizeEvolution[i], i, annotation[i]
		offset = -1 if i % 2 == 0 else 1
		ax.annotate(annotation[i], xy=(i - 0.5, graphqlSizeEvolution[i]+2000 * offset))
		ax.annotate(annotation[i], xy=(i - 0.5, restSizeEvolution[i]+2000 * offset))
	plt.show()

def showRequestSizeEvolution(graphqlSizeEvolution, restSizeEvolution, annotation):
	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.plot(graphqlSizeEvolution, marker="o", label="GraphQL")
	ax.plot(restSizeEvolution, marker="o", label="Rest")
	ax.legend(loc="upper left")
	ax.set_xlabel("Screen navigation")
	ax.set_ylabel("Cumulated request size")
	plt.xticks(range(1, len(restSizeEvolution)))
	for i in xrange(1,len(graphqlSizeEvolution)):
		print graphqlSizeEvolution[i], i, annotation[i]
		offset = -1 if i % 2 == 0 else 1
		ax.annotate(annotation[i], xy=(i - 0.5, graphqlSizeEvolution[i]+100 * offset))
		ax.annotate(annotation[i], xy=(i - 0.5, restSizeEvolution[i]+100 * offset))
	plt.show()

def showRoundTripEvolution(graphqlRoundTripEvolution, restRoundTripEvolution, annotation):
	fig = plt.figure()
	ax = fig.add_subplot(111)

	print(restRoundTripEvolution)

	ax.plot(graphqlRoundTripEvolution, marker="o", label="GraphQL")
	ax.plot(restRoundTripEvolution, marker="o", label="Rest")
	ax.legend(loc="upper left")
	ax.set_xlabel("Screen navigation")
	ax.set_ylabel("Cumulated RoundTrip")
	plt.xticks(range(1, len(restRoundTripEvolution)))

	for i in xrange(1,len(graphqlRoundTripEvolution)):
		print graphqlRoundTripEvolution[i], i, annotation[i]
		offset = -1 if i % 2 == 0 else 1
		ax.annotate(annotation[i], xy=(i - 0.5, graphqlRoundTripEvolution[i]+2 * offset))
		ax.annotate(annotation[i], xy=(i - 0.5, restRoundTripEvolution[i]+2 * offset))


	plt.show()

def sortResultAndDisplay():
	graphqlTimeByActivity = []
	restTimeByActivity = []
	xLabel = []

	for sample in dataSample:
		if sample.pref.requestType == 2:
			continue;
		restTimeByActivity.append(sample.stat.calculateDurationMean())
		graphqlTimeByActivity.append(getMirrorMesure(sample.pref).stat.calculateDurationMean())

		xLabel.append(sample.pref.className)

	showDurationByActivity(graphqlTimeByActivity, restTimeByActivity, xLabel)

def showDurationByActivity(graphqlTimeByActivity, restTimeByActivity, xLabel):
	n_groups = len(graphqlTimeByActivity)
	index = np.arange(n_groups)
	bar_width = 0.25

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.bar(index, graphqlTimeByActivity, bar_width, color="b", label="GraphQL")
	ax.bar(index + bar_width, restTimeByActivity, bar_width, color="r", label="Rest")
	ax.legend(loc="upper left")
	ax.set_xlabel("Activity Name")
	ax.set_ylabel("Mean waiting time")
	plt.xticks(index + bar_width, xLabel)
	plt.show()


def showEvolution(graphqlDurationEvolution, restDurationEvolution, graphqlSizeEvolution, restSizeEvolution) :
	fig = plt.figure()
	ax = fig.add_subplot(211)
	ax2 = fig.add_subplot(212)

	print(restDurationEvolution)

	ax.plot(graphqlDurationEvolution, marker="o", label="GraphQL")
	ax.plot(restDurationEvolution, marker="o", label="Rest")
	ax.legend(loc="upper left")
	ax.set_xlabel("Screen navigation")
	ax.set_ylabel("Cumulated query duration")
	ax.set_xticks(range(1, len(restDurationEvolution)))

	ax2.plot(graphqlSizeEvolution, marker="o", label="GraphQL")
	ax2.plot(restSizeEvolution, marker="o", label="Rest")
	ax2.legend(loc="upper left")
	ax2.set_xlabel("Screen navigation")
	ax2.set_ylabel("Cumulated response size")
	ax2.set_xticks(range(1, len(restSizeEvolution)))
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
	ax.legend(loc="upper left")
	ax.set_xlabel("Screen navigation")
	ax.set_ylabel("Cumulated response size")
	plt.xticks(range(1, len(rest)))
	plt.show()

def meanByActivity():
	print "wip"
	graphql = []
	rest = []


	#Take a duration calculate mean and plot array of means

if len(sys.argv) > 1:
	defaultPath = sys.argv[1]

buildObjects(readFile(defaultPath))
dataSample = getTimePerActivity()

#plt.plot(dataSample[0].stat.getTotalValues())
#plt.plot(getMirrorMesure(dataSample[0].pref).stat.getTotalValues())
#plt.show()

#sortResultAndDisplay();
SortChronologicaly();

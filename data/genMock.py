import random

activities = ["Main Activity", "Profile Activity", "Create New Post", "Update value", "User List"]

file = open("mockgen.graphdata", "w")

def generateRandomData():
	for i in range(0, 50):
		activity = random.randint(0, len(activities)-1);
		generateRestData(activity);
		generateGraphqlData(activity);

def generateRestData(activity):
	startTime = random.randint(0,1000);
	offset = random.randint(100, 300);
	endTime = startTime + offset;
	duration = offset - random.randint(10,40);
	sentSize = random.randint(150, 250);
	receivedSize = random.randint(300, 2000);
	roundtrip = random.randint(1,5)
	use = random.randint(20, 50)
	s = "###"
	seq = (activities[activity], str(startTime), str(endTime), str(duration), str(sentSize), str(receivedSize), str(roundtrip), str(use), "1", "gen") 
	message = s.join(seq) + "\n"
	print message
	file.write(message)

def generateGraphqlData(activity):
	startTime = random.randint(0,1000);
	offset = random.randint(100, 300);
	endTime = startTime + offset;
	duration = offset - random.randint(10,40);
	sentSize = random.randint(150, 550);
	receivedSize = random.randint(50, 800);
	roundtrip = 1
	use = 100
	s = "###"
	seq = (activities[activity], str(startTime), str(endTime), str(duration), str(sentSize), str(receivedSize), str(roundtrip), str(use), "2", "gen")
	message = s.join(seq) + "\n"
	file.write(message)

generateRandomData()	
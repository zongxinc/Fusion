import os
import json

with open('./room_information.json') as f:
	room_information = json.load(f)
RP = []
for i in room_information[0]["thermal address"]:
	RP.append(i)
while(1):
	os.system("rsync -zaP " + RP[0] + ":./Buffer/ ./RP1")
	os.system("rsync -zaP " + RP[1] + ":./Buffer/ ./RP2")
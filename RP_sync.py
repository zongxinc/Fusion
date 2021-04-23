import os
import json

with open('./room_information.json') as f:
	room_information = json.load(f)
RP = []
for i in room_information:
	for j in i['thermal']:
		RP.append(j['thermal_ip'])
print(RP[0])
while(1):
	count = 1
	for ip in RP:
		os.system("rsync -zaP " + ip + ":/home/pi/Buffer/ ./RP" + str(count))
		count+=1
		# os.system("rsync -zaP " + RP[1] + ":./Buffer/ ./RP2")

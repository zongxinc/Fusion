import os
import json

print("hhere")
with open('./room_information.json') as f:
	room_information = json.load(f)
RP = []


for j in room_information[1]['thermal']:
	RP.append(j['thermal_ip'])
print("RP sync:", RP[0])
while(1):
	count = len(room_information[0]['thermal']) + 1
	for ip in RP:
		print("rsync -zaP " + ip + ":/home/pi/Buffer/ ./RP" + str(count))
		os.system("rsync -zaP " + ip + ":/home/pi/Buffer/ ./RP" + str(count))
		count+=1
		# os.system("rsync -zaP " + RP[1] + ":./Buffer/ ./RP2")

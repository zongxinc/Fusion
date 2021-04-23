import json
import string

print("how many rooms are you going to use:")
roomNum = input()
MAC = {}
MAC["OFC-1"] = "ACCC8EB4A2D9"
MAC["OFC-2"] = 'ACCC8EB66056'
MAC["OFC-3"] = "ACCC8EB65F9D"
MAC["TDS-1"] = "ACCC8E655F9D"
MAC["TDS-2"] = "ABCC8E655F9D"
MAC["TDS-3"] = "ABBC8E655F9D"
MAC["TDS-4"] = "ABCC8Y655F9D"

information = []
for i in range(int(roomNum)):
	camAddress = {}
	thermAddress = {}
	print("how many cameras are there gonna be in room " + str(i + 1))
	camCount = input()
	roomInfor = {"room # " : i + 1, "camera" : [], "thermal" : []}
	for j in range(int(camCount)):
		print("what is the id of camera " + str(j + 1) + " in room " + str(i + 1))
		camid = input()
		print("what is the address of camera " + str(j + 1) + " " + MAC[camid] + " in room " + str(i + 1))
		address = input()
		# camAddress['cam_id'] = camid
		# camAddress['cam_ip'] = address
		roomInfor['camera'].append({'cam_id': camid, 
											'cam_ip' :address })
		# print(roomInfor['camera address'])

	print("how many thermal sensors are there gonna be in room " + str(i + 1))
	thermCount = input()

	for j in range(int(thermCount)):
		print("what is the id of thermal sensor " + str(j + 1) + " in room " + str(i + 1))
		thermid =  input()
		print("what is the address of thermal sensor " + str(j + 1) + " " + MAC[thermid]+ " in room " + str(i + 1))
		address = 'pi@' + input()
		# thermAddress['thermal_id'] = thermid
		# thermAddress['thermal_ip'] = address
		roomInfor['thermal'].append({'thermal_id': thermid,
											 'thermal_ip': address})

	# roomInfor = {"room # " : i + 1, "camera address" : camAddress, "thermal address" : thermAddress}
	information.append(roomInfor)
with open('./room_information.json', 'w') as f:
	json.dump(information, f, indent=2)


	




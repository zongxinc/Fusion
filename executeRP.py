import sys, getopt
import os
import json
from datetime import datetime


try:
	opts, args = getopt.getopt(sys.argv[1:], "p:R:", ["H="])
except getopt.GetoptError:
	print("Error: modified_filter.py MCSOA:B:Imsf")
	sys.exit()


for opt, arg in opts:
	if opt in ("-p", "--command"):
		RP = arg
	if opt in ("-R", "--roomnum"):
		roomnum = int(arg)
RP = RP.replace('_', ' ')
print(RP)
with open('./room_information.json') as f:
	temp = json.load(f)
count = 1
for i in temp:
	for j in i['thermal']:
		# os.system('ssh ' + j['thermal_ip'] + ' ' + RP + '&')
		os.system('mkdir ' + ('RP'+str(count)))
		count += 1
		# print('ssh ' + j['thermal_ip'] + ' ' + RP + '&')
print(roomnum)
for i in temp[roomnum-1]['thermal']:
	os.system('ssh ' + i['thermal_ip'] + ' ' + RP + '&')
	print(i)
	print('ssh ' + i['thermal_ip'] + ' ' + RP + '&')




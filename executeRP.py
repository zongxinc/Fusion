import sys, getopt
import os
import json
from datetime import datetime


try:
	opts, args = getopt.getopt(sys.argv[1:], "p:", ["H="])
except getopt.GetoptError:
	print("Error: modified_filter.py MCSOA:B:Imsf")
	sys.exit()

for opt, arg in opts:
	if opt in ("-p", "--command"):
		RP = arg
RP = RP.replace('_', ' ')
print(RP)
with open('./room_information.json') as f:
	temp = json.load(f)
count = 1
for i in temp:
	for j in i['thermal']:
		os.system('ssh ' + j['thermal_ip'] + ' ' + RP + '&')
		os.system('mkdir ' + ('RP'+str(count)))
		count += 1
		print('ssh ' + j['thermal_ip'] + ' ' + RP + '&')


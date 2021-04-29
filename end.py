import os
import json
import sys, getopt
# os.system("kill -9 $(ps -aux | grep RP_sync.py | awk '{print $2}')")
# os.system("kill -9 $(ps -aux | grep modified_filter_twoCameras.py | awk '{print $2}')")
# os.system("kill -9 $(ps -aux | grep axis_cameras_single_cam_v2_copy.py | awk '{print $2}')")

with open("./room_information.json") as f:
	info = json.load(f)

try:
	opts, args = getopt.getopt(sys.argv[1:], "R:")
except getopt.GetoptError:
	print("Error: modified_filter.py -N <reportTime>")
	sys.exit()

for opt, arg in opts:
	if opt in ("-R", "roomnum"):
		roomnum = int(arg)

for ip in info[roomnum - 1]['thermal']:
	print("ssh " + ip['thermal_ip'] + " python3 end.py")
	os.system("ssh " + ip['thermal_ip'] + " python3 end.py &")
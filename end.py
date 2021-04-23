import os
import json

# os.system("kill -9 $(ps -aux | grep RP_sync.py | awk '{print $2}')")
# os.system("kill -9 $(ps -aux | grep modified_filter_twoCameras.py | awk '{print $2}')")
# os.system("kill -9 $(ps -aux | grep axis_cameras_single_cam_v2_copy.py | awk '{print $2}')")

with open("./room_information.json") as f:
	info = json.load(f)

for r in info:
	for ip in r['thermal']:
		# print(str("ssh " + ip['thermal_ip'] + "" kill -9 $(ps -aux | grep run.py | awk '{print $2}') + "&"))
		os.system("sh end.sh -p " + ip['thermal_ip'])
		# os.system(str("ssh " + ip['thermal_ip'] + "' kill -9 $(ps -aux | grep run.py | awk '{print $2}')'" + "&"))
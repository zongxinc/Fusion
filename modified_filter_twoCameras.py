import json
import os
import numpy as np
import matplotlib.pyplot as plt
import sys, getopt
import time

# Here are all the variables
# RPLast = 0

short_window = 7
long_window = 25
RP_ts = [] # store all the timestamps from the Raspberry Pis
RP_count = [] # store all the count from the Raspberry Pis
RPdict = [] # this is an array of dictionaries each element is a dictionary of timestamp and count for each RP devices
maxFileNum = 0 # currently in all the RP directories, the max number of files in all RP directories
RPIndex = 0 # the index of last visited element in RP_ts and RP_count
camIndex = 0 # the index of last processed element in cam_ts and cam_count
start = 0 # the index of RP last time used as right

RPfoldername = []
folders = os.listdir()
for f in folders:
	if '._' not in f:
		if 'RP' in f and len(f) < 4:
			RPfoldername.append(f)
RPfoldername = sorted(RPfoldername)


Camerafoldername = []#'/home/team19/Desktop/Axis_DL/Detection/YOLO/zongxin_test/Camera 1/'
camLast = 0 # the idex of the file in the folders that was last used

cam_ts = [] # array that stores all the timestamp from camera
cam_count = np.array([]) # array that stores all the count from camera

camdict = [] # array of dictionaries stores timestamp and count for each cameras
camEnd = 0 # stores the min num of file in current camera folders
reportTime = 10 # the time when there is not new file form RP, do a median
report = False # bool for report

#getting the folder name of the latest trial
camerafolders = os.listdir('/home/team19/Desktop/Axis_DL/Detection/YOLO/')
datafolder = []
for f in camerafolders:
	if ':' in f:
		datafolder.append(f)
folderdict = {}
for i, f in enumerate(datafolder):
	print(f)
	datafolder[i] = f[6:10] + f[0:2] + f[3:5] + f[11:13] + f[14:16] + f[17:19]
	folderdict[datafolder[i]] = f
datafolder = sorted(datafolder, reverse=True)
print(datafolder)
Camerafoldername.append("/home/team19/Desktop/Axis_DL/Detection/YOLO/" + folderdict[datafolder[0]] +"/Camera 1/")
# Camerafoldername.append("/home/team19/Desktop/Axis_DL/Detection/YOLO/" + folderdict[datafolder[0]] +"/Camera 3/")


cam_intermediate_count = np.zeros(len(Camerafoldername)) # array stores count of individual cameras
roomnum = 0

# get input from commandline
try:
	opts, args = getopt.getopt(sys.argv[1:], "hN:MR:", ["H="])
except getopt.GetoptError:
	print("Error: modified_filter.py -N <reportTime>")
	sys.exit()

for opt, arg in opts:
	if opt == "-h":
		print('modified_filter.py -N <reportTime>')
		print("-M, for two cameras")
		sys.exit()
	elif opt in ("-N", "--infile"):
		reportTime = arg
	elif opt == "-M":
		Camerafoldername.append("/home/team19/Desktop/Axis_DL/Detection/YOLO/" + folderdict[datafolder[0]] +"/Camera 2/")
	elif opt in ("-R", "roomnum"):
		roomnum = int(arg)


with open("./room_information.json") as f:
	room = json.load(f)
sensornum = len(room[0]["thermal"])
if roomnum == 1:
	RPfoldername = RPfoldername[:sensornum]
else:
	RPfoldername = RPfoldername[sensornum:]
print(sensornum)
print(RPfoldername)
count = np.zeros(len(RPfoldername))

# initialize the dictionaries
for i in range(len(Camerafoldername)):
	camdict.append({})

for i in range(len(RPfoldername)):
	RPdict.append({})

# Access ip or other information from the devices
with open('./room_information.json') as f:
	room_information = json.load(f)

while 1:
	time.sleep(1)
	#iterate through the newest camera result, create dictionary for each timestamp, and append the new timestamp to the cam_ts
	ts_temp = []
	
	for i in range(len(Camerafoldername)):
		files = sorted(os.listdir(Camerafoldername[i]))
		jsonList = []
		for file in files:
			if '.json' in file:
				if not '._' in file:
					jsonList.append(file)
		camEnd = len(jsonList)
		print("file:", len(jsonList))
		for j in range(camLast, camEnd):
			ts_temp.append(float(jsonList[j][0:len(jsonList[j])-5]))
			# print("append", float(jsonList[j][0:len(jsonList[j])-5]))
			with open(Camerafoldername[i] + jsonList[j]) as f:
				temp = json.load(f)
				camdict[i][float(jsonList[j][0:len(jsonList[j])-5])] = temp["Num People"]
	print(len(ts_temp))
	camLast = camEnd
	ts_temp.sort()
	if len(ts_temp) != 0:
		cam_ts = cam_ts + ts_temp
	# print("cam_ts len", cam_ts)
	#after sorting the cam_ts, append each count to the cam_count in the order of cam_ts
	for i in range(len(ts_temp)):
		cam_intermediate_count = np.zeros(len(Camerafoldername)) 
		for j in range(len(Camerafoldername)):
			if ts_temp[i] in camdict[j]:	
				cam_intermediate_count[j] = camdict[j][ts_temp[i]]
				print(cam_intermediate_count[j], ts_temp[i])
		cam_count = np.append(cam_count, sum(cam_intermediate_count))
	print("cam_count", cam_count/len(Camerafoldername))
	#go through all the RP folder and decide which one has the most file and create a matrix that store all the RP information.
	for i in range(len(RPfoldername)):
		myfiles = np.array(os.listdir(RPfoldername[i]))
		myprocessedfile = []
		for j in range(len(myfiles)):
			if "._" not in myfiles[j]:
				myprocessedfile.append(myfiles[j])
		maxFileNum = max(maxFileNum, len(myprocessedfile))

	fileList = np.array(np.zeros(maxFileNum))
	for i in range(len(RPfoldername)):
		oneList = sorted(os.listdir(RPfoldername[i]))
		myprocessedfile = np.array([])
		for j in oneList:
			if "._" not in j:
				myprocessedfile = np.append(myprocessedfile, j)
		while len(myprocessedfile) < maxFileNum:
			myprocessedfile = np.append(myprocessedfile, 'placeHolder')
		# print(np.shape([fileList]))
		# print(np.shape([oneList]))
		fileList = np.vstack([fileList, myprocessedfile])
	#print(np.shape(fileList))
	#print(np.shape(fileList), maxFileNum)
	print(fileList)
	#creating dictionary for all the time stamp and add the count and time stamp to RP_count and RP_ts
	ts_temp = []
	for i in range(1, np.shape(fileList)[0]):
		for j in range(0, maxFileNum):
			if fileList[i][j] != 'placeHolder':
				with open(RPfoldername[i - 1] + '/' + fileList[i][j], encoding='utf-8') as f:
					temp = json.load(f)
				os.system('ssh ' + room_information[roomnum-1]["thermal"][i - 1]['thermal_ip'] + ' rm ./Buffer/' + fileList[i][j])
				ts_temp.append(float(temp['timestamp']))
				RPdict[i - 1][float(temp['timestamp'])] = int(temp['count'])
				#print(float(temp['timestamp']), int(temp['count']))
	
	
	ts_temp.sort()
	RP_ts = ts_temp
	RP_count = []
	for i in range(len(ts_temp)):
		for j in range(len(RPfoldername)):
			if ts_temp[i] in RPdict[j]:
				count[j] = RPdict[j][ts_temp[i]]
		RP_count.append(sum(count))

	#fusion
	if len(cam_ts) > 0:
		if (len(RP_ts) > RPIndex):
			window = cam_count[-short_window:]
			med = np.median(window)
			res_count = med
			res_ts = cam_ts[-1]
			cam_Index = len(cam_ts) - 1
			RPIndex = len(RP_ts)
		elif (len(cam_ts) - camIndex < short_window):
			window = cam_count[-short_window:]
			med = np.median(window)
			res_count = med
			res_ts = cam_ts[-1]
			# cam_Index = len(cam_ts) - 1
		elif (len(cam_ts) - camIndex < long_window):
			window = cam_count[camIndex:]
			med = np.median(window)
			res_count = med
			res_ts = cam_ts[-1]
		else:
			window = cam_count[-long_window:]
			med = np.median(window)
			res_count = med
			res_ts = cam_ts[-1]

	# report
		print("writing to result")
		result = {}
		result[str(res_ts)] = [str(res_count)]
		# print(cam_count)
		with open('result/' + str(res_ts) + '.json', 'w') as outfile:
			json.dump(result, outfile)





plt.plot(cam_ts, cam_count)
plt.title('filtered')
plt.show()
		








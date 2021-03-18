import os
import json
import matplotlib.pyplot as plt
import numpy as np
import datetime
import dateutil.relativedelta

with open("result.json", "r") as f:
	res = json.load(f)

fusion_ts = []
fusion_count = []
dt1 = datetime.datetime.fromtimestamp(1615468878.35857)
for data in res["info"]:
	for ts in data.keys():
		dt2 = datetime.datetime.fromtimestamp(float(ts))
		diff = dateutil.relativedelta.relativedelta(dt2, dt1)
		sec = diff.hours * 3600 + diff.minutes * 60 + diff.seconds
		fusion_ts.append(sec)
		fusion_count.append(float(data[ts]))
# plt.plot(fusion_ts, fusion_count)
# plt.savefig("fusion_count.png")

files = sorted(os.listdir('/home/team19/Desktop/Axis_DL/Detection/YOLO/zongxin_test/Camera 1/'))

jsonList = []
NUC_ts = []
NUC_count = []
for file in files:
	if '.json' in file:
		if not '._' in file:
			jsonList.append(file)
camEnd = len(jsonList)
# print("file:", len(jsonList))
for j in range(0, camEnd):
	dt2 = datetime.datetime.fromtimestamp(float(jsonList[j][0:len(jsonList[j])-5]))
	diff = dateutil.relativedelta.relativedelta(dt2, dt1)
	sec = diff.hours * 3600 + diff.minutes * 60 + diff.seconds
	NUC_ts.append(sec)
	# print("append", float(jsonList[j][0:len(jsonList[j])-5]))
	with open('/home/team19/Desktop/Axis_DL/Detection/YOLO/zongxin_test/Camera 1/' + jsonList[j]) as f:
		temp = json.load(f)
		NUC_count.append(temp[1][temp[1].find(':') + 1 : len(temp[1])])


RPfoldername = ["RP1", "RP2"]
RP_ts = []
RP_dict = []
RP1_ts = []
RP2_ts = []
RP1_count = []
RP2_count = []
count = np.zeros(len(RPfoldername))
for i in range(len(RPfoldername)):
	RP_dict.append({})

for i in range(len(RPfoldername)):
	myfiles = np.array(os.listdir(RPfoldername[i]))
	myfiles.sort()
	for j in range(len(myfiles)):
		if "._" not in myfiles[j]:
			with open(RPfoldername[i] + "/" + myfiles[j], encoding='utf-8') as f:
				temp = json.load(f)
				print(RPfoldername[i] + "/" + myfiles[j])
				RP_ts.append(float(temp['timestamp']))
				print(float(temp['timestamp']), int(temp['count']))
				RP_dict[i][float(temp['timestamp'])] = int(temp['count'])
				if i == 0:
					dt2 = datetime.datetime.fromtimestamp(float(temp['timestamp']))
					diff = dateutil.relativedelta.relativedelta(dt2, dt1)
					sec = diff.hours * 3600 + diff.minutes * 60 + diff.seconds
					RP1_ts.append(sec)
					RP1_count.append(int(temp['count']))
				else:
					dt2 = datetime.datetime.fromtimestamp(float(temp['timestamp']))
					diff = dateutil.relativedelta.relativedelta(dt2, dt1)
					sec = diff.hours * 3600 + diff.minutes * 60 + diff.seconds
					RP2_ts.append(sec)
					RP2_count.append(int(temp['count']))

RP_ts.sort()
RP_count = []

for i in range(len(RP_ts)):
	for j in range(len(RPfoldername)):
		if RP_ts[i] in RP_dict[j]:
			count[j] = RP_dict[j][RP_ts[i]]
	RP_count.append(sum(count))
RP_ts_g = []
RP_count_g = []
RP_ts_g.append(0)
RP_count_g.append(0)
for i in range(len(RP_ts)):
	dt2 = datetime.datetime.fromtimestamp(RP_ts[i])
	diff = dateutil.relativedelta.relativedelta(dt2, dt1)
	sec = diff.hours * 3600 + diff.minutes * 60 + diff.seconds
	# print(sec)
	if i !=0:
		RP_ts_g.append(sec)
		RP_count_g.append(RP_count[i-1])
	else:
		RP_ts_g.append(sec)
		RP_count_g.append(0)
	RP_ts_g.append(sec)
	RP_count_g.append(RP_count[i])

RP1_ts_g = []
RP1_count_g = []
RP1_ts_g.append(0)
RP1_count_g.append(0)
for i in range(len(RP1_ts)):
	if i !=0:
		RP1_ts_g.append(RP1_ts[i])
		RP1_count_g.append(RP1_count[i-1])
	else:
		RP1_ts_g.append(RP1_ts[i])
		RP1_count_g.append(0)
	RP1_ts_g.append(RP1_ts[i])
	RP1_count_g.append(RP1_count[i])

RP2_ts_g = []
RP2_count_g = []
RP2_ts_g.append(0)
RP2_count_g.append(0)
for i in range(len(RP2_ts)):
	if i !=0:
		RP2_ts_g.append(RP2_ts[i])
		RP2_count_g.append(RP2_count[i-1])
	else:
		RP2_ts_g.append(RP2_ts[i])
		RP2_count_g.append(0)
	RP2_ts_g.append(RP2_ts[i])
	RP2_count_g.append(RP2_count[i])

plt.figure()
plt.plot(NUC_ts, NUC_count, "b", label="NUC")
plt.plot(fusion_ts, fusion_count, "r", label="Fusion")
plt.xlim([0, 10000])
plt.ylim(-4, 11)
plt.title("Fusion and NUC")
plt.xlabel("Time (seconds)")
plt.ylabel("Number of people")
plt.legend()
plt.savefig("Fusion_NUC_count.png")

plt.figure()
plt.plot(fusion_ts, fusion_count, "b", label="Fusion")
plt.plot(RP_ts_g, RP_count_g, 'r', label="RP toal")
plt.xlim([0, 10000])
plt.ylim([-4, 11])
plt.title("Fusion and RP total")
plt.xlabel("Time (seconds)")
plt.ylabel("Number of people")
plt.legend()
plt.savefig("Fusion_RP_count.png")

# plt.figure()
# print(RP_count)
# plt.plot(RP_ts_g, RP_count_g)
# plt.xlim([0, 10000])
# plt.ylim([-4, 11])
# plt.title("RP total")
# plt.xlabel("Time (seconds)")
# plt.ylabel("Number of people")
# plt.savefig("RP_count.png")

plt.figure()
plt.plot(RP1_ts_g, RP1_count_g, "b", label="RP1")
plt.plot(RP2_ts_g, RP2_count_g, "r", label="RP2")
plt.xlim([0, 10000])
plt.ylim([-4, 11])
plt.title("RP1 and RP2")
plt.xlabel("Time (seconds)")
plt.ylabel("Number of people")
plt.legend()
plt.savefig("RP1_RP2_count.png")

# plt.figure()
# plt.plot(RP2_ts_g, RP2_count_g)
# plt.savefig("RP2_count.png")




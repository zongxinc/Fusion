import os

while(1):
	os.system("rsync -zaP pi@10.241.10.18:./Buffer/ ./RP1")
	os.system("rsync -zaP pi@10.241.10.17:./Buffer/ ./RP2")
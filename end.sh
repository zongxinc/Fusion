#!/bin/bash

ssh pi@10.241.10.32 "kill -9 \$(ps -aux | grep run.py | awk '{print \$2}')"&
ssh pi@10.241.10.31 "kill -9 \$(ps -aux | grep run.py | awk '{print \$2}')"&

kill -9 $(ps -aux | grep RP_sync.py | awk '{print $2}')
kill -9 $(ps -aux | grep modified_filter_twoCameras.py | awk '{print $2}')
kill -9 $(ps -aux | grep axis_cameras_single_cam.py | awk '{print $2}')

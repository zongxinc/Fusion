#!/bin/bash

ssh pi@10.241.10.18 "kill -9 \$(ps -aux | grep run.py | awk '{print \$2}')"&
ssh pi@10.241.10.17 "kill -9 \$(ps -aux | grep run.py | awk '{print \$2}')"&

kill -9 $(ps -aux | grep RP_sync.py | awk '{print $2}')
kill -9 $(ps -aux | grep modified_filter.py | awk '{print $2}')
kill -9 $(ps -aux | grep axis_cameras_v2.py | awk '{print $2}')

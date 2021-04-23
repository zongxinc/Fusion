#!/bin/bash

ssh pi@10.241.10.32 "kill -9 \$(ps -aux | grep run.py | awk '{print \$2}')"&
ssh pi@10.241.10.33 "kill -9 \$(ps -aux | grep run.py | awk '{print \$2}')"&

kill -9 $(ps -aux | grep RP_sync.py | awk '{print $2}')
kill -9 $(ps -aux | grep modified_filter_twoCameras.py | awk '{print $2}')
kill -9 $(ps -aux | grep axis_cameras_single_cam_v2_copy.py | awk '{print $2}')

# IP=''
# while getopts "p:" opt;
# do
#     case "${opt}" in
#             p) IP="${OPTARG}"
#                     ;;
#     esac
# done
# # echo "hi"
# echo ${IP}
# ssh ${IP} "kill -9 \$(ps -aux | grep run.py | awk '{print \$2}')"&
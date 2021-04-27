#!/bin/bash

# ssh pi@10.241.10.32 "kill -9 \$(ps -aux | grep run.py | awk '{print \$2}')"&
# ssh pi@10.241.10.33 "kill -9 \$(ps -aux | grep run.py | awk '{print \$2}')"&



room='python3 end.py'
myr=""
while getopts "R:" opt;
do
    case "${opt}" in
            R) room="${room} -R ${OPTARG}"
				myr="${OPTARG}"
                    ;;
    esac
done

if [[ ${myr} == "1" ]]
then
	echo "${myr}"
	kill -9 $(ps -aux | grep RP_sync.py | awk '{print $2}')
	kill -9 $(ps -aux | grep modified_filter_twoCameras.py | awk '{print $2}')
	kill -9 $(ps -aux | grep axis_cameras_single_cam_v2_copy.py | awk '{print $2}')
else
	echo "${myr} hi"
	kill -9 $(ps -aux | grep RP_sync_room2.py | awk '{print $2}')
	kill -9 $(ps -aux | grep modified_filter_twoCameras_room2.py | awk '{print $2}')
	kill -9 $(ps -aux | grep axis_cameras_single_cam_v2_copy_room2.py | awk '{print $2}')
fi

echo "hi"
echo ${room}
eval "${room}"
# ssh ${IP} "kill -9 \$(ps -aux | grep run.py | awk '{print \$2}')"&
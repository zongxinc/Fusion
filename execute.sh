#!/bin/bash

NUC="python3 axis_cameras_single_cam.py"
RP="python3 rpi-realtime-peoplecount/run.py"
Fusion="python3 modified_filter_twoCameras.py"
now=$(date +"%m-%d-%Y-%T")
while getopts "N:CSOImsf" opt;
do
    case "${opt}" in
            N) Fusion="${Fusion} -N ${OPTARG}"
                    ;;
            C) NUC="${NUC} -c"
                    ;;
            S) NUC="${NUC} -s"
                    ;;
            O) NUC="${NUC} -o ${now}/"
                    ;;
            I) NUC="${NUC} -i"
                    ;;
            m) RP="${RP} -m"
                    ;;
            s) RP="${RP} -s"
                    ;;
            f) RP="${RP} -f ${now}/"
    esac
done
echo "${NUC}"
echo "${RP}"
echo "${Fusion}"
cd
cd Desktop
. /home/team19/Desktop/ENV/bin/activate
cd Axis_DL/Detection/YOLO
mkdir "${now}"
cd "${now}"
mkdir "Camera 1"
mkdir "Camera 2"
mkdir "Camera 3"
cd ..
ls
eval "${NUC}" >running_stdout.txt&
cd 
cd Fusion
ssh pi@10.241.10.31 "${RP}"&
ssh pi@10.241.10.32 "${RP}"&
python3 RP_sync.py >autoSync.txt&
eval "${Fusion}">filter.txt&

#!/bin/bash

NUC="python3 axis_cameras_single_cam_v2_copy.py"
RP="python3_rpi-realtime-peoplecount/run.py"
Fusion="python3 modified_filter_twoCameras.py"
now=$(date +"%m-%d-%Y-%T")
while getopts "N:MCSOA:B:Imsf" opt;
do
    case "${opt}" in
            N) Fusion="${Fusion} -N ${OPTARG}"
                    ;;
            M) Fusion="${Fusion} -M"
                    ;;
            C) NUC="${NUC} -c"
                    ;;
            S) NUC="${NUC} -s"
                    ;;
            O) NUC="${NUC} -o ${now}/"
                    ;;
            I) NUC="${NUC} -i"
                    ;;
            A) NUC="${NUC} -a http://viewer:OPC-ECE-viewer@${OPTARG}//axis-cgi/mjpg/video.cgi"
                    ;;
            B) NUC="${NUC} -b http://viewer:OPC-ECE-viewer@${OPTARG}//axis-cgi/mjpg/video.cgi"
                    ;;
            m) RP="${RP}_-m"
                    ;;
            s) RP="${RP}_-s"
                    ;;
            f) RP="${RP}_-f_${now}/"
    esac
done
echo "${NUC}"
echo "${RP}"
echo "${Fusion}"
cd result
rm *.json
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
eval "python3 executeRP.py -p ${RP}"&
# ssh pi@10.241.10.17 "${RP}"&
# ssh pi@10.241.10.32 "${RP}"&
python3 RP_sync.py >autoSync.txt&
eval "${Fusion}">filter.txt&

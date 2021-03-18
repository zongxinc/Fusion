#!/bin/bash

NUC="python3 axis_cameras_v2.py"
RP="python3 rpi-realtime-peoplecount/run.py"
Fusion="python3 modified_filter.py"
while getopts "N:CSO:Im" opt;
do
    case "${opt}" in
            N) Fusion="${Fusion} -N ${OPTARG}"
                    ;;
            C) NUC="${NUC} -c"
                    ;;
            S) NUC="${NUC} -s"
                    ;;
            O) NUC="${NUC} -o ${OPTARG}"
                    ;;
            I) NUC="${NUC} -i"
                    ;;
            m) RP="${RP} -m"
    esac
done

echo "${NUC}"
echo "${RP}"
echo "${Fusion}"
cd
cd Desktop
. /home/team19/Desktop/ENV/bin/activate
cd Axis_DL/Detection/YOLO
ls
eval "${NUC}" >running_stdout.txt&
cd 
cd Fusion
ssh pi@10.241.10.18 "${RP}"&
ssh pi@10.241.10.17 "${RP}"&
python3 RP_sync.py >autoSync.txt&
python3 modified_filter.py>filter.txt&

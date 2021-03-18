# Fusion



## To start

use ```bash execute [flgs] &```to start. Please remember to add "&". Example:

```bash
bash execute.sh -N 5 -C -S -O ./ -I -m &
```
Capital letters are flags for the cameras or Fusion (-N is the only flag for the fusion):
 - `-N [insert number here]` will specify the report time in minute (system will report if there is new thermal entry, if there is no thhermal entry for a long time, how long do you want it to report)
  - `-C` will set it to run analysis from images taken from the camera
  - `-S` will set it to save images
  - `-O [insert folder name here]` will set it to save images to a particular folder. Default is `./PICS/detections`
  - `-I` will read images in from a folder should you need to anaylze them as such

Lower case letters are for the thermal sensors:
 -  -h, --help     show this help message and exit
 - -f save_path   Folder to save resulting JSON files. Must be a subdirectory of the current path. Saved to sensor_results by default
 - -n [duration]  Time to run the sensor in seconds (approximated using number of frames). For indefinite runtime, omit flag.
 - -m             Enable saving thermal frame data to JSON files.
 - -s             Enable Single-Person/Baseline algorithm.

## To End

To stop the program press enter and use:

```bash
sh end.sh
```

## Note
- I redirected the output from the camera to a file ```running_stdout.txt``` located at the same place where the camera's people counting program is on so that the constant output from the camera does not obstruct further operation.
- I also redirected the output from the Rsync to ```autoSync.txt``` located in the current directory.
- JSON files from the thermal sensor is located in folders call RP#
- Results are store in ```result.json```

## 


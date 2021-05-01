# Fusion



## To start

use ```bash execute [flgs] &```to start. Please remember to add "&". Example:

Capital letters are flags for the cameras or Fusion (-N is the only flag for the fusion):
  - `-C` will set it to run analysis from images taken from the camera
  - `-S` will set it to save images
  - `-O` will set it to save images to a folder named after current time. 
  - `-I` will read images in from a folder should you need to anaylze them as such
  - `-M` used when there are two cameras in one room
  - `-m` is to enable saving thermal frame data in the json files.
  - `-s` is to enable single-person/baseline algorithm instead of the multiperson algorithm. For the multiperson algorithm, omit flag. 
  - `-R [room number]` it will tell the system to look at which room's information. To decide which room the COSSY is going to run

eg: to run room 1 which has 2 cameras
```bash
bash execute.sh -C -S -O -M -I -m -s -f -R 1&
```
eg: to run room 2 which has 1 cameras
```bash
bash execute.sh -C -S -O -I -m -s -f -R 2&
```

## To End

To stop the program press enter and use:
eg: end the system in room 1
```bash
bash end.sh -R 1
```
- `-R [room number]` it will tell the system to end the system at which room

## Note
- I redirected the output from the camera to a file ```running_stdout.txt``` located at the same place where the camera's people counting program is on so that the constant output from the camera does not obstruct further operation.
- I also redirected the output from the Rsync to ```autoSync.txt``` located in the current directory.
- JSON files from the thermal sensor is located in folders call RP#
- Results are store in ```result.json``` or ```result2.json```


## 


# openCV-carDetect
A lightweight computer vision application made to detect cars.

# Prerequisites 
## Libraries
In python command line, pass in these commands: *(assuming you have pip installed)* 
1. pip install urllib3
2. pip install opencv-python
3. pip install numpy

## IPWebcam
For the program to work, you need a app named IPWebcam. It can be downloaded on IOS and Android
- IPWebcam allows the application to obtain image input, which can then be processed by opencv.
- When you have IPWebcam downloaded, open it and start a server. Keep it open as we will need it later.

# How to use
## Passing in args
1. Download the files from this repository into a folder.
2. Whilst in the folder, type cmd into the file explorer. This will open cmd to the path of our folder.
3. After cmd is open, go back into IPWebcam and save the IPv4 address of the server (only numbers and port.)
4. In cmd, type in: *carDetect.py 192.168.0.1:8080* (change the numbers to your IPWebcam address.)
5. Python should then open a window of the live camera feed from your phone. Point at car to test detection.
6. Look back onto computer screen to see output.
7. Profit!

# Todo
- Make a better cascade
- Change multiscale, extremely hard to get correct amount of layers and K neighbors.







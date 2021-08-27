<h1 align="center">Flask Camera Stream</h1>
<p align="center">
Access your PC's or Raspberry Pi's camera from any device that's connected to the same LAN/WiFi network through a web 
interface, with OpenCV and Flask.
</p>

## Dependencies

This program is based on :
* [OpenCV](https://github.com/pytube/pytube) (Accessing the camera and encoding the stream frames)
* [Flask](https://github.com/kkroening/ffmpeg-python) (Handling the web requests)

You can install these dependencies using this command :
```Bash
pip3 install -U Flask opencv-python
```

## Getting Started
The camera's index is 0 by default, if you have multiple cameras connected to the same computer you may have to change 
it to the desired camera's index by going to the `main.py` file and editing this line `index = 0`.

## Usage
1. Run the code, and wait for the host's IP address to appear (e.g. 192.168.1.7:8000).
2. Go to any browser in any device that's connected to the same network.
3. Go to the host's IP address.
4. Wait for the camera feed.

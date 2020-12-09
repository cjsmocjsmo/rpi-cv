#!/bin/sh

cd /home/pi/;
python3 -m venv cv --system-site-packages;
cd cv;
source ./bin/activate;
pip3 install opencv-contrib-python==4.1.0.25 imutils imageZMQ numpy picamera["array"];
deactivate;
cd
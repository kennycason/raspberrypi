# Robotics


### 4" MiuZei Touch Display

Miuzei Raspberry Pi 4 Touchscreen with Case Fan, 4 inch IPS Touch Screen LCD Display, 800x480 HDMI Monitor for RPI 4b 8gb/4gb/2gb with Touch Pen (Support Raspbian/Kali/Octopi/Ubuntu)
https://www.amazon.com/Miuzei-Raspberry-Full-Angle-Heatsinks-Raspbian/dp/B07XBVF1C9

#### Installation
`scripts/pi_4in_display_setup.sh`

#### Configuration
http://wiki.sunfounder.cc/index.php?title=Adjust_Resolution_for_Raspberry_Pi

```
hdmi_cvt=<width> <height> <framerate> <aspect> <margins> <interlace>
Value	Default	Default
width	(required)	width in pixels
height	(required)	height in pixels
framerate	(required)	framerate in Hz
aspect	3	aspect ratio 1=4:3, 2=14:9, 3=16:9, 4=5:4, 5=16:10, 6=15:9
margins	0	0=margins disabled, 1=margins enabled
interlace	0	0=progressive, 1=interlaced
rb	0	0=normal, 1=reduced blanking
```


#### Copy project to Pi

```bash
rsync -azvh robotics spider.local:~/ --exclude venv/
```

#### Venv Setup
```bash
pip install virtualenv
virtualenv -p python3.9.15 venv
source venv/bin/activate
```


#### Stream Video over TCP

Server (spider.local)
```bash
libcamera-vid -t 0  -q 100 --framerate 3 -n --codec mjpeg --inline --listen -o tcp://192.168.4.76:8888 -v
```

Client (VLC -> Open Network)
```bash
tcp/mjpeg://192.168.4.76:8888
```

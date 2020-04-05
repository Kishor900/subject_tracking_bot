# Subject Tracking Bot
This is a computer vision project where a vehicle with robotics part follows a subject

There are two parts of this project

1. Robotics
2. Computer Vision

# Robotics
Components Required
1. Node MCU
2. Geared dc motor 100 rpm each x 4
3. L298N Motor Driver
4. 6-9v battery
5. An android or ios phone with a camera
6. Bread Board small
7. Jumpers


You need to connect the node mcu with L2989 as follows 
ENA-> D4
ENB-> D14
INT1-> D5
INT2-> D0
INT3-> D2
INT4-> D12

Above are GPIO pins of the NODEMCU, you need to connect the pins as per the pin numbering. But the code should be exactly as above. L298N power pins go to the battery and 5v output of L298N goes to NODEMCU vin and gnd.


Once the connection is established. Connect the Node MCU to the computer. Open Arduino IDE, open blynk-wifi from examples, change the API key, SSID and password. Upload the code.
Note: Full blynk setup can be found here http://help.blynk.cc/en/articles/633736-nodemcu


Once Blynk is setup then open the Firmware/Firmware.INO from source code provided and upload the code to the NodeMCU
Open blynk app and set D7 D8 D9 as left, right and forward buttons 

You should have these APIs already set by blynk 

http://188.166.206.43/api_key/update/D13?value=0 forward off
http://188.166.206.43/api_key/update/D13?value=1 forward on
http://188.166.206.43/api_key/update/D14?value=0 left off
http://188.166.206.43/api_key/update/D14?value=1 left on
http://188.166.206.43/api_key/update/D3?value=0 right off
http://188.166.206.43/api_key/update/D3?value=1 right on

# Computer Vision

To execute this part, you need to have an app installed on the onboard Mobile Phone  https://play.google.com/store/apps/details?id=com.pas.webcam&hl=en_IN


Then upload the OpenCV code from the OpenCV folder above provided.
Finally, run the test.py file

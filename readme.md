# Smart Switchboard
### Smart switchboard solves a unique problem. Usually smart devices require you to keep the switch on, making the switchboard useless. This smart switchboard solves that problem by making the switches smart directly.

<p align="center">
  <img src="./Assets/complete.png" alt="Smart Switchboard" width="400">
</p>

# Features
 - This uses an ESP32 to control relays connected with my lights and a socket. I have a smart fan and the ESP32 will use its API to control the smart fan. 
 - It has 4 push buttons and a rotary encoder switch with RGB LEDs to control the devices.
 - The Led lights are placed flushed into the surface of the board. They reflect the light from the switch back to the surface giving a cool futuristic glow effect!

# Quick Start
To replicate this project, you would want to follow these steps - 
 - Clone the repo and get the production files & firmware files
 - Get the model 3d printed from the .stl files
 - Take a look at the BOM and arrange the parts
 - Refer to the schematic folder and wire up the parts. (You have to have some soldering knowledge) **Be careful when handling wires from mains!**
 - Assemble all the components with non-conductive glue for electronics in the 3D printed model.
 - Enter your wifi credentials in the firmware.
 - Flash the firmware via micropico in the ESP32. 
 - Finally visit your ESP's local IP to access the control panel!

# Schematic
Here is the schematic. 

<p align="center">
  <img src="./Assets/Schematic.png" alt="Schematic" width="600">
</p>

All the parts should be soldered directly since the microcontroller is to be kept a bit far away from the live AC current wires so that it works the best. Since the circuit is very simple and all the parts are supposed to be spaced out, a PCB is not required and the parts will be soldered directly.

# CAD model
 - This is the model to be 3D printed. It has holes to place the push buttons, LEDs and the rotary encoder switch

<p align="center">
  <img src="./Assets/base.png" alt="CAD" width="400">
</p>

 - It also has space to stick a socket in the back. 

<p align="center">
  <img src="./Assets/socket.png" alt="Socket" width="400">
</p>

 - I measured everything like the screw holes, socket size and the borders with my existing switchboard to ensure everything fits in place

<p align="center">
  <img src="./Assets/screws.png" alt="Smart Switchboard" width="400">
</p>

# Firmware
 - The firmware launches a webserver to control all the devices including 3 lights, a socket and a fan. 

<p align="center">
  <img src="./Assets/webserver.png" alt="Websever" width="400">
</p>

 - I have a smart fan with a remote. I also have a IR blaster which I will use to control the fan. The code to control the fan via the IR blaster's API will not be pushed to github for obvious reasons. I dont want people around the world to control my fan. 

 - The firmware is made such that you could seamlessly switch the control between controlling from webserver or with physical buttons. The lights will also update in the switchboard as you change status of any device

 - The firmware right now is not the best or perfect since I have no way to run the code and check if it works. I will test it properly once I actually get my hands on the hardware.

# BOM
 - 1x  3D printed base
 - 1x  ESP32
 - 1x  Rotary Encoder Switch
 - 1x  5V 2A Power Supply
 - 4x  Push buttons
 - 4x  5V 30A Relays
 - 15x WS2812B RGB LEDs
 
For testing out stuff - 
 - 1x  Breadboard
 - 40x jumper wires

# Credits 
## Knob Model - [Jack](https://www.printables.com/model/243409-crown-knob/files)

## Basic setup instructions for adding ToDoist to a 4.2inch Waveshare E-paper display

Setup a raspberry Pi. I have used a Pi zero, 3B+ and a Pi 400 with no issues. If you just want to run the code over SSH then use Pi OS Lite. If you want to edit and experiment with the code then it might be easier to use full Raspberry Pi OS.

Next install updates,
`sudo apt update && sudo apt upgrade -y`

Install ToDoIst API python package
`sudo pip install todoist-api-python`

Ensure you have SPI enabled in your Pi's interfacing options. If using full Raspberry Pi OS then this can be done by going into Raspberry Pi Configuration from the drop down menu. If using the terminal just type,
`sudo raspi-config`

Download the folder in my github projects repository called Eink ToDoIst.

Open the folder titled main.py and insert your API token from ToDoIst. 

Connect the Eink display to the Pi using the images below.

![Raspberry Pi GPIO Pins](https://cdn.sparkfun.com/assets/learn_tutorials/1/5/9/5/GPIO.png)
Ref: https://learn.sparkfun.com/tutorials/introduction-to-the-raspberry-pi-gpio-and-physical-computing/gpio-pins-overview

[Waveshare Wiki](https://www.waveshare.com/wiki/4.2inch_e-Paper_Module_Manual#Users_Guides_of_Raspberry_Pi)


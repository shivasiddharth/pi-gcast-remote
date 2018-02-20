# pi-gcast-remote
## DIY Remote control for Google Cast Devices using Raspberry Pi Zero and Pimoroni Button SHIM
************************************************************************************************************  

<a href="http://www.youtube.com/watch?feature=player_embedded&v=cYcNOCwakKM
" target="_blank"><img src="http://img.youtube.com/vi/cYcNOCwakKM/0.jpg"
alt="Detailed Youtube Video" width="240" height="180" border="10" /></a>


#### Step-1 - Install drivers for Button SHIM using:
````  
sudo curl https://get.pimoroni.com/buttonshim | bash  
```` 

#### Step-2 - Install dependencies using:  
````  
sudo apt-get install git  
sudo pip3 install pychromecast  
````  

#### Step-3 - Clone the project using:  
````  
cd /home/pi/  
sudo git clone https://github.com/shivasiddharth/pi-gcast-remote  
````  

#### Step-4 - Declare your Google Cast devices in the g-cast-controller.py script  
````
#Enter the IP Addresses of your Google Cast devices   
chromecasts_ip=['192.168.1.4','192.168.1.13']   
   
#Enter the names of the Google Cast devices as in the Google App  
chromecasts_name=['Living Room Speaker','Living Room TV']  
````  

#### Step-5 - Setup the script to start on boot using:   
````
sudo chmod +x /home/pi/pi-gcast-remote/scripts/service-installer.sh  
sudo /home/pi/pi-gcast-remote/scripts/service-installer.sh  
````  

#### Step-6 - Enable the service to start on boot:   
````
sudo systemctl enable gcastremote.service   
````  

**To switch between the devices, press and hold the A button/key.**  


#### Note: **[pychromecast](https://github.com/balloob/pychromecast)** API takes time to get the list of active devices, hence continuous device status monitoring has not been added as it would cause delays to get a response from a device on button press. So the remote control program should be started after making sure that your devices are online.  

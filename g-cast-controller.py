#!/usr/bin/env python

import signal
import buttonshim
import time
import pychromecast

#The IP Address should match the device name or they must be in the same order

#Enter the IP Addresses of your Google Cast devices
chromecasts_ip=['192.168.1.4','192.168.1.13']

#Enter the names of the Google Cast devices as in the Google App
chromecasts_name=['Living Room Speaker','Living Room TV']


devices=pychromecast.get_chromecasts()
print("""
Press the buttons once to control first cast device, press and hold the buttons to control the second cast device.
Press Ctrl+C to exit.

If you want to control more than one device, press and hold A button to switch between devices.

A="Pause"
B="Play"
C="Stop"
D="Volume Down"
E="Volume Up"

""")
selecteddevice=0
while True:
  if devices==[]:
     print("No Device Online")
  elif not devices==[]:
     if len(devices)==len(chromecasts_name):
        buttonshim.set_pixel(0x94, 0x00, 0xd3)
        @buttonshim.on_hold(buttonshim.BUTTON_A, hold_time=2)
        def button_a(button):
           global selecteddevice
           selecteddevice^=1
           print("Value Changed")
        @buttonshim.on_press(buttonshim.BUTTON_A)
        def button_a(button, pressed):
           cast=pychromecast.Chromecast(chromecasts_ip[selecteddevice])
           mc = cast.media_controller
           cast.wait()
           time.sleep(1)
           mc.pause()
        @buttonshim.on_press(buttonshim.BUTTON_B)
        def button_b(button, pressed):
           cast=pychromecast.Chromecast(chromecasts_ip[selecteddevice])
           mc = cast.media_controller
           cast.wait()
           time.sleep(1)
           mc.play()
        @buttonshim.on_press(buttonshim.BUTTON_C)
        def button_c(button, pressed):
           cast=pychromecast.Chromecast(chromecasts_ip[selecteddevice])
           mc = cast.media_controller
           cast.wait()
           time.sleep(1)
           mc.stop()
        @buttonshim.on_press(buttonshim.BUTTON_D)
        def button_d(button, pressed):
           cast=pychromecast.Chromecast(chromecasts_ip[selecteddevice])
           cast.wait()
           time.sleep(1)
           cast.volume_down(0.1)
        @buttonshim.on_press(buttonshim.BUTTON_E)
        def button_e(button, pressed):
           cast=pychromecast.Chromecast(chromecasts_ip[selecteddevice])
           cast.wait()
           time.sleep(1)
           cast.volume_up(0.1)
     elif len(devices)<len(chromecasts_name):
        if devices[0].device.friendly_name==chromecasts_name[0]:
           buttonshim.set_pixel(0x00, 0x00, 0xff)
           @buttonshim.on_press(buttonshim.BUTTON_A)
           def button_a(button, pressed):
               cast=pychromecast.Chromecast(chromecasts_ip[0])
               mc = cast.media_controller
               cast.wait()
               time.sleep(1)
               mc.pause()
           @buttonshim.on_press(buttonshim.BUTTON_B)
           def button_b(button, pressed):
               cast=pychromecast.Chromecast(chromecasts_ip[0])
               mc = cast.media_controller
               cast.wait()
               time.sleep(1)
               mc.play()
           @buttonshim.on_press(buttonshim.BUTTON_C)
           def button_c(button, pressed):
               cast=pychromecast.Chromecast(chromecasts_ip[0])
               mc = cast.media_controller
               cast.wait()
               time.sleep(1)
               mc.stop()
           @buttonshim.on_press(buttonshim.BUTTON_D)
           def button_d(button, pressed):
               cast=pychromecast.Chromecast(chromecasts_ip[0])
               cast.wait()
               time.sleep(1)
               cast.volume_down(0.1)
           @buttonshim.on_press(buttonshim.BUTTON_E)
           def button_e(button, pressed):
               cast=pychromecast.Chromecast(chromecasts_ip[0])
               cast.wait()
               time.sleep(1)
               cast.volume_up(0.1)
        elif devices[0].device.friendly_name==chromecasts_name[1]:
           buttonshim.set_pixel(0x00, 0xff, 0x00)
           @buttonshim.on_press(buttonshim.BUTTON_A)
           def button_a(button, pressed):
               cast=pychromecast.Chromecast(chromecasts_ip[1])
               mc = cast.media_controller
               cast.wait()
               time.sleep(1)
               mc.pause()
           @buttonshim.on_press(buttonshim.BUTTON_B)
           def button_b(button, pressed):
               cast=pychromecast.Chromecast(chromecasts_ip[1])
               mc = cast.media_controller
               cast.wait()
               time.sleep(1)
               mc.play()
           @buttonshim.on_press(buttonshim.BUTTON_C)
           def button_c(button, pressed):
               cast=pychromecast.Chromecast(chromecasts_ip[1])
               mc = cast.media_controller
               cast.wait()
               time.sleep(1)
               mc.stop()
           @buttonshim.on_press(buttonshim.BUTTON_D)
           def button_d(button, pressed):
               cast=pychromecast.Chromecast(chromecasts_ip[1])
               cast.wait()
               time.sleep(1)
               cast.volume_down(0.1)
           @buttonshim.on_press(buttonshim.BUTTON_E)
           def button_e(button, pressed):
               cast=pychromecast.Chromecast(chromecasts_ip[1])
               cast.wait()
               time.sleep(1)
               cast.volume_up(0.1)


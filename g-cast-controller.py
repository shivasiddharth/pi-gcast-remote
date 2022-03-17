#!/usr/bin/python

import signal
import buttonshim
import time
import pychromecast

#Enter the names of the Google Cast devices as in the Google App
chromecasts_name=['Living Room Speaker','Living Room TV']

print("Discovering connected Chromecasts")
devices, browser = pychromecast.get_chromecasts()

selecteddevice=0
cc = []
for device in devices:
  print("Found:",device.cast_info.friendly_name,"at",device.cast_info.host)
  for chromecast_name in chromecasts_name:
    if device.cast_info.friendly_name == chromecast_name:
       cc.append(device)

print("""
Press the buttons to control first cast device, press and hold the buttons to control the second cast device.
Press Ctrl+C to exit.

A = "Pause"
B = "Play"
C = "Stop"
D = "Volume Down"
E = "Volume Up"

""")

while True:
  if devices==[]:
     print("No Device Online")
     time.sleep(5)
  elif not devices==[]:

    if len(cc) > 1:
      @buttonshim.on_press(None)
      def button_press(button, state):
        # assume any button press is a short press... (device #1)
        buttonshim.set_pixel(0x00, 0x00, 0x00)
        global selecteddevice
        selecteddevice=0

      @buttonshim.on_hold(None)
      def button_hold(button, hold_time=1):
        # ...but then long press on any button = device #2
        # flash the led green to indicate the button's been held long enough
        buttonshim.set_pixel(0x00, 0xFF, 0x00)
        print(buttonshim.NAMES[button],'long pressed')
        global selecteddevice
        selecteddevice=1
        print("Target device",cc[selecteddevice].cast_info.friendly_name)
        # turn off the led
        buttonshim.set_pixel(0x00, 0x00, 0x00)

    @buttonshim.on_release(buttonshim.BUTTON_A)
    def button_a(button, pressed):
       #print('A pressed')
       buttonshim.set_pixel(0xFF, 0xEE, 0x00)
       cast=cc[selecteddevice]
       mc=cast.media_controller
       cast.wait()
       time.sleep(1)
       mc.pause()
       #buttonshim.set_pixel(0x00, 0x00, 0x00)

    @buttonshim.on_release(buttonshim.BUTTON_B)
    def button_b(button, pressed):
       #print('B pressed')
       buttonshim.set_pixel(0x00, 0xFF, 0x00)
       cast=cc[selecteddevice]
       mc=cast.media_controller
       cast.wait()
       time.sleep(1)
       mc.play()
       buttonshim.set_pixel(0x00, 0x00, 0x00)

    @buttonshim.on_release(buttonshim.BUTTON_C)
    def button_c(button, pressed):
       #print('C pressed')
       buttonshim.set_pixel(0xFF, 0x00, 0x00)
       cast=cc[selecteddevice]
       mc=cast.media_controller
       cast.wait()
       time.sleep(1)
       mc.stop()
       buttonshim.set_pixel(0x00, 0x00, 0x00)

    @buttonshim.on_release(buttonshim.BUTTON_D)
    def button_d(button, pressed):
       #print('D pressed')
       buttonshim.set_pixel(0xFF, 0x80, 0xFF)
       cast=cc[selecteddevice]
       cast.wait()
       time.sleep(1)
       cast.volume_down(0.1)
       buttonshim.set_pixel(0x00, 0x00, 0x00)

    @buttonshim.on_release(buttonshim.BUTTON_E)
    def button_e(button, pressed):
       #print('E pressed')
       buttonshim.set_pixel(0xFF, 0x80, 0xFF)
       cast=cc[selecteddevice]
       cast.wait()
       time.sleep(1)
       cast.volume_up(0.1)
       buttonshim.set_pixel(0x00, 0x00, 0x00)


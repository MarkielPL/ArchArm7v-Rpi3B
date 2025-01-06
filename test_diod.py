#!/usr/bin/env python
#-*- coding:utf-8 -*-

from gpiozero import LED
from time import sleep

# Przypisanie pinów GPIO do diod
blue = LED(20)
green = LED(21)
red = LED(26)

# Funkcja testowa dla diod
def test_leds():
    for led in [blue, green, red]:
        print(f"Testing LED on GPIO {led.pin}")
        led.on()
        sleep(1)  # Diody w³¹czone przez 1 sekundê
        led.off()
        sleep(1)

test_leds()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import Adafruit_DHT
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)  # Ustaw tryb BCM dla zgodności z gpiozero
GPIO.setup(21, GPIO.OUT)  # Ustawienie pinu 19 jako zasilanie (+) dla DHT11
GPIO.output(21, GPIO.HIGH)  # Włączenie zasilania dla DHT11

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 26

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print(f"Temperatura: {temperature:.1f}°C, Wilgotność: {humidity:.1f}%")
    else:
        print("[Błąd] Nie udało się odczytać danych z czujnika!")
    time.sleep(2)

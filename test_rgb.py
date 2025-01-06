#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO

# Definicje pinów GPIO
RED_PIN = 13
GREEN_PIN = 16
BLUE_PIN = 19
ANODE_PIN = 20

# Inicjalizacja GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

# Konfiguracja pinów dla diody RGB
GPIO.setup(RED_PIN, GPIO.OUT)
GPIO.setup(GREEN_PIN, GPIO.OUT)
GPIO.setup(BLUE_PIN, GPIO.OUT)
GPIO.setup(ANODE_PIN, GPIO.OUT)

# Ustawienie anody na HIGH (zasilanie diody RGB)
GPIO.output(ANODE_PIN, GPIO.HIGH)

# Funkcja zerowania diody RGB
def zeruj_kolory():
    GPIO.output(RED_PIN, GPIO.HIGH)
    GPIO.output(GREEN_PIN, GPIO.HIGH)
    GPIO.output(BLUE_PIN, GPIO.HIGH)

try:
    zeruj_kolory()
    print("[Test] Wszystkie kolory wyłączone.")

    # Testowanie czerwonej diody
    print("[Test] Zapalanie czerwonej diody.")
    GPIO.output(RED_PIN, GPIO.LOW)
    time.sleep(2)
    zeruj_kolory()

    # Testowanie zielonej diody
    print("[Test] Zapalanie zielonej diody.")
    GPIO.output(GREEN_PIN, GPIO.LOW)
    time.sleep(2)
    zeruj_kolory()

    # Testowanie niebieskiej diody
    print("[Test] Zapalanie niebieskiej diody.")
    GPIO.output(BLUE_PIN, GPIO.LOW)
    time.sleep(2)
    zeruj_kolory()

    print("[Test] Wszystkie kolory wyłączone.")
finally:
    GPIO.cleanup()
    print("[Test] GPIO cleanup wykonany.")

import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import threading

# Konfiguracja pinów GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # Ustawienie trybu BCM dla pinów GPIO
PIN_DHT11 = 26  # Pin danych dla czujnika DHT11
PIN_RGB_RED = 13
PIN_RGB_GREEN = 16
PIN_RGB_BLUE = 19
PIN_RGB_ANODE = 20
PIN_DHT11_POWER = 21

# Inicjalizacja GPIO dla czujnika i diody RGB
GPIO.setup(PIN_RGB_RED, GPIO.OUT)
GPIO.setup(PIN_RGB_GREEN, GPIO.OUT)
GPIO.setup(PIN_RGB_BLUE, GPIO.OUT)
GPIO.setup(PIN_RGB_ANODE, GPIO.OUT)
GPIO.setup(PIN_DHT11_POWER, GPIO.OUT)

GPIO.output(PIN_RGB_ANODE, GPIO.HIGH)  # Włączenie wspólnej anody dla RGB
GPIO.output(PIN_DHT11_POWER, GPIO.HIGH)  # Zasilanie czujnika DHT11

# Konfiguracja PWM dla diod RGB
pwm_red = GPIO.PWM(PIN_RGB_RED, 100)  # 100 Hz
pwm_green = GPIO.PWM(PIN_RGB_GREEN, 100)
pwm_blue = GPIO.PWM(PIN_RGB_BLUE, 100)

# Rozpoczęcie PWM z zerowym wypełnieniem
pwm_red.start(0)
pwm_green.start(0)
pwm_blue.start(0)

# Funkcja zerująca wszystkie kolory RGB (wyłącza diodę)
def zeruj_kolory():
    pwm_red.ChangeDutyCycle(0)
    pwm_green.ChangeDutyCycle(0)
    pwm_blue.ChangeDutyCycle(0)

# Efekt płynnego przejścia kolorów (ładowanie)
def efekt_ladowania():
    print("Uruchamianie programu... Efekt ładowania RGB.")
    zeruj_kolory()  # Wyłączenie wszystkich kolorów przed efektem

    try:
        for i in range(0, 101):  # Jasność narasta (od 0% do 100%)
            pwm_red.ChangeDutyCycle(i)
            pwm_green.ChangeDutyCycle(i // 2)  # Zielony wolniej narasta
            pwm_blue.ChangeDutyCycle(100 - i)  # Niebieski maleje
            time.sleep(0.02)  # Czas między zmianami jasności

        for i in range(100, -1, -1):  # Jasność maleje (od 100% do 0%)
            pwm_red.ChangeDutyCycle(i)
            pwm_green.ChangeDutyCycle(i // 2)  # Zielony wolniej maleje
            pwm_blue.ChangeDutyCycle(100 - i)  # Niebieski narasta
            time.sleep(0.02)

        zeruj_kolory()  # Wyłączenie wszystkich kolorów na końcu efektu
        print("Efekt ładowania zakończony.")
    except KeyboardInterrupt:
        zeruj_kolory()

# Flaga i zmienne globalne
flaga_koniec = False
wynik = None
lock = threading.Lock()

# Funkcja odczytu z DHT11 w osobnym wątku
def odczyt_dht11():
    global wynik, flaga_koniec
    print("Uruchamianie odczytu z czujnika DHT11...")
    while not flaga_koniec:
        wilgotnosc, temperatura = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, PIN_DHT11)
        with lock:
            if wilgotnosc is not None and temperatura is not None:
                wynik = (temperatura, wilgotnosc)
            else:
                wynik = None
        time.sleep(60)  # Odczyt co minutę

# Funkcja sterująca diodą RGB na podstawie danych z DHT11
def sterowanie_rgb(temp, hum):
    zeruj_kolory()
    if temp is None or hum is None:
        print("[RGB] Brak odczytu czujnika!")
        return

    # Logika sterowania diodą RGB
    if temp <= 25:
        print("[RGB] Zielony: temperatura <= 25°C")
        pwm_green.ChangeDutyCycle(100)  # Zielony na 100%
    else:
        print("[RGB] Czerwony: temperatura > 25°C")
        pwm_red.ChangeDutyCycle(100)  # Czerwony na 100%

    if hum < 50:
        print("[RGB] Niebieski: wilgotność < 50%")
        pwm_blue.ChangeDutyCycle(100)  # Niebieski na 100%

# Funkcja czyszcząca piny GPIO
def cleanup_pins():
    zeruj_kolory()
    pwm_red.stop()
    pwm_green.stop()
    pwm_blue.stop()
    GPIO.cleanup([PIN_RGB_RED, PIN_RGB_GREEN, PIN_RGB_BLUE, PIN_RGB_ANODE, PIN_DHT11_POWER, PIN_DHT11])
    print("GPIO zostało wyczyszczone.")

# Główna funkcja programu
def main():
    global flaga_koniec

    # Efekt ładowania programu
    efekt_ladowania()

    # Uruchomienie wątku czujnika
    watek_czujnika = threading.Thread(target=odczyt_dht11)
    watek_czujnika.start()

    try:
        while True:
            with lock:
                dane = wynik

            if dane:
                temp, hum = dane
                print(f"Temperatura: {temp}°C, Wilgotność: {hum}%")
            else:
                print("[Brak odczytu czujnika]")

            sterowanie_rgb(temp if dane else None, hum if dane else None)
            time.sleep(60)  # Przerwa między kolejnymi iteracjami
    except KeyboardInterrupt:
        print("\n[Koniec] Wyłączono program.")
    finally:
        flaga_koniec = True
        watek_czujnika.join()
        cleanup_pins()

# Uruchomienie programu
if __name__ == "__main__":
    main()
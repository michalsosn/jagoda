#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

BUTTON_PIN = 17
BUZZER_PIN = 24


def main():
    try:
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(BUTTON_PIN, GPIO.IN)
        GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.LOW)

        last_pressed = False
        while True:
            pressed = GPIO.input(BUTTON_PIN)
            if pressed and not last_pressed:
                print "Button pressed"
                GPIO.output(BUZZER_PIN, GPIO.HIGH)
            elif not pressed and last_pressed:
                print "Button released"
                GPIO.output(BUZZER_PIN, GPIO.LOW)
            last_pressed = pressed
            time.sleep(0.1)
    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()


#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

LED_PIN = 18

def main():
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(LED_PIN, GPIO.OUT)

        while True:
            print "LED on"
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(1)
            print "LED off"
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(1)
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    main()


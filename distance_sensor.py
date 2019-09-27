#!/usr/bin/env python

import RPi.GPIO as GPIO
import time


SOUND_SPEED = 343 # m/s

TRIGGER_PIN = 4
ECHO_PIN = 27


def trigger_sensor():
    GPIO.output(TRIGGER_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIGGER_PIN, GPIO.LOW)


def measure_pulse_duration():
    while GPIO.input(ECHO_PIN) == 0: pass
    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 1: pass
    pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    return pulse_duration
    

def pulse_duration_to_distance(pulse_duration):
    return pulse_duration * SOUND_SPEED / 2


def measure_distance_sensor():
    trigger_sensor()
    duration = measure_pulse_duration()
    return pulse_duration_to_distance(duration)


def main():
    try:
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(TRIGGER_PIN, GPIO.OUT)
        GPIO.setup(ECHO_PIN, GPIO.IN)

        print "Waiting for sensor to settle"
        time.sleep(2)

        while True:
            print "Triggering the sensor"
            distance = measure_distance_sensor()
            print "Distance:", round(distance * 100, 2), "cm"
            time.sleep(1)

    finally:
        GPIO.cleanup()


if __name__ == "__main__":
    main()


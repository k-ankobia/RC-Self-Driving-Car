import RPi.GPIO as GPIO
import time


IN1 = 17
IN2= 27
ENA = 22
IN3 = 19
IN4 = 26
ENB = 13

def set_gpio_pins():
    """Sets the GPIO pins for the two motors"""
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(BACK_MOTOR_DATA_IN2, GPIO.OUT)
    GPIO.setup(BACK_MOTOR_DATA_IN1, GPIO.OUT)
    GPIO.setup(FRONT_MOTOR_DATA_IN3, GPIO.OUT)
    GPIO.setup(FRONT_MOTOR_DATA_IN4, GPIO.OUT)
    GPIO.setup(BACK_MOTOR_ENABLE_PIN, GPIO.OUT)


def set_right_mode():
    """Set mode to Right"""
    GPIO.output(FRONT_MOTOR_DATA_IN3, True)
    GPIO.output(FRONT_MOTOR_DATA_IN4, False)

def set_left_mode():
    """Set mode to Left"""
    GPIO.output(FRONT_MOTOR_DATA_IN3, False)
    GPIO.output(FRONT_MOTOR_DATA_IN4, True)

def set_reverse_mode():
    """Set mode to Reverse"""
    GPIO.output(BACK_MOTOR_DATA_IN2, False)
    GPIO.output(BACK_MOTOR_DATA_IN1, True)

def set_forward_mode():
    """Set mode to Forward"""
    GPIO.output(BACK_MOTOR_DATA_IN2, True)
    GPIO.output(BACK_MOTOR_DATA_IN1, False)

# def set_idle_mode():
#     """Set mode to Idle"""
#     set_back_motor_to_idle()
#     set_front_motor_to_idle()

# def set_back_motor_to_idle():
#     """Sets the Back motor to Idle state"""
#     GPIO.output(BACK_MOTOR_DATA_IN2, True)
#     GPIO.output(BACK_MOTOR_DATA_IN1, True)

# def set_front_motor_to_idle():
#     """Sets the Front motor to Idle state"""
#     GPIO.output(FRONT_MOTOR_DATA_IN3, True)
#     GPIO.output(FRONT_MOTOR_DATA_IN4, True)




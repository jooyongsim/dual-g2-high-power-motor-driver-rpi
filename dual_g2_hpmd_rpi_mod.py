import pigpio

_pi = pigpio.pi()
if not _pi.connected:
    raise IOError("Can't connect to pigpio")

_pin_M1FLT = 5
_pin_M2FLT = 6
_pin_M1PWM = 12
_pin_M2PWM = 13
_pin_M1EN = 22
_pin_M2EN = 23
_pin_M1DIR = 24
_pin_M2DIR = 25

_pi.set_pull_up_down(_pin_M1FLT, pigpio.PUD_UP) # make sure FLT is pulled up
_pi.write(_pin_M1EN, 1) # enable driver by default
_pi.write(_pin_M1DIR, 1)

duty = 0.5
_pi.hardware_PWM(_pin_M1PWM, 20000, int(1000000*duty));
# 20 kHz PWM, duty cycle in range 0-1000000 as expected by pigpio

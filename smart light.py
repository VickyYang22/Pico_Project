from machine import Pin, ADC, I2C
import ws2812b
import utime
from ultrasonic import ultrasonic

rocket_x = ADC(27)
rocket_y = ADC(28)
button = Pin(26, Pin.IN, Pin.PULL_UP)

Echo = Pin(18, Pin.IN)
Trig = Pin(17, Pin.OUT)
ultrasonic = ultrasonic(Trig, Echo)

ring_pin = 5
numpix = 8

i2c = I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)

strip = ws2812b.ws2812b(numpix, 0, ring_pin)
strip.fill(0,0,0)
strip.show()

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128, 32, i2c)
        
def read_x():
    value = int(rocket_x.read_u16() * 256 / 65535)
    return value

def read_y():
    value = int(rocket_y.read_u16() * 256 / 65535)
    return value

def btn_state():
    press = False
    if button.value() == 0:
        press = True
    return press

def change_color():
    if read_y() >= 250:
        strip.fill(0,0,0)
        strip.fill(255,0,0)
        strip.show()
            
        oled.fill(0)
        oled.text("Red", 50, 15)
        oled.show()
        utime.sleep(1)
            
        oled.fill(0)
        oled.text("Red ^", 0, 0)
        oled.text("Green <", 70, 0)
        oled.text("Blue >", 0, 20)
        oled.text("White v", 70, 20)
        oled.show()
            
    elif read_y() <= 5:
        strip.fill(0,0,0)
        strip.fill(255,255,255)
        strip.show()
            
        oled.fill(0)
        oled.text("White", 50, 15)
        oled.show()
        utime.sleep(1)
            
        oled.fill(0)
        oled.text("Red ^", 0, 0)
        oled.text("Green <", 70, 0)
        oled.text("Blue >", 0, 20)
        oled.text("White v", 70, 20)
        oled.show()
            
    elif read_x() <= 5:
        strip.fill(0,0,0)
        strip.fill(0,0,255)
        strip.show()
            
        oled.fill(0)
        oled.text("Blue", 50, 15)
        oled.show()
        utime.sleep(1)
            
        oled.fill(0)
        oled.text("Red ^", 0, 0)
        oled.text("Green <", 70, 0)
        oled.text("Blue >", 0, 20)
        oled.text("White v", 70, 20)
        oled.show()
            
    elif read_x() >= 250:
        strip.fill(0,0,0)
        strip.fill(0,255,0)
        strip.show()
            
        oled.fill(0)
        oled.text("Green", 50, 15)
        oled.show()
        utime.sleep(1)
            
        oled.fill(0)
        oled.text("Red ^", 0, 0)
        oled.text("Green <", 70, 0)
        oled.text("Blue >", 0, 20)
        oled.text("White v", 70, 20)
        oled.show()

while True:
    value_x = read_x()
    value_y = read_y()
    state = btn_state()
    distance = ultrasonic.Distance_accurate()
    print("x:%d, y:%d"%(value_x, value_y))
    print("distance is %d cm"%(distance))
    utime.sleep_ms(1)
    
    if distance <= 130:
        change_color()
        oled.fill(0)
        oled.text("Red ^", 0, 0)
        oled.text("Green <", 70, 0)
        oled.text("Blue >", 0, 20)
        oled.text("White v", 70, 20)
        oled.show()
        
    elif distance >= 131:
        strip.fill(0,0,0)
        strip.show()
        oled.fill(0)
        oled.show()
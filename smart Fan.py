from machine import Pin,I2C,PWM
import random
import ws2812b
from ultrasonic import ultrasonic
from dht11 import DHT11
from ir import ir
import utime,time

i2c = I2C(0,scl=Pin(21),sda=Pin(20),freq =200000)

from ssd1306 import SSD1306_I2C
oled = SSD1306_I2C(128,32,i2c)

human = Pin(11,Pin.IN)
led = Pin(25,Pin.OUT)

abc = 0

pin= Pin(22,Pin.OUT)
dht11 = DHT11(pin)




def led_on():
    led.value(1)
    
def led_off():
    led.value(0)
    
def detect_someone():
    if human.value() == 1:
        return True
    return False






def check_tem():
    tem = dht11.temperature
    hum = dht11.humidity
        
    print("temperature is %d C" % tem)
    time.sleep(.2)
    print("Humidity is %d " % hum)
    time.sleep(.2)
        
    oled.fill(0)
    oled.text("temperature %d C" % tem,0,10)
    oled.text("Humidity is %d" % hum,10,25)
    oled.show()
    utime.sleep(1)
    oled.fill(0)
    oled.show()
    if tem >= 30 and hum >= 40 :
        pwm_motor(50)
        music_mode()
        buzzer.off()
    elif tem >= 30 and hum >= 50 :
        pwm_motor(100)
        music_mode()
        buzzer.off()
    else :
        pwm_motor(0)







red = Pin(0,Pin.OUT)
green = Pin(1,Pin.OUT)
blue = Pin(2,Pin.OUT)

def rgb_red(state):
    if state == 0:
        red.value(0)
    else :
        red.value(1)
        
def rgb_green(state):
    if state == 0:
        green.value(0)
    else :
        green.value(1)
        
def rgb_blue(state):
    if state == 0:
        blue.value(0)
    else :
        blue.value(1)
        
def rgb_off():
    red.value(0)
    green.value(0)
    blue.value(0)
    
def rgb_on():
    red.value(1)
    green.value(1)
    blue.value(1)






fan = PWM(Pin(13))
fan.freq(1000)

def my_map(x, in_min, in_max, out_min, out_max):
    return int((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

def pwm_motor(speed):
    if speed > 100 or speed < 0:
        print("Please enter a limited value of 0-100")
        return
    pulse = my_map(speed, 0, 100, 0, 65535)
    fan.duty_u16(pulse)
    







ring_pin = 5
numpix = 8
strip = ws2812b.ws2812b(numpix, 0, ring_pin)

Echo = Pin(18,Pin.IN)
Trig = Pin(17,Pin.OUT)
ultrasonic = ultrasonic(Trig,Echo)

def cm_light():
    distance = ultrasonic.Distance_accurate()
    print("distance is %d cm" %(distance))
    utime.sleep(0.2)
    
    if distance <=100:
        for i in range(numpix):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            strip.set_pixel(i, r, g, b)  
    
        strip.show()  
        utime.sleep(1)
        
    else  :
        strip.fill(0,0,0)
        strip.show()
 
 
 
 
 
 
 
 
led = Pin(25,Pin.OUT)
key = Pin(27,Pin.IN,Pin.PULL_UP)

def led_on():
    led.value(1)
    
def led_off():
    led.value(0)

def press_state():
    if key.value() == 0:
        return True 
    return False    





buzzer = Pin(4,Pin.OUT)

C4 = 261.63
D4 = 293.66
E4 = 329.63
F4 = 349.23
G4 = 392.00
A4 = 440.00
B4 = 493.88

# Note durations
quarter_note = 500
half_note = 1000
whole_note = 2000

melody1 = [
    (E4, quarter_note), (E4, quarter_note), (F4, half_note),
    (G4, half_note), (G4, quarter_note), (F4, quarter_note),
    (E4, half_note), (D4, quarter_note), (C4, quarter_note),
    (D4, half_note), (E4, half_note), (E4, quarter_note),
    (D4, quarter_note), (D4, half_note), (E4, half_note),
    (E4, quarter_note), (F4, quarter_note), (G4, half_note),
    (G4, half_note), (F4, quarter_note), (E4, quarter_note),
    (D4, half_note), (C4, quarter_note), (D4, quarter_note),
    (E4, whole_note)
]

melody2 = [
    (C4, quarter_note), (D4, quarter_note), (E4, quarter_note),
    (C4, quarter_note), (E4, quarter_note), (F4, quarter_note),
    (G4, half_note), (C4, quarter_note), (D4, quarter_note),
    (E4, quarter_note), (C4, quarter_note), (E4, quarter_note),
    (F4, half_note), (G4, quarter_note), (C4, quarter_note),
    (G4, quarter_note), (F4, quarter_note), (E4, quarter_note),
    (D4, quarter_note), (C4, whole_note)
]

def play_note(frequency, duration):
    for _ in range(int(duration / 2)):
        buzzer.on()
        utime.sleep_us(int(500000 / frequency))
        buzzer.off()
        utime.sleep_us(int(500000 / frequency))
        
def music_mode():
        for note in melody2:
            play_note(note[0], note[0])
            utime.sleep_ms(0)  # Add a small gap between notes
        utime.sleep(0)  # Pause between repeats
        





while True:
    if detect_someone() == True:
        abc += 1
        led_on()
        print('check = ',abc)
        utime.sleep(.2)
        
        rgb_off()
        rgb_on()
        utime.sleep(1)
        
        check_tem()
        cm_light()
        
    else :
        oled.fill(0)
        oled.text("System off",20,10)
        oled.show()
        rgb_off()
        led_off()
        buzzer.off()


from machine import Pin,I2C, PWM
import time, random, utime, ws2812b
from ir import ir
from ssd1306 import SSD1306_I2C
 
#Configure infrared receiving pin
pin = Pin(6, Pin.IN, Pin.PULL_UP)
buzzer_pin = Pin(4, Pin.OUT)

red = Pin(0, Pin.OUT)
green = Pin(1, Pin.OUT)
blue = Pin(2, Pin.OUT)

G4 = 392.00
P3 = 960


rolls = 2

# roll color
ring_pin = 5 # Mdoule connect pin
numpix = 24
strip = ws2812b.ws2812b(numpix, 0, ring_pin)
strip.fill(0,0,0) # Clear RGB buffer
strip.show()


i2c=I2C(0, scl=Pin(21), sda=Pin(20), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)

#Configure infrared receiver library
Ir = ir(pin)

melody=[P3, P3]
melody1=[G4, G4]

def emergency(frequency):
    for _ in range(1000):
        buzzer_pin.on()
        utime.sleep_us(int(5000 / frequency))
        
        buzzer_pin.off()
        utime.sleep_us(int(5000 / frequency))

def play_note(frequency):
    for _ in range(1000):
        buzzer_pin.on()
        utime.sleep_us(int(5000 / frequency))
        
        buzzer_pin.off()
        utime.sleep_us(int(5000 / frequency))
        
  


        
def rgb_off():
    red.value(0)
    green.value(0)
    blue.value(0)
    
def rgb_on():
    red.value(1)
    green.value(1)
    blue.value(1)
    
prev_value = None
rgb_off()
while True:
    #Read remote control data
    strip.fill(0,0,0)
    #rgb_off()
    value = Ir.Getir()
    oled.fill(0)
    oled.show()
    
    
    if value is not None and value != prev_value:
        prev_value = value


        if value == 17:
            oled.text("4,  white", 0, 15)
            oled.show()
            rgb_on()
            for i in range(rolls):
                for note in melody:
                    play_note(note)
            print(value)
#             time.sleep_ms(100)    
            
        elif value == 25:
            oled.text("1,  red", 0, 15)
            oled.show()
            for i in range(rolls):
                for note in melody:
                    play_note(note)
            red.value(1)
            print(value)
#             time.sleep_ms(100)
            
        elif value == 49:
            oled.text("2,  green ", 0, 15)
            oled.show()
            for i in range(rolls):
                for note in melody:
                    play_note(note)
            green.value(1)
            print(value)
#             time.sleep_ms(100)
            
        elif value == 189:
            oled.text("3,  blue ", 0, 15)
            oled.show()
            for i in range(rolls):
                for note in melody:
                    play_note(note)
            blue.value(1)
            print(value)
#             time.sleep_ms(100)
            
        elif value == 133:
            oled.text("7,  whiteblue ", 0, 15)
            oled.show()
            blue.value(1)
            green.value(1)
            for i in range(rolls):
                for note in melody:
                    play_note(note)
            print(value)
#             time.sleep_ms(100)
            
        elif value == 57:
            oled.text("5,  pink ", 0, 15)
            oled.show()
            blue.value(1)
            red.value(1)
            for i in range(rolls):
                for note in melody:
                    play_note(note)
            print(value)
#             time.sleep_ms(100)
            
        elif value == 181:
            oled.text("6,  yellow ", 0, 15)
            oled.show()
            green.value(1)
            red.value(1)
            for i in range(rolls):
                for note in melody:
                    play_note(note)
            print(value)
#             time.sleep_ms(100)

        elif value == 165:
            oled.text("8, ramdom color ", 0, 15)
            oled.show()
            for i in range(rolls):
                for note in melody:
                    play_note(note)
            for i in range(numpix):
                strip.fill(0,0,0)
                r = random.randint(0, 256)
                g = random.randint(0, 256)
                b = random.randint(0, 256)
         
                strip.set_pixel(i, r, g, b)
                strip.show()
                utime.sleep(.3)
            print(value)
            strip.fill(0,0,0)
            time.sleep_ms(100)
            
            

        elif value == 149:
            oled.text("9,  emergency    ", 0, 15)
            oled.show()
            green.value(1)
            red.value(1)
            for i in range(rolls):
                for note in melody1:
                    emergency(note)
            
            print(value)
#             time.sleep_ms(100)
            
            
        elif value == 139:
            oled.text(" shutdowm all ", 0, 15)
            oled.show()
            print(value)
            rgb_off()
            strip.fill(0,0,0)
            oled.fill(0)
            oled.show()
            time.sleep_ms(1)
            
            
        else:
            rgb_off()
            strip.fill(0,0,0)
            oled.fill(0)
            oled.show()
            time.sleep_ms(1)
        
        



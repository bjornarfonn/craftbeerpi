from brewapp import app
from views import base
from util import *
import time
from thread import start_new_thread

###
@brewinit()
def initBuzzer():
    buzzer_gpio = app.brewapp_config.get("BUZZER_GPIO", None)
    app.logger.info("BUZZER GPIO: " + str(buzzer_gpio) )
    try:
        GPIO.setup(buzzer_gpio, GPIO.OUT)
        GPIO.output(buzzer_gpio, 0)
    except Exception as e:
        app.logger.error(e)

def nextStepBeep():
    start_new_thread(playSound,(sound1,))

def timerBeep():
    start_new_thread(playSound,(sound2,))

def resetBeep():
    start_new_thread(playSound,(sound3,))

## Melodie Pattern
## H = HIGH
## L = LOW
## Float value as pause
## it must be a L at the end to turn the sound off
sound1 = ["H",1.0,"L"]
sound2 = ["H",0.2,"L",0.2,"H",0.2,"L",0.2,"H",0.2,"L"]
sound3 = ["H",0.1,"L",0.1,"H",0.1,"L",0.1,"H",0.1,"L"]

## Logic to play the sound melodie
def playSound(melodie):
    try:
        buzzer_gpio = app.brewapp_config.get("BUZZER_GPIO", None)
        if(buzzer_gpio == None):
            return
        for i in melodie:
            if(isinstance(i, str)):
                if(i == "H"):
                    GPIO.output(buzzer_gpio,GPIO.HIGH)
                else:
                    GPIO.output(buzzer_gpio,GPIO.LOW)
            else:
                time.sleep(i)
    except Exception as e:
        print app.logger.error("ERROR")

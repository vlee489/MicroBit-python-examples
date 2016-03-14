from microbit import *
hours = 0minuites = 0minuiteToHours = 0total = 0
while True:    if button_a.is_pressed():        hours = hours + 1        display.scroll((str)hours)
    if button_b.is_pressed():
        minuites = minuites + 1
        display.scrol((str)minuites)

    if accelerometer.was_gesture("shake"):
        minuiteToHours = hours * 60
        total = minuiteToHours + minuites
        display.scroll("Starting time for")
        display.scroll((str)total)
        display.scroll("minuites")
        

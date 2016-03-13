from microbit import *

stopclock = 0
loop = 1

while True:
    #Sees if the A button is pressed, if so it them
    #it starts the stopclock
    if button_a.is_pressed():
        while loop == 1 :
            sleep(1000)
            stopclock = stopclock + 1
            display.scroll(str(stopclock))
            
            #looks to see if B is held down when the stop clock is active,
            #if so it it stops the stop clock and reads out the final time
            if button_b.is_pressed():
                loop = loop + 1
                display.scroll("Final time is ")
                display.scroll(str(stopclock))
                display.scroll(" Seconds")
                break
    
    #Looks to see if the microbit is shaked and is on a loop value of 2
    #If so it resets the stopclock time    
    if (accelerometer.was_gesture("shake") and loop ==  2):
        loop = loop - 1
        stopclock = stopclock - stopclock
        display.scroll("Stopclock Reset")
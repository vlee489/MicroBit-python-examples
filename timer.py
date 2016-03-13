from microbit import *

timer = 0
var = 1

while True:
    if (button_b.is_pressed() and var ==  1):
        print ("I don't do anthing but stop the timer")
        display.scroll("I only work to stop the timer")
        
    if (accelerometer.was_gesture("shake") and var ==  2):
        var = var - 1
        timer = timer - timer
        print ("Timer Cleared")
        display.scroll("Timer Cleared")
        
    if (button_a.is_pressed() and var ==  2):
        print ("you need to reset the timer first")
        display.scroll("You need to reset the timer first")


    if pin2.is_touched():
        print ("Timer is at ",timer, " seconds")
        if var == 2 :
            print ("you need to reset you timer to use")
            display.scroll("Shake me to use me again")
        else:
            print ("I'm ready to use again")
            display.scroll("Ready to Rock `N` Roll")
        sleep(1000)

    if button_a.is_pressed():
        while var == 1 :
            print ("Timer Started")
            while var == 1 :
                sleep(1000)
                timer = timer + 1
                print(timer," seconds")
                display.scroll(str(timer))
                if button_b.is_pressed():
                    var = var + 1
                    print("Timer Stopped")
                    print("Final time is ",timer," seconds")
                    display.scroll("Final time is ")
                    display.scroll(str(timer))
                    display.scroll(" Seconds")
                    break

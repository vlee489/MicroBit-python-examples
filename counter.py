import microbit

ctr = 0# Initialize counter

while True:

    if microbit.button_a.is_pressed():

        ctr = ctr + 1

        microbit.display.scroll(str(ctr)) #Display counter

    elif microbit.button_b.is_pressed():

        ctr = ctr - 1

        microbit.display.scroll(str(ctr))

        

    microbit.sleep(100)
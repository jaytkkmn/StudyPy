from pyfirmata import Arduino, util
from time import sleep

board = Arduino('/dev/ttyACM0')



def sensor_LED(board): # sensor detect and blink LED

    iterator = util.Iterator(board)
    iterator.start()

    irsensor = board.get_pin('d:3:i') # get sensor signal from Uno pin 2


    while True:
        sleep(2)
        print(irsensor.read())
        if irsensor.read() == False:
            board.digital[13].write(1)
        else:
            board.digital[13].write(0)




sensor_LED(board)

'''
while True:
    board.digital[13].write(1)
    sleep(2)
    board.digital[13].write(0)
    #sleep(0)
'''

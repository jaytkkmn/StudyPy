from pyfirmata import Arduino, util
from time import sleep
import paho.mqtt.client as mqtt
import time

global board_name

board_name = Arduino('/dev/ttyACM0')

pin = 3
broker_host = "localhost"
subscribe_topic = "Jack/switch"


def sensor_led(board, pin_nr):  # sensor detect and blink LED

    iterator = util.Iterator(board)
    iterator.start()
    irsensor = board.get_pin("d:" + str(pin_nr) + ":i")  # get sensor signal from Uno pin 2
    while True:
        sleep(2)
        print(irsensor.read())
        if irsensor.read() is False:
            board.digital[13].write(1)
        else:
            board.digital[13].write(0)


def led_blink(board, pin_nr):  # Blink LED

    while True:
        board.digital[pin_nr].write(1)
        sleep(2)
        board.digital[pin_nr].write(0)
        sleep(1)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe(subscribe_topic)

    # The callback for when a PUBLISH message is received from the server.


def on_message(client, userdata, msg):
    msg.payload = msg.payload.decode("utf-8")  # If msg.payload doesn't decode to "utf-8". The result will become b' msg.payload.
    print(msg.topic + " " + msg.payload)

    if msg.payload == 'true':
        board_name.digital[13].write(1)
    else:
        board_name.digital[13].write(0)


def node_red_switch():  # Click Node_red switch button to switch the LED ON/OFF
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker_host, 1883, 60)

    client.loop_forever()


sensor_led(board_name, pin)
# led_blink(board_name, pin)
# node_red_switch()

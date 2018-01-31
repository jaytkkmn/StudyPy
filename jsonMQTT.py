#!/usr/bin/python3

import paho.mqtt.publish as publish


def MQTT_pub(topic, payload):
    ''' Use MQTT to publish the data '''

    host = "localhost"
    publish.single(topic, payload, qos=1, hostname=host)


topic = "jack"
MQTT_pub(topic, "a")
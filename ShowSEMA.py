#!/usr/bin/python3

from subprocess import check_output
import paho.mqtt.publish as publish

# subprocess.run(["./semaeapi_tool", "-a", "SemaEApiBoardGetStringA", "1"]) #doesn't capture output

def MQTT_pub(topic, payload):
    ''' Use MQTT to publish the data '''

    host = "localhost"
    publish.single(topic, payload, qos=1, hostname=host)

def get_boardinfo():
    '''Get information by SEMAEApi and use subprocess->check_output to capture result'''

    topic = "adlink/SEMA/boardinfo"  #Set MQTT topic for def MQTT_pub

    baord_info_index = [2, 4] # index2 = Board Name; index4 = Board BIOS Revision

    for index in baord_info_index[:]:
        payload = check_output(["./semaeapi_tool", "-a", "SemaEApiBoardGetStringA", str(index)]).decode("utf-8")
        MQTT_pub(topic + "/" + str(index), payload)

    return 0

def get_boardvalue():
    '''Get information by SEMAEApi and use subprocess->check_output to capture result'''

    topic = "adlink/SEMA/boardvalue" #Set MQTT topic for def MQTT_pub

    baord_value_index = [8, 10, 11, 18]  # 8 = CPU Temperature; 10 = System Temperature; 11 = CPU Core Voltage; 18 = CPU Fan

    for index in baord_value_index[:]:
        payload = check_output(["./semaeapi_tool", "-a", "SemaEApiBoardGetValue", str(index)]).decode("utf-8")
        MQTT_pub(topic + "/" + str(index), payload)

    return 0

def get_CPUINFO():
    '''Get information by SEMAEApi and use subprocess->check_output to capture result'''

    topic = "adlink/SEMA/cpuinfo"  # Set MQTT topic for def MQTT_pub

    payload = check_output(["./semaeapi_tool", "-a", "SemaEApiCPUGetString", "1"]).decode("utf-8")
    print(payload)
    MQTT_pub(topic + "/" + "1", payload)

    value_index = [3, 4]  # 3 = Number of CPUs; 4 = Number of cores of each CPU

    for index in value_index[:]:
        payload = check_output(["./semaeapi_tool", "-a", "SemaEApiCPUGetValue", str(index)]).decode("utf-8")
        print(payload)
        MQTT_pub(topic + "/" + str(index), payload)

    return 0

def get_Memory():
    '''Get information by SEMAEApi and use subprocess->check_output to capture result'''

    topic = "adlink/SEMA/memory"  # Set MQTT topic for def MQTT_pub

    value_index = [1, 2, 3]  # 1 = memory frequency; 2 = total size; 3 = free memory

    for index in value_index[:]:
        payload = check_output(["./semaeapi_tool", "-a", "SemaEApiMemoryGetValue", str(index)]).decode("utf-8")
        MQTT_pub(topic + "/" + str(index), payload)
    return 0


get_boardinfo()
get_CPUINFO()

while True:
    get_boardvalue()
    get_Memory()

#!/usr/bin/env python
#
# Copyright (c) 2013 Fabian Affolter <fabian at affolter-engineering.ch>
#
# Released under the MIT license.
#
from gi.repository import Notify
import mosquitto

broker = '127.0.0.1'
port = 1883
topic = 'test/#'
qos = 0

# Assign a callback for connect and disconnect
def on_connect(mosq, obj, rc):
    if rc == 0:
        print 'Connected successfully to %s:%s' % (broker, port)

def on_disconnect(mosq, obj, rc):
    print 'Not able to connect to %s:%s' % (broker, port)

# Send a notification after a new message has arrived
def on_message(mosq, obj, msg):
    message = msg.payload + ' \n(Topic: ' + msg.topic + ' - QoS: ' + str(msg.qos) + ')'
    Notify.init('MQTT message')
    n = Notify.Notification.new(
        'MQTT message:',
        message,
        '/usr/share/icons/gnome/32x32/places/network-server.png')
    n.show()

def main():
    # Setup the MQTT client
    mqttclient = mosquitto.Mosquitto('notify')
    mqttclient.connect(broker, port, 60)

    # Callbacks
    mqttclient.on_connect = on_connect
    mqttclient.on_message = on_message
    mqttclient.on_disconnect = on_disconnect

    # Subscribe to topic 'test'
    mqttclient.subscribe(topic, qos)

    # Loop the client forever
    while mqttclient.loop() == 0:
        pass

if __name__ == '__main__':
    main()

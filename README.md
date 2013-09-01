# mqtt-notify

Subscribe to a topic and desktop notifications are sent if a message about a 
specific MQTT topic arrives.

## Prerequisites/Installation

### Get the files
Clone the `mqtt-notify` [repository](https://github.com/fabaff/mqtt-notify):
```
git clone git@github.com:fabaff/mqtt-notify.git
```

###Dependencies
`mqtt-notify` depends on a couple of additional pieces: 

- [mosquitto](http://mosquitto.org/)
- [notify-python](http://www.freedesktop.org/wiki/Software/DBusBindings/)

```
sudo yum -y install notify-python mosquitto
```

## Usage
Make the _mqtt-notify.py_ file executable and run it.

```
./mqtt-notify.py
```

## License
`mqtt-notify` licensed under MIT, for more details check LICENSE.

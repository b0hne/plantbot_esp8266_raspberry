import network, machine, webrepl
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('<SSID>', '<Password>')
while not wifi.isconnected():
    machine.idle()
webrepl.start()


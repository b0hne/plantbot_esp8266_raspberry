import network, machine, webrepl
wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect('Felsit', '3sUdo#k8-9')
while not wifi.isconnected():
    machine.idle()
webrepl.start()


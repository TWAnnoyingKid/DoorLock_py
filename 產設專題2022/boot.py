# This file is executed on every boot (including wake-boot from deepsleep)

import esp
esp.osdebug(None)
import gc
import webrepl
#webrepl.start()
gc.collect()

#10
def flash(times):
    from machine import Pin
    import time
    led = Pin(2,Pin.OUT)

    for i in range(times):
        led.value(0)
        time.sleep(0.1)
        led.value(1)
#20
        time.sleep(0.1)
    led.value(0)
    
def connectAP(ssid,pwd):
    import network
    wlan = network.WLAN(network.STA_IF)
    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid,pwd)
#30
        while not wlan.isconnected():
            pass
    print('network config:',wlan.ifconfig())


print('-----Boot.py is done by Dancer')



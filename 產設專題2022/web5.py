import time
from machine import Pin, PWM
servo = PWM(Pin(0), freq=50) //D3

def rotate(servo, degree):
    period = 20000
    minDuty = int(500/period * 1024)
    maxDuty = int(2500/period * 1024)
    unit = (maxDuty - minDuty)/180
    _duty = round(unit * degree ) + minDuty
    _duty = min(maxDuty, max(minDuty, _duty))
    servo.duty(_duty)
    
def flash(times):
    led = Pin(2,Pin.OUT)

    for i in range(times):
        led.value(not led.value())
        time.sleep(0.1)
        led.value(not led.value())
        time.sleep(0.1)

def url(PORT):
    import time
    print("Running url ")
    import socket
    from machine import Pin
    LED0 = Pin(5, Pin.OUT)
    LED1 = Pin(4, Pin.OUT)
    LED2 = Pin(0, Pin.OUT)
    LED0.value(1)
    LED1.value(1)
    LED2.value(1)
    num = 0
    test=0
    s=socket.socket()
    HOST='0.0.0.0'
    httpHeader = b"""\
    HTTP/1.0 200 OK

    <!doctype html>
    <html>
      <head>
        <meta charset="utf-8">
        <title>MicroPython</title>
      </head>
      <body>
        <p><b><h1 align="center">產設專題 遠端控制門鎖</h1></b></p>
        <p><b><h1 align="center">程式by. 白簡銘</h1></b></p>
        <form align="center">
        <button name="Up" value="ON001" type="submit"
        style="width:400px;height:100px;font-size:40px;color:red;background:#5c99dc">上</button><br><br>
        <button name="Down" value="ON001" type="submit"
        style="width:400px;height:100px;font-size:40px;color:red;background:#26d3fa">下</button><br><br>
        </form>
      </body>
    </html>
    """

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    s.listen(30)
    print("Server port",PORT)

    while True:
        client,addr=s.accept()
        print("Client address:",addr)
        
        req=client.recv(2048)
        print(req)
        request = str(req)
        req==0
        LEDON0 = request.find('/?Up=ON001')
        LEDOFF0 = request.find('/?Down=ON001')
        print('LEDON0=',LEDON0)
        print('LEDOFF0=',LEDOFF0)
        if LEDON0 == 6:
            LED0.value(0)
            time.sleep(0.1)
            LED0.value(1)
            rotate(servo,30)
            flash(1)   //至此為控制伺服機轉動至30度
        if LEDOFF0 == 6:
            LED2.value(0)
            time.sleep(0.1)
            LED2.value(1)
            rotate(servo,150)
            flash(3)   //至此為控制伺服機轉動至150度
        client.send(httpHeader.format(num=num))
        client.close()
        test=num
        print('---------------',test)



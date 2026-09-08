import network
import machine
import socket
import time
import neopixel

speed = 2
pin_clk = machine.Pin(6, machine.Pin.IN, machine.Pin.PULL_UP)
pin_dt = machine.Pin(7, machine.Pin.IN, machine.Pin.PULL_UP)

last_clk_state = pin_clk.value()

relay1 = machine.Pin(27, machine.Pin.OUT, value=0)
relay2 = machine.Pin(28, machine.Pin.OUT, value=0)
relay3 = machine.Pin(30, machine.Pin.OUT, value=0)
relay4 = machine.Pin(31, machine.Pin.OUT, value=0)

btn1 = machine.Pin(26, machine.Pin.OUT, machine.Pin.PULL_UP)
btn2 = machine.Pin(29, machine.Pin.OUT, machine.Pin.PULL_UP)
btn3 = machine.Pin(14, machine.Pin.OUT, machine.Pin.PULL_UP)    
btn4 = machine.Pin(16, machine.Pin.OUT, machine.Pin.PULL_UP)
btn5 = machine.Pin(13, machine.Pin.OUT, machine.Pin.PULL_UP)

btn1_state = 0
btn2_state = 0
btn3_state = 0
btn4_state = 0
btn5_state = 0

btn1_time = 0
btn2_time = 0
btn3_time = 0
btn4_time = 0
btn5_time = 0

led1 = neopixel.NeoPixel(machine.Pin(10),2)
led2 = neopixel.NeoPixel(machine.Pin(11),2)
led3 = neopixel.NeoPixel(machine.Pin(8),2)
led4 = neopixel.NeoPixel(machine.Pin(12),2)
ledrotary = neopixel.NeoPixel(machine.Pin(37),6)

btns = {
    "tubelight":[btn1,btn1_time,btn1_state],
    "bedlight":[btn2,btn2_time,btn2_state],
    "desklight":[btn3,btn3_time,btn3_state],
    "socket":[btn4,btn4_time,btn4_state],
    "fan":[btn5,btn5_time,btn5_state]
}

relays = {
    "tubelight": relay1,
    "bedlight": relay2,
    "desklight": relay3,
    "socket": relay4
}

leds = {
    "tubelight": led1,
    "bedlight": led2,
    "desklight": led3,
    "socket": led4,
    "fan":ledrotary
}

# import fan
# sensitive code with propreitary api (I dont want people around the world to control my fan)

def toggle_fan():
    # sensitive code with propreitary api (I dont want people around the world to control my fan)
    ledrotary[0] = (0,0,0)
    ledrotary[1] = (0,0,0)
    ledrotary[2] = (0,0,0)
    ledrotary[3] = (0,0,0)
    ledrotary[4] = (0,0,0)
    ledrotary[5] = (0,0,0)
    ledrotary.write()
    time.sleep(0.5)
    ledrotary[0] = (0,0,255)
    ledrotary[1] = (0,0,255)
    ledrotary[2] = (0,0,255)
    ledrotary[3] = (0,0,255)
    ledrotary[4] = (0,0,255)
    ledrotary[5] = (0,0,255)
    ledrotary.write()

def fan_speed(speed):
    # sensitive code with propreitary api (I dont want people around the world to control my fan)
    for i in range(speed):
        ledrotary[5-i] = (0,0,0)
    ledrotary.write()
    time.sleep(0.5)
    ledrotary[0] = (0,0,255)
    ledrotary[1] = (0,0,255)
    ledrotary[2] = (0,0,255)
    ledrotary[3] = (0,0,255)
    ledrotary[4] = (0,0,255)
    ledrotary[5] = (0,0,255)
    ledrotary.write()
    pass

ssid = ""
pssw = ""

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid,pssw)

while not wlan.isconnected():
    time.sleep(1)
print("Connected to Wifi")
ip_address = wlan.ifconfig()[0]
print(ip_address)

def update_speed(current_speed):
    global last_clk_state
    
    current_clk = pin_clk.value()
    new_speed = current_speed
    
    if last_clk_state == 1 and current_clk == 0:
        if pin_dt.value() == 1:
            new_speed = min(6, current_speed + 1)
        else:
            new_speed = max(1, current_speed - 1)
            
    last_clk_state = current_clk
    return new_speed

def webpage():
    tubelight = "active" if relays["tubelight"].value() == 1 else ""
    bedlight = "active" if relays["bedlight"].value() == 1 else ""
    desklight = "active" if relays["desklight"].value() == 1 else ""
    socket = "active" if relays["socket"].value() == 1 else ""

    return f"""

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Smart Switchboard</title>
    <style>
*{{
    margin: 0;
    padding: 0;
}}
body{{
    background-color: rgb(11, 17, 24);
}}
h1{{
    color: rgb(227, 166, 75);
    font-family:'Courier New', Courier, monospace ;
    justify-self: center;
    margin: 10px;
}}
div{{
    display:grid;
    grid-template-columns: auto auto auto;
    justify-content: center;
}}

button:last-child {{
  grid-column: 2;
}}

button{{
    margin: 20px;
    padding: 2px;
    background-color:rgba(255, 231, 169, 0);
    border: 2.5px solid rgb(227, 166, 75);
    border-radius: 2px;
    color: rgb(227, 166, 75);
    font-weight: bold;
}}
button:hover{{
    color: rgb(11, 17, 24);
    background-color:rgb(223, 126, 28);
    border: 2.5px solid rgb(223, 126, 28);
}}
button:active{{
    color: rgb(11, 17, 24);
    background-color:rgb(255, 153, 0);
    border: 2.5px solid rgb(255, 153, 0);
}}

button.active{{
    background-color:rgb(255, 232, 174);
    color: rgb(255, 161, 19);
    border: 2.5px solid rgb(255, 153, 0);
}}
button.active:hover{{
    background-color:rgb(255, 232, 174);
    color: rgb(255, 161, 19);
    border: 2.5px solid rgb(255, 153, 0);
}}
    </style>
</head>
<body>
    <h1>Smart Switchboard</h1>
    <div>
        <a href="/api/relay?r=tubelight"><button class="{tubelight}">Tubelight</button></a>
        <a href="/api/relay?r=bedlight"><button class="{bedlight}">Bed light</button></a>
        <a href="/api/relay?r=desklight"><button class="{desklight}">Desk light</button></a>
        <a href="/api/relay?r=socket"><button class="{socket}">Socket</button></a>
        <a href="/api/relay?r=-fan"><button>Fan</button></a>
        <a href="/api/relay?r=fan"><button>Fan</button></a>
        <a href="/api/relay?r=+fan"><button>Fan</button></a>
    </div>
</body>
</html>
"""

def checkbtnpress(btn):
    if btn[0].value() == 1 & btn[2] == 0:
        return (False,time.ticks_ms(),1)
    elif btn.value() == 0 & btn[2] == 1:
        diff = time.ticks_diff(time.ticks_ms(),btn[1])
        return (True,diff,0)
    return (False,btn[1],btn[2])

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('',80))
s.listen(5)

while 1:
    _ = update_speed(speed)
    if _ != speed:
        speed = _
        fan_speed(speed)

    btn1press,btn1_time,btn1_state = checkbtnpress(btns["tubelight"])
    btn2press,btn2_time,btn2_state = checkbtnpress(btns["bedlight"])
    btn3press,btn3_time,btn3_state = checkbtnpress(btns["desklight"])
    btn4press,btn4_time,btn4_state = checkbtnpress(btns["socket"])
    btn5press,btn5_time,btn5_state = checkbtnpress(btns["fan"])

    if btn1press:
        if btn1_time < 500:
            relays["tubelight"].value(not relays["tubelight"].value())
            if relays["tubelight"].value():
                led1[0] = (0,255,0)
                led1[1] = (0,255,0)
            else: 
                led1[0] = (255,0,0)
                led1[1] = (255,0,0)
            led1.write()
            btn1_time = 0

    if btn2press:
        if btn2_time < 500:
            relays["bedlight"].value(not relays["bedlight"].value())
            if relays["bedlight"].value():
                led2[0] = (0,255,0)
                led2[1] = (0,255,0)
            else: 
                led2[0] = (255,0,0)
                led2[1] = (255,0,0)
            led2.write()
            btn2_time = 0

    if btn3press:
        if btn3_time < 500:
            relays["desklight"].value(not relays["desklight"].value())
            if relays["desklight"].value():
                led3[0] = (0,255,0)
                led3[1] = (0,255,0)
            else: 
                led3[0] = (255,0,0)
                led3[1] = (255,0,0)
            led3.write()
            btn3_time = 0

    if btn4press:
        if btn4_time < 500:
            relays["socket"].value(not relays["socket"].value())
            if relays["socket"].value():
                led4[0] = (0,255,0)
                led4[1] = (0,255,0)
            else: 
                led4[0] = (255,0,0)
                led4[1] = (255,0,0)
            led4.write()
            btn4_time = 0
    if btn5press:
        if btn5_time < 500:
            toggle_fan()
            btn5_time = 0

    try:
        conn, addr = s.accept()
        request = conn.recv(1024).decode('utf-8')
        request_url = request.split('\r\n'[0])
        if "GET /api/relay" in request_url:
            for key in relays.keys():
                if "r=fan" in request_url:
                    toggle_fan()
                elif "r=-fan" in request_url:
                    speed -= 1
                    fan_speed(speed)
                elif "r=+fan" in request_url:
                    speed += 1
                    fan_speed(speed)
                elif f"r={key}" in request_url:
                    relays[key].value(not relays[key].value())
                    if relays[key].value():
                        leds[key][0] = (0,255,0)
                        leds[key][1] = (0,255,0)
                    else: 
                        leds[key][0] = (255,0,0)
                        leds[key][1] = (255,0,0)
                    leds[key].write()
                    break
            response = "HTTP/1.1 303 See Other\r\nLocation: /\r\n\r\n"
            conn.send(response)
        else:
            response = webpage()
            conn.send("http/1.1 200 OK\r\nContent-Type; text/html\r\n\r\n" + response)
        conn.close()
    except Exception as e:
        pass

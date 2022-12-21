# Tank


## Tank CLI

#### Start

```shell
python tank_cli.py
```

#### Controls

```shell
# ↖  ↑  ↗   1 speed--
#   QWE     2 speed++
# ← ASD →   H clockwise
#   ZXC     J counterclockwise
# ↙  ↓  ↘　
```


## Tank Web Server

```shell
export FLASK_APP=tank_server
flask run -h 192.168.4.76 -p 8080
```

#### Endpoints
```shell
GET /tank/forward
GET /tank/reverse
GET /tank/stop
GET /tank/turn-left
GET /tank/turn-right
GET /tank/left-track-forward
GET /tank/left-track-reverse
GET /tank/right-track-forward
GET /tank/right-track-reverse
GET /tank/clockwise
GET /tank/counter-clockwise
```



## Sample Output

#### CLI Output

```shell
#### Output
```shell
python tank_cli.py
Init Track, enA: 16, in1: 20, in2: 26
Init Track, enA: 25, in1: 24, in2: 23
stop
left track stop
left track stop
w
forward
left track forward
left track forward
x
reverse
left track reverse
left track reverse
d
turn right
left track forward
left track stop
a
turn left
left track stop
left track forward
h
rotate clockwise
left track forward
left track reverse
j
rotate counterclockwise
left track reverse
left track forward
e
left track forward
c
left track reverse
q
left track forward
z
left track reverse
s
stop
left track stop
left track stop
```

#### Tank Web Server Output

```shell
 * Running on http://192.168.4.76:8080
Press CTRL+C to quit
forward
left track forward
left track forward
192.168.4.44 - - [21/Dec/2022 01:43:56] "GET /tank/forward HTTP/1.1" 200 -
forward
left track forward
left track forward
192.168.4.44 - - [21/Dec/2022 01:43:57] "GET /tank/forward HTTP/1.1" 200 -
reverse
left track reverse
left track reverse
192.168.4.44 - - [21/Dec/2022 01:44:00] "GET /tank/reverse HTTP/1.1" 200 -
stop
left track stop
left track stop
192.168.4.44 - - [21/Dec/2022 01:44:01] "GET /tank/stop HTTP/1.1" 200 -
turn left
left track stop
left track forward
192.168.4.44 - - [21/Dec/2022 01:44:03] "GET /tank/turn-left HTTP/1.1" 200 -
turn right
left track forward
left track stop
192.168.4.44 - - [21/Dec/2022 01:44:06] "GET /tank/turn-right HTTP/1.1" 200 -
left track forward
192.168.4.44 - - [21/Dec/2022 01:44:08] "GET /tank/left-track-forward HTTP/1.1" 200 -
left track forward
192.168.4.44 - - [21/Dec/2022 01:44:10] "GET /tank/left-track-forward HTTP/1.1" 200 -
left track reverse
192.168.4.44 - - [21/Dec/2022 01:44:12] "GET /tank/left-track-reverse HTTP/1.1" 200 -
left track forward
192.168.4.44 - - [21/Dec/2022 01:44:14] "GET /tank/right-track-forward HTTP/1.1" 200 -
left track reverse
192.168.4.44 - - [21/Dec/2022 01:44:17] "GET /tank/right-track-reverse HTTP/1.1" 200 -
rotate clockwise
left track forward
left track reverse
192.168.4.44 - - [21/Dec/2022 01:44:19] "GET /tank/clockwise HTTP/1.1" 200 -
rotate counterclockwise
left track reverse
left track forward
192.168.4.44 - - [21/Dec/2022 01:44:22] "GET /tank/counter-clockwise HTTP/1.1" 200 -
stop
left track stop
left track stop
192.168.4.44 - - [21/Dec/2022 01:44:24] "GET /tank/stop HTTP/1.1" 200 -
```
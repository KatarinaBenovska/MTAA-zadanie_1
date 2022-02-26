import socketserver
import socket
import sipfullproxy
import logging
from datetime import datetime


def main():
    
    date_time= datetime.now()
    dt_string = date_time.strftime("%d/%m/%Y %H:%M:%S")
    print(dt_string+": Spustenie SIP PROXY")
    hostname = socket.gethostname()
    ipaddress = socket.gethostbyname(hostname)
    print("PROXY IP: "+ipaddress)
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='proxy.log',level=logging.INFO,datefmt='%H:%M:%S')
    sipfullproxy.recordroute = "Record-Route: <sip:%s:%d;lr>" % (ipaddress,sipfullproxy.PORT)
    sipfullproxy.topvia = "Via: SIP/2.0/UDP %s:%d" % (ipaddress,sipfullproxy.PORT)
    server = socketserver.UDPServer((sipfullproxy.HOST, sipfullproxy.PORT), sipfullproxy.UDPHandler)
    server.serve_forever()

main()
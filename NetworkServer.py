__author__ = 'siddiqui'

import socket
def Main():
    host = '127.0.0.1'
    port = 2000

    newsoc = socket.socket()
    newsoc.bind((host, port))

    newsoc.listen(4)
    conn, address = newsoc.accept()
    print "Connection from : " + str(address)
    while True:
        data = conn.recv(1024)
        if not data :
            break
        print "from connected user :" + str(data)
        data = str(data).upper()
        print "sending: " + str(data)
        conn.send(data)
    conn.close()

if __name__== "__main__" :
    Main()
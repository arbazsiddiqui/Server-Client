__author__ = 'siddiqui'
import socket

def Main():
    host = '127.0.0.1'
    port = 2000

    newsoc = socket.socket()
    newsoc.connect((host,port))

    message = raw_input()

    while message != 'Q':
        newsoc.send(message)
        data = newsoc.recv(1024)
        print "recieved from server :" + str(data)
        message = raw_input()
    newsoc.close()

if __name__ == '__main__':
    Main()
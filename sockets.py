import socket
import sys

def sockets_create():
    try: 
        global host
        global port
        global s
        host = ''
        port = 9999
#!/usr/bin/env python2
import argparse
import zmq
import socket


def get_local_ip():
    """
    Retrieve the clients local ip address and return it as a string

    :returns IpAddress as String
    """
    ip = socket.gethostbyname(socket.gethostname())
    return ip

context = zmq.Context()

socket = context.socket(zmq.DEALER)

# @ep14 172.16.16.228:5555
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--connect-address', default='tcp://127.0.0.1:5555')

args = parser.parse_args()

socket.connect(args.connect_address)
for i in range(10):
    msg = "Hi server this is my message {}".format(i)
    socket.send(msg)
    print socket.recv()

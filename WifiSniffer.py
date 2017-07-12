#!/usr/bin/env python
#coding='utf-8'

import json
import time
from socket import *


def jason_data_parser(jason_data):
    data = json.loads(jason_data, 'utf-8')

    detail_info_list = []
    rate = 0;wssid = "";wmac = "";lat = "";lon = "";addr = "";detailkeys = ""

    datakeys = data.keys()
    if 'rate' in datakeys:
        rate = data['rate']
    if 'wssid' in datakeys:
        wssid = data['wssid']
    if 'wmac' in datakeys:
        wmac = data['wmac']
    if 'lat' in datakeys:
        lat = data['lat']
    if 'lon' in datakeys:
        lon = data['lon']
    if 'addr' in datakeys:
        addr = data['addr']

    if 'data' in datakeys:
        detail_info_list = data['data']

    for e in detail_info_list:
        if 'mac' in e:
            print "mac =", e["mac"],
        if 'rssi' in e:
            print "rssi", e["rssi"]


def main():
    HOST = ''
    PORT = 5000
    BUFSIZE = 2048
    ADDR = (HOST, PORT)

    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    while True:
        print 'waiting for connect...'
        tcpCliSock, addr = tcpSerSock.accept()
        print '.... connected from:', addr

        total_data = ""
        while True:
            data_segement = tcpCliSock.recv(BUFSIZE)
            if not data_segement:
                print 'No jason datas'
                break
            total_data += data_segement

        print "total_data 's len=",total_data
        print total_data

        datastr = total_data.decode('utf-8')
        strlen = datastr.find("data=")
        jason_data = datastr[strlen + 5:len(datastr)]
        jason_data_parser(jason_data)
        tcpCliSock.close()
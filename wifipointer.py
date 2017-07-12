#!/usr/bin/env python
# -*- coding: utf-8 -*-



import json
import time
from socket import *
from time import ctime
from flask import Blueprint, request


def check_json_format(raw_msg):
    """
    用于判断一个字符串是否符合Json格式
    :param self:
    :return:
    """
    if isinstance(raw_msg, str):  # 首先判断变量是否为字符串
        try:
            json.loads(raw_msg, encoding='utf-8')
        except ValueError:
            return False
        return True
    else:
        return False


def get_data():
    return

HOST = ''
PORT = 5000
BUFSIZE = 2048
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR);
tcpSerSock.listen(5)

while True:
    print 'waiting for connect...'
    tcpCliSock, addr = tcpSerSock.accept()
    print '.... connected from:', addr

    total_data = ""
    while True:
        datas = tcpCliSock.recv(BUFSIZE);
        print "datas type is : ", type(datas)

        if not datas:
            print 'No jason datas'
            break;
        # total_data.append(datas)
        total_data+=datas

    print '\n================Get jason datas====================='
    print total_data
    print '================Get jason datas=====================\n'

    # print datas
    datastr = total_data.decode('utf-8')
    # datastr = str(total_data)
    print datastr
    strlen = datastr.find("data=");
    # print  "data's index=", strlen
    datastr2 = datastr[strlen + 5:len(datastr)]
    print "\n\n============================"
    print datastr2
    print "============================\n\n"
    # da = "\"\"\""+datastr2+"\"\"\""

    # print "\n\n============================"
    # print da
    # print "============================\n\n"
    ##load jason###
    # da2 ="""{"id":"00ac892f","mmac":"5e:cf:7f:ac:89:2f","rate":"1","wssid":"TP-LINK_HyFi_504","wmac":"08:57:00:8a:12:0a","time":"Sun Jul 02 20:18:07 2017","lat":"31.473772","lon":"104.676430","addr":"\xe5\x9b\x9b\xe5\xb7\x9d\xe7\x9c\x81\xe7\xbb\xb5\xe9\x98\xb3\xe5\xb8\x82\xe6\xb6\xaa\xe5\x9f\x8e\xe5\x8c\xba\xe9\xab\x98\xe6\x96\xb0\xe5\x8c\xba\xe8\xa1\x97\xe9\x81\x93\xe4\xb8\x89\xe6\xb2\xb3\xe8\xa1\x97;\xe6\x99\xae\xe6\x98\x8e\xe4\xb8\xad\xe8\xb7\xaf\xe4\xb8\x8e\xe7\x81\xab\xe7\x82\xac\xe8\xa5\xbf\xe8\xa1\x97\xe5\x8c\x97\xe6\xae\xb5\xe8\xb7\xaf\xe5\x8f\xa3\xe4\xb8\x9c\xe5\x8d\x97203\xe7\xb1\xb3","data":[{"mac":"08:57:00:5e:ba:e0","rssi":"-89","range":"77.1"},{"mac":"88:25:93:74:65:17","rssi":"-76","range":"25.5","router":"Y.S EDU"},{"mac":"08:57:00:8a:12:0a","rssi":"-56","rssi1":"-54","rssi2":"-69","rssi3":"-69","range":"25.5","router":"TP-LINK_HyFi_504"},{"mac":"ec:88:8f:6f:ef:bc","rssi":"-86","range":"59.7","router":"TP-LINK-he"},{"mac":"9c:61:21:4f:b1:a9","rssi":"-88","range":"70.8","router":"ChinaNet-Kihm"},{"mac":"c0:61:18:a8:31:bc","rssi":"-94","range":"118.1"},{"mac":"d0:c7:c0:92:56:5a","rssi":"-94","range":"118.1","router":"FAST_565A"},{"mac":"f8:d1:11:fc:65:ca","rssi":"-93","range":"108.5","router":"TP-LINK_FC65CA"},{"mac":"08:57:00:95:04:73","rssi":"-72","range":"18.1","router":"TP-LINK_HyFi_504"},{"mac":"b0:95:8e:0a:1d:98","rssi":"-83","rssi1":"-82","rssi2":"-83","rssi3":"-83","range":"46.3","router":"TP-LINK_1D98"},{"mac":"28:6c:07:99:c0:66","rssi":"-86","rssi1":"-81","rssi2":"-80","range":"35.8"},{"mac":"c8:3a:35:cd:48:e8","rssi":"-94","range":"118.1"}]}"""

    data = json.loads(datastr2, 'utf-8')
    # if(check_json_format(datastr2)):
    #     data = json.loads(datastr2, 'utf-8')
    #     print
    # else:
    #     continue;

    detail_info_list= []
    rate = 0
    wssid = ""
    wmac    = ""
    lat      = ""
    lon      = ""
    addr    = ""
    detailkeys = ""
    datakeys=data.keys()
    if 'rate' in datakeys:
        rate = data['rate']
        print rate
    if 'wssid' in datakeys:
        wssid = data['wssid']
        print wssid
    if 'wmac' in datakeys:
        wmac = data['wmac']
        print wmac
    if 'lat' in datakeys:
        lat = data['lat']
        print lat
    if 'lon' in datakeys:
        lon = data['lon']
        print lon
    if 'addr' in datakeys:
        addr = data['addr']
        print addr
    print data.keys()
    print 'wssid value is'
    print wssid

    print "\n###########"
    if 'data' in datakeys:
        detail_info_list = data['data']
        print detail_info_list
    print "\n###########"

    print "\n#### ITEM #######"
    for e in detail_info_list:
        if 'mac' in e :
            print "mac =", e["mac"],
        if 'rssi' in e:
            print "rssi", e["rssi"]
    print "\n#### ITEM #######"
    tcpCliSock.close()


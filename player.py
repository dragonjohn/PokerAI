#! /usr/bin/env python
# -*- coding:utf-8 -*-


import time
import json
from websocket import create_connection

# pip install websocket-client
ws = ""

#Global Variable



def takeAction(action, data):
    if action == "__bet":
        #time.sleep(2)
        print "my bet is " + str(data)
        ws.send(json.dumps({
            "eventName": "__action",
            "data": {
                "action": "bet",
                "playerName": "jl",
                "amount": 100
            }
        }))
    elif action == "__new_round":
        print "\n new round : "+str(data)+"\n"
    elif action == "__deal":
        print "＊＊＊＊＊cards in table = " + str(data)
    elif action == "__start_reload":
        print "You can reload now"
        ws.send(json.dumps({
            "eventName" : "__reload"
            }))
    elif action == "__action":
        #time.sleep(2)
        print "What I can do is "+ str(data)
        ws.send(json.dumps({
            "eventName": "__action",
            "data": {
                "action": "call", #還可以是 : "check", "fold", "allin", "raise", "bet"
                "playerName": "jl"
            }
        }))
    elif action == "__show_action":
        print "Current show Action"


def doListen():
    try:
        global ws
        ws = create_connection("ws://allhands2018-beta.dev.spn.a1q7.net:3001")
        ws.send(json.dumps({
            "eventName": "__join",
            "data": {
                "playerName": "jl"
            }
        }))
        while 1:
            result = ws.recv()
            msg = json.loads(result)
            event_name = msg["eventName"]
            data = msg["data"]
            print event_name
            print data
            takeAction(event_name, data)
    except Exception, e:
        print e.message
        doListen()


if __name__ == '__main__':
    doListen()

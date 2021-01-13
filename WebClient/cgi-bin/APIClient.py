from dataclasses import dataclass
import socket, struct, threading, time
import json
from server import *

HOST = 'localhost'
PORT = 12345

def ProcessReceive(ClientID):
    while True:
        try:
            print('Messages: ' + GetList(ClientID)['m'])
        except Exception:
            pass
        time.sleep(10)

def Client():
    ClientID = Init()['id']

    t = threading.Thread(target=ProcessReceive,  args=[ClientID])
    t.start()
    while True: 
        n = int(input("1. Отправить клиенту \n2. Отправить всем \n3. Получить сообщения\n 4. Выйти \n"))
        if (n == 1):
            id = int(input("Введите id \n"))
            s = input("Введите сообщение\n")
            SendMsg(ClientID, s, id)
        elif (n == 2):
            s = input("Введите сообщение\n")
            SendMsg(ClientID, s, M_ALL)
        elif (n == 3):
            print('Messages' + GetList(ClientID)['m'])
        elif (n == 4):
            Exit(ClientID)
            return 
Client()
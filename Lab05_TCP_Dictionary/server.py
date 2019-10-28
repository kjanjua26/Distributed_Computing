import socket 
from _thread import *
import threading 
  
print_lock = threading.Lock() 
# Maintain the data dictionary 
data_dict = {"accidial": "dial someone's number on phone accidentally",
            "agender": "people do not identify as male or female",
            "airball": "completely miss the basket, rim, and backboard with a shot",
            "automagically": "in a way that seems magical, especially by computer",
            }
 
def threaded(c):
    while True: 
        data = c.recv(1024)
        if not data:
            print('Bye') 
            print_lock.release() 
            break
        data = data.decode('ascii')
        typeInp, data = data.split(";")
        print("Key: ", data, " Type: ", typeInp)
        if (int(typeInp) == 1):
            if data in data_dict:
                data = data_dict[data]
                c.send(data.encode('ascii'))
            else:
                c.send("key does not exist!".encode('ascii'))
        if(int(typeInp) == 2):
            key, meaning = data.split(":")
            if key in data_dict:
                c.send("key already exists!".encode('ascii'))
            else:
                data_dict[key] = meaning
                c.send("added!".encode('ascii'))
        if(int(typeInp) == 3):
            if data in data_dict:
                del data_dict[data]
                c.send("removed!".encode('ascii'))
            else:
                c.send("key does not exist!".encode('ascii'))
    c.close() 
  
  
def Main(): 
    host = "127.0.0.1"
    port = 12359
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to port", port) 
    s.listen(5) 
    print("socket is listening") 
    while True: 
        c, addr = s.accept() 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
        start_new_thread(threaded, (c,)) 
    s.close() 

if __name__ == '__main__': 
    Main() 
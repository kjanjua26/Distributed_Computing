import socket 
  
  
def Main(): 
    host = '127.0.0.1'
    port = 12359
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
    s.connect((host,port)) 
    message = "Hello Server! I am connected!"
    inp = int(input("\nWhat do you want to do? \n1. Query? \n2. Add? \n3. Remove?\n"))
    while True: 
        if (inp == 1):
            word = input("\nWhat do you want to query?")
            wordInp = str(1) + ";" + word
            s.send(wordInp.encode('ascii'))
            data = s.recv(1024)
            print("The word {} you asked for => \n{}".format(word, str(data.decode('ascii'))))
            ans = input('\nDo you want to continue(y/n): ') 
            if ans == 'y':
                continue
            else: 
                break
        if(inp == 2):
            word = input("\nWhat do you want to add?\n")
            meaning = input("\nWhat is the meaning of it?\n")
            toSend = str(2) + ";" + word + ":" + meaning
            s.send(toSend.encode('ascii'))
            data = s.recv(1024)
            print("The word {} you asked to add => {}".format(word, str(data.decode('ascii'))))
            ans = input('\nDo you want to continue(y/n): ') 
            if ans == 'y': 
                continue
            else: 
                break
        if(inp == 3):
            word = input("\nWhat do you want to remove?\n")
            toSend = str(3) + ";" + word
            s.send(toSend.encode('ascii'))
            data = s.recv(1024)
            print("The word {} you asked to remove => {}".format(word, str(data.decode('ascii'))))
            ans = input('\nDo you want to continue(y/n): ') 
            if ans == 'y': 
                continue
            else:
                break
    s.close() 
  
if __name__ == '__main__': 
    Main() 

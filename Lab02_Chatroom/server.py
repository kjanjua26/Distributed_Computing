'''
    This is the server class which can initiate multiple clients and handles all the processes related to it.
    I use multithreading to manage each client with a thread so that switching can occur without lags to other clients.
    This is a Peer-to-Peer architecture approach.
'''
from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread

class Server:

    def __init__(self):
        self.HOST = '127.0.0.1'
        self.PORT = 33045
        self.BUFSIZE = 1024
        self.ADDR = (self.HOST, self.PORT)
        self.SERVER = socket(AF_INET, SOCK_STREAM)
        self.SERVER.bind(self.ADDR)
        self.SERVER.listen(5)
        self.clients = {}
        self.addresses = {}


    def connections(self):
        while True:
            client, client_addr = self.SERVER.accept()
            print("Client => {} is on!\n".format(client))
            client.send(bytes("Please enter your name: ", "utf-8"))
            self.addresses[client] = client_addr
            Thread(target=self.handler, args=(client,)).start()

    def handler(self, client):
        name = client.recv(self.BUFSIZE).decode("utf-8")
        welcome = "Welcome {}, if you want to leave, please press 'Q'".format(name)
        client.send(bytes(welcome, "utf8"))
        msg = "{} has joined the chat!".format(name)
        self.broadcaster(bytes(msg, "utf8"))
        self.clients[client] = name

        while True:
            msg = client.recv(self.BUFSIZE)
            if msg != bytes("{Q}", "utf8"):
                if msg == bytes("U", "utf-8"):
                    toWhom = input("Unicast to whom?")
                    self.unicaster(msg, name, toWhom)
                else:
                    self.broadcaster(msg, name + ": ")
            else:
                client.send(bytes("Q", "utf8"))
                client.close()
                del self.clients[client]
                self.broadcaster(bytes("{} has left the chat.".format(name), "utf8"))
                break

    def broadcaster(self, msg, prefix=''):
        for ix, client in enumerate(self.clients):
            print("Client => ", prefix)
            client.send(bytes(prefix, "utf8") + msg)

    def unicaster(self, msg, prefix='', toWhom=''):
        senderClient = list(self.clients.keys())[list(self.clients.values()).index(prefix)]
        toWhomAddr = list(self.clients.keys())[list(self.clients.values()).index(toWhom)]

        print("Sender, ToWhom => ", prefix, toWhom)
        print("UNICAST => ", senderClient, toWhomAddr)
        ms = input("What to send?")
        addr_ = str(toWhomAddr).split('=')[-1].replace(">", "")
        f, s = addr_.split(",")
        f = f.replace('(', '')
        s = s.replace(')', '')
        f = f.replace("'", "")
        print(f, s)
        addr = f, int(s)
        print(addr)
        senderClient.sendto(bytes(ms, encoding='utf8'), addr)

    def closeServer(self):
        self.SERVER.close()

if __name__ == '__main__':
    server = Server()
    ACCEPT_THREAD = Thread(target=server.connections())
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    server.closeServer()


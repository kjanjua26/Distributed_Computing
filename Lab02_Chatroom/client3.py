'''
    This is the client class which can initiate multiple clients and handles all the processes related to it.
    I use multithreading to manage each client with a thread so that switching can occur without lags to other clients.
    This is a Peer-to-Peer architecture approach.
'''

from threading import Thread
from socket import AF_INET, socket, SOCK_STREAM
import tkinter

class Client:

    def __init__(self):
        self.top = tkinter.Tk()
        self.top.title("DC Lab 02")
        messages_frame = tkinter.Frame(self.top)
        self.my_msg = tkinter.StringVar()
        self.my_msg.set("")
        scrollbar = tkinter.Scrollbar(messages_frame)
        self.msg_list = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.msg_list.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        self.msg_list.pack()
        messages_frame.pack()
        entry_field = tkinter.Entry(self.top, textvariable=self.my_msg)
        entry_field.bind("<Return>", self.send)
        entry_field.pack()
        send_button = tkinter.Button(self.top, text="Send", command=self.send)
        send_button.pack()
        self.top.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.HOST = '127.0.0.1'
        self.PORT = 33045
        self.BUFSIZE = 1024
        ADDR = (self.HOST, self.PORT)

        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(ADDR)
        self.client_list = {}

    def receive(self):
        while True:
            try:
                msg = self.client_socket.recv(self.BUFSIZE).decode("utf8")
                print("MSG => ", msg)
                self.msg_list.insert(tkinter.END, msg)
            except OSError:
                break

    def send(self, event=None):
        msg = self.my_msg.get()
        self.my_msg.set("")
        self.client_socket.send(bytes(msg, "utf8"))
        if msg == "{Q}":
            self.client_socket.close()
            self.top.quit()

    def on_closing(self, event=None):
        self.my_msg.set("{Q}")
        self.send()

    def unicast(self, name):
        pass

if __name__ == '__main__':
    client = Client()
    receive_thread = Thread(target=client.receive)
    receive_thread.start()
    tkinter.mainloop()


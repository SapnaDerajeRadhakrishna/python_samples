from websocket import create_connection

def short_lived_connection():
    #create the connection with server
    ws = create_connection("ws://127.0.0.1:4041/")
    print("Sending 'Hello, Server'...")
    ws.send("Hello, Server")
    print("Sent")
    print("Receiving...")
    result =  ws.recv()
    print("Received '%s'" % result)
    #close the connection after receiving the response
    ws.close()

if __name__ == '__main__':
    short_lived_connection()
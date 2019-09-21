import websocket


def on_message(ws, message):
    '''
        This method is invoked when ever the client
        receives any message from server
    '''
    print("received message as {}".format(message))
    ws.send("hello again")
    print("\nsending 'hello again'")

def on_error(ws, error):
    '''
        This method is invoked when there is an error in connectivity
    '''
    print("received error as {}".format(error))

def on_close(ws):
    '''
        This method is invoked when the connection between the 
        client and server is closed
    '''
    print("Connection closed")

def on_open(ws):
    '''
        This method is invoked as soon as the connection between client
        and server is opened and only for the first time
    '''
    ws.send("hello there")
    print("sent message on open")


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:4041/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
'''
    This module hosts a websocket server using tornado
    libraries
'''
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.websocket as ws
import tornado.options
import time

LISTEN_PORT = 4041
LISTEN_ADDRESS = 'localhost'

class web_socket_handler(ws.WebSocketHandler):
    '''
    This class handles the websocket channel
    '''
    @classmethod
    def route_urls(cls):
        return [(r'/',cls, {}),]
    
    def simple_init(self):
        self.last = time.time()
        self.stop = False

    
    def open(self):
        '''
            client opens a connection
        '''
        self.simple_init()
        print("New client connected")
        self.write_message("You are connected")

        
    def on_message(self, message):
        '''
            Message received on the handler
        '''
        print("received message {}".format(message))
        self.write_message("You said {}".format(message))
        self.last = time.time()
    
    def on_close(self):
        '''
            Channel is closed
        '''
        print("connection is closed")
        self.loop.stop()
    
    def check_origin(self, origin):
        return True


def initiate_server():
    #create a tornado application and provide the urls
    app = tornado.web.Application(web_socket_handler.route_urls())
    
    #setup the server
    server = tornado.httpserver.HTTPServer(app)
    server.listen(LISTEN_PORT, LISTEN_ADDRESS)
    
    #start io/event loop
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    initiate_server()
        
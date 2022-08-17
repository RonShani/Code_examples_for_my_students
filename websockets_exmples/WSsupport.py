from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
import socket
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory, listenWS
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


wsStr = "Wait..."

class BroadcastServerProtocol(WebSocketServerProtocol):

    def onOpen(self):
        self.factory.register(self)
        print("connected")


    def onMessage(self, payload, isBinary):
        if not isBinary:
            msg = "{} from {}".format(payload.decode('utf8'), self.peer)
            print(msg)

    def connectionLost(self, reason):
        WebSocketServerProtocol.connectionLost(self, reason)
        self.factory.unregister(self)

class BroadcastServerFactory(WebSocketServerFactory):

    """
    Simple broadcast server broadcasting any message it receives to all
    currently connected clients.
    """

    def __init__(self, url):
        WebSocketServerFactory.__init__(self, url)
        self.clients = []

    def register(self, client):
        if client not in self.clients:
            print("registered client {}".format(client.peer))
            self.clients.append(client)

    def unregister(self, client):
        if client in self.clients:
            print("unregistered client {}".format(client.peer))
            self.clients.remove(client)

    def broadcast(self, msg):
        print("broadcasting message '{}' ..".format(msg))
        for c in self.clients:
            c.sendMessage(msg.encode('utf8'))
            print("message sent to {}".format(c.peer))

class BroadcastPreparedServerFactory(BroadcastServerFactory):

    """
    Functionally same as above, but optimized broadcast using
    prepareMessage and sendPreparedMessage.
    """

    def broadcast(self, msg):
        print("broadcasting prepared message '{}' ..".format(msg))
        preparedMsg = self.prepareMessage(msg)
        for c in self.clients:
            c.sendPreparedMessage(preparedMsg)
            print("prepared message sent to {}".format(c.peer))

class WStestApp(App):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        wsStr = "ws://" + self.get_ip() + ":9000"
        ServerFactory = BroadcastServerFactory
        self.factory = ServerFactory(wsStr)
        self.factory.protocol = BroadcastServerProtocol
        listenWS(self.factory)
        print(wsStr)

    def build(self):
        print("OK")

    def txtBtn(self, instance):
        T = instance
        print(T)
        App.get_running_app().factory.broadcast(T)

    def change_label(self, msg):
        print(msg)

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            # doesn't even have to be reachable
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

if __name__ == '__main__':
    WStestApp().run()


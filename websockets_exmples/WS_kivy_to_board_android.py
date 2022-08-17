from kivy.support import install_twisted_reactor
install_twisted_reactor()

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
import socket
from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
from twisted.internet import reactor
from android.permissions import request_permissions, Permission

wsStr = "Wait..."


class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            msgtxt = payload.decode('utf8')
            print("Text message received: {0}".format(payload.decode('utf8')))
            App.get_running_app().change_label(msgtxt)

        # echo back message verbatim
        self.sendMessage(payload, isBinary)

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))

class WStestApp(App):

    def build(self):
        request_permissions([Permission.READ_EXTERNAL_STORAGE,
                             Permission.WRITE_EXTERNAL_STORAGE,
                             Permission.INTERNET,
                             Permission.ACCESS_COARSE_LOCATION])
        self.lay = FloatLayout()
        wsStr = "ws://" + self.get_ip() + ":9000"
        factory = WebSocketServerFactory(wsStr)
        factory.protocol = MyServerProtocol
        reactor.listenTCP(9000, factory)
        print(wsStr)
        self.lbl = Label(text=wsStr)
        self.lay.add_widget(self.lbl)
        return self.lay

    def change_label(self, msg):
        self.lbl.text = msg

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


import sys, os, tornado
from PyQt5.QtWidgets import QDialog, QApplication # case sensitive!
from integrated import *
from interactions import *
from tornado_websocket import *

class AppWindow(QDialog):
    def __init__(self): 
        super().__init__()
        self.ui = Ui_Form() # Class name from bestThermostat.py
        self.ui.setupUi(self)
        self.show()

app = QApplication(sys.argv)
w = Form()
w.show()

application = tornado.web.Application([
    (r'/ws', WSHandler),
])

http_server = tornado.httpserver.HTTPServer(application)
http_server.listen(8888)
myIP = socket.gethostbyname(socket.gethostname())
print('*** Websocket Server Started at %s***' % myIP)
tornado.ioloop.IOLoop.instance().start()

sys.exit(app.exec_())
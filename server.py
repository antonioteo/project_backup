__author__ = 'TeodorZ'

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler
from domain.restaurant import Restaurant
from domain.menuFinder import MenuFinder
from pathHandler import PathHandler

HOST_NAME = 'localhost'
PORT_NUMBER = 80

class ServerParam(HTTPServer):
    def __init__(self, path_handler, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        self._path_handler = path_handler

    @property
    def path_handler(self):
        return self._path_handler


class MyHandler(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        s = self.server.path_handler.handle_it(self.path)
        self.wfile.write(s.encode())

if __name__ == '__main__':
    server_class = ServerParam
    mnfinder = MenuFinder()
    restaurant = Restaurant(mnfinder)
    handle_path = PathHandler(restaurant)
    httpd = server_class(handle_path, (HOST_NAME, PORT_NUMBER), MyHandler)
    try:
       httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
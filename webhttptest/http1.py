from http.server import HTTPServer,BaseHTTPRequestHandler
import os
from urllib import parse
class MyRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        path=parse.urlparse(self.path).path
        query=parse.urlparse(self.path).query
        if path=="/favicon.ico":
            return
        filename = "webfront" + path
        if filename=="webfront/":
            filename="webfront/index.html"
        print(filename)
        if not os.path.exists(filename):
            return

        self.send_response(200)
        self.send_header("Content-Type","text/html")
        self.end_headers()

        with open(filename,"r",encoding="utf8") as f:
            self.wfile.write(f.read().encode("utf8"))
    def do_POST(self):
        print("收到post请求")
        self.send_response(200)
        self.send_header("Content-Type", "text/html")
        self.end_headers()
        print(self.rfile.read())
        print(self.rfile.read().decode("utf8"))

server=HTTPServer(("192.168.12.3",8000),MyRequestHandler)
server.serve_forever()

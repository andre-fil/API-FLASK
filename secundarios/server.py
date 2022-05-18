
from http.server import HTTPServer, BaseHTTPRequestHandler

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'

        #elif self.path == '/contato':
            #self.path = '/contato.html'
        else:
            self.path = f'/{self.path}'

        #file_to_open = open(self.path[1:]).read()
        file_to_open = open(self.path[1:]+'.html').read()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

httpd = HTTPServer(('localhost',5000),Server)
httpd.serve_forever()

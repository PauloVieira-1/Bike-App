from http.server import HTTPServer, BaseHTTPRequestHandler

class helloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type','text/html')
        self.end_headers()
        self.wfile.write('Hello Alex/Paulo!'.encode())
        # /

def main(): 
    PORT = 8000
    Server = HTTPServer(('127.0.0.1', PORT), helloHandler)
    print('Server running on port %s' % PORT)
    Server.serve_forever()

if __name__ == '__main__':
    main()

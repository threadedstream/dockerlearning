from http.server import HTTPServer, SimpleHTTPRequestHandler


if __name__ == '__main__':
    print('Welcome to this server')
    addr = ('', 8080)
    http_server = HTTPServer(addr, SimpleHTTPRequestHandler)
    http_server.serve_forever()


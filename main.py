from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

PORT = 80

with TCPServer(("", PORT), SimpleHTTPRequestHandler) as httpd:
    print(f"Server started at http://localhost:{PORT}")
    httpd.serve_forever()

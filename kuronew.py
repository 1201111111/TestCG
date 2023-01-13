import os, sys, ssl, socket, base64
from signal import signal, SIGINT
from http.server import HTTPServer, BaseHTTPRequestHandler


def main():
    class GetHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            if self.path.endswith("/"):
                self.send_response(200)
                self.send_header("Content-type","text/html")
                self.end_headers()
                data = (b"bypass by <a href='https://t.me/gil2strongg'>@Gil</a> <br>Thanks to <a href='https://t.me/zeexzenn'>@ZeexZeNN</a> <br> Thanks to <a href='https://t.me/MiTM_Attack'>@JeelsBoobz</a> for script")
                self.wfile.write(bytes(data))
                return
            	
        def do_POST(self):
            if self.path.endswith("/kuronewvip/login2.php"):
                self.send_response(200)
                self.send_header("Content-type","text/html")
                self.end_headers()
                data = base64.b64decode("YnlwYXNzIEdpbA==")
                self.wfile.write(bytes(data))
                return

        def log_message(self, format, *args):
            return

    Handler = GetHandler
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="test.crt", keyfile="test.key")
    httpd=HTTPServer(("165.22.110.231", 443), Handler)
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print("Server is running...\nPress CTRL-C to exit!")
    httpd.serve_forever()
main()

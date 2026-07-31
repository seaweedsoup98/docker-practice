from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import pwd

USER_NAME = pwd.getpwuid(os.getuid()).pw_name


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = f"Hello from linux container. user={USER_NAME}\n".encode()

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()

        self.wfile.write(body)


HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()

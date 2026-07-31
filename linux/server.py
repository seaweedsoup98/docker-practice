from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import pwd

USER_NAME = pwd.getpwuid(os.getuid()).pw_name
APP_MODE = os.getenv("APP_MODE", "development")
PORT = int(os.getenv("PORT", "8080"))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = (
            f"Hello from linux container. "
            f"user={USER_NAME}, mode={APP_MODE}, port={PORT}\n"
        ).encode()

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


print(
    f"Starting server: user={USER_NAME}, mode={APP_MODE}, port={PORT}",
    flush=True,
)

HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()

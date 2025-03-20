#!/usr/bin/env python3

import http.server
import ssl
import urllib.parse
import json
import subprocess

USERS = {"admin": "password123", "user": "mypassword"}
sessions = {}

class SecureHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):

    def do_POST(self):
        if self.path == "/login":
            self.handle_login()
        else:
            self.send_error(404, "Not Found")

    def do_GET(self):
        if self.path == "/logout":
            self.handle_logout()
        elif self.path.startswith("/download"):
            self.serve_file_if_logged_in()
        else:
            super().do_GET()

    def handle_login(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode("utf-8")
        params = urllib.parse.parse_qs(post_data)

        username = params.get("username", [""])[0]
        password = params.get("password", [""])[0]

        if USERS.get(username) == password:
            session_token = f"{username}_session"
            sessions[session_token] = username

            self.send_response(200)
            self.send_header("Set-Cookie", f"session={session_token}; Path=/; Secure; HttpOnly")
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Login successful"}).encode("utf-8"))
        else:
            self.send_error(401, "Unauthorized")

    def handle_logout(self):
        cookie = self.headers.get("Cookie", "")
        session_token = self.get_session_token(cookie)

        if session_token in sessions:
            del sessions[session_token]
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"message": "Logged out"}).encode("utf-8"))
        else:
            self.send_error(401, "Not logged in")

    def serve_file_if_logged_in(self):
        cookie = self.headers.get("Cookie", "")
        session_token = self.get_session_token(cookie)

        if session_token in sessions:
            super().do_GET()
        else:
            self.send_error(403, "Forbidden - Login Required")

    def get_session_token(self, cookie):
        if "session=" in cookie:
            return cookie.split("session=")[-1].split(";")[0]
        return None

server_address = ('0.0.0.0', 4443)
httpd = http.server.HTTPServer(server_address, SecureHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(keyfile="certs/private.key", certfile="certs/public.crt")
httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serving on https://0.0.0.0:4443")
httpd.serve_forever()
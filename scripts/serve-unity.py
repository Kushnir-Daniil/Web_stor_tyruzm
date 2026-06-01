#!/usr/bin/env python3
"""Локальний сервер з правильним MIME для Unity WebGL (.wasm)."""
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080


class UnityHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".wasm": "application/wasm",
        ".data": "application/octet-stream",
        ".js": "application/javascript",
        ".json": "application/json",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def log_message(self, format, *args):
        sys.stderr.write("%s - %s\n" % (self.address_string(), format % args))


if __name__ == "__main__":
    os.chdir(ROOT)
    with ThreadingHTTPServer(("", PORT), UnityHandler) as httpd:
        print()
        print("  Unity WebGL сервер")
        print("  Квест:  http://localhost:%s/kvest_web_stor14.html" % PORT)
        print("  Ігри:   http://localhost:%s/public/games.html" % PORT)
        print("  Ctrl+C — зупинити")
        print()
        httpd.serve_forever()

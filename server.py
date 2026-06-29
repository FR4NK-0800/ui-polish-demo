import http.server
import socketserver
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3000

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print(f"[dev-server] {args[0]} {args[1]} {args[2]}")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving UI Polish Demo at http://localhost:{PORT}")
    print("Press Ctrl+C to stop")
    httpd.serve_forever()

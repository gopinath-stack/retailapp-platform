from http.server import BaseHTTPRequestHandler, HTTPServer
import json

VERSION = "4.2.1"


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/":
            response = f"Retail Platform v{VERSION} is running"

            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()

            self.wfile.write(response.encode())

        elif self.path == "/health":
            response = {
                "status": "ok",
                "version": VERSION
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(response).encode())

        elif self.path == "/payment":
            response = {
                "status": "payment service operational",
                "version": VERSION
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(response).encode())

        elif self.path == "/products":
            response = {
                "products": [
                    "Laptop",
                    "Phone",
                    "Headphones"
                ],
                "version": VERSION
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(response).encode())

        elif self.path == "/orders":
            response = {
                "orders": [
                    "ORD-1001",
                    "ORD-1002",
                    "ORD-1003"
                ],
                "version": VERSION
            }

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            self.wfile.write(json.dumps(response).encode())

        else:
            self.send_response(404)
            self.end_headers()


server = HTTPServer(("0.0.0.0", 8081), Handler)

print(f"Retail Platform v{VERSION} running on port 8081")

server.serve_forever()
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Parse query parameters
        parsed_path = urllib.parse.urlparse(self.path)
        query_params = urllib.parse.parse_qs(parsed_path.query)
        index = int(query_params.get("index", [0])[0])

        # Compute Fibonacci number
        fibonacci_number = self.fibonacci(index)

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(f"Fibonacci({index}) = {fibonacci_number}".encode())

    @staticmethod
    def fibonacci(n):
        if n <= 0:
            return "Invalid index"
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

if __name__ == "__main__":
    httpd = HTTPServer(('localhost', 8000), SimpleHTTPRequestHandler)
    print("Serving HTTP on port 8000...")
    httpd.serve_forever()

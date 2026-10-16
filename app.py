import http.server
import socketserver
import webbrowser
import threading
import os

PORT = int(os.environ.get("PORT", 3007))

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Evita problemas de cache durante os testes
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate, max-age=0')
        super().end_headers()

def run_server():
    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Servidor rodando em http://localhost:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    # Abre o navegador automaticamente
    threading.Timer(1.0, lambda: webbrowser.open(f"http://localhost:{PORT}")).start()
    try:
        run_server()
    except KeyboardInterrupt:
        print("\nServidor encerrado.")
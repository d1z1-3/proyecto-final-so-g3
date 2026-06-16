from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # 1. Responder con éxito
        self.send_response(200)
        # 2. Indicar que es JSON
        self.send_header('Content-type', 'application/json')
        # 3. PERMITIR CORS (Esto elimina el error del navegador)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        data = {"mensaje": "Backend Python activo", "status": "ok"}
        self.wfile.write(json.dumps(data).encode('utf-8'))

def run():
    server_address = ('0.0.0.0', 5000)
    httpd = HTTPServer(server_address, MyHandler)
    print("Servidor listo en puerto 5000")
    httpd.serve_forever()

if __name__ == '__main__':
    run()

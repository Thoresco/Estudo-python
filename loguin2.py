from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/submit_task':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            task = post_data.decode('utf-8')

            with open('tasks.txt', 'a') as f:
                f.write(task + '\n')

            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Tarefa adicionada com sucesso!\n')
        else:
            self.send_error(404, 'Caminho não encontrado')

    def do_GET(self):
        if self.path == '/tasks':
            tasks = []
            try:
                with open('tasks.txt', 'r') as f:
                    tasks = f.read().splitlines()
            except FileNotFoundError:
                pass

            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({'tasks': tasks})
            self.wfile.write(response.encode())
        else:
            self.send_error(404, 'Caminho não encontrado')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Servidor Python iniciado na porta {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()

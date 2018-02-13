from http.server import BaseHTTPRequestHandler, HTTPServer
import json


global data

# put data to serve here 
data = {
 
}

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
 
  # GET
  def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        global data
        data_json = json.dumps(data)   
        print(data_json)
        self.wfile.write(data_json.encode())
        return 
 
def run():
  print('starting server...')
  server_address = ('127.0.0.1', 8081)
  httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
  print('running server...')
  httpd.serve_forever()


run()
#Today I am learning about HTTP server, where I learned how to setup a http server in python and how to setup get and post method inside it. I used BASEHTTPRequestHandler from http.server module. I also learned how to run a server from CLI, that was very easy to do. 

from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import date, time,datetime
import json,requests
HOST = "192.168.29.245"
PORT = 3300

class http_server(BaseHTTPRequestHandler):
    
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()
        res = requests.get("https://httpbin.org/html")
        self.wfile.write(bytes(res.text,"utf-8"))
        print(res.content)
    
    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type","application/json")
        self.end_headers()
        
        current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        response = {"time":current_time}
        self.wfile.write(bytes(json.dumps(response),"utf-8"))
        

server = HTTPServer((HOST,PORT),http_server)
print("Server is Running.....")
server.serve_forever()
server.server_close()
print("Server is Closed!")



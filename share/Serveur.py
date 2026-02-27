import socketserver
import http.server
import socket
import os
os.system("TITLE Activite sur votre serveur http. ( par mackedzoa )")
ip = ''
port = 80
address = ("",port)
server = http.server.HTTPServer
handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = [""]
httpd = server(address, handler)
httpd.serve_forever()

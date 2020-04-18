from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl

pathFileKeyPem = './test-keys/key.pem'
pathFileCertPem = './test-keys/cert.pem'
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
    	self.send_response(200)
    	self.end_headers()
    	try:
    		file = open("./" + str(self.path), 'rb')
    		self.wfile.write(file.read())
    	except:
    		print("An exception occurred loading" + str(self.path))
    	

httpd = HTTPServer(('0.0.0.0', 4443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket, 
        keyfile=pathFileKeyPem, 
        certfile=pathFileCertPem, server_side=True)

httpd.serve_forever()

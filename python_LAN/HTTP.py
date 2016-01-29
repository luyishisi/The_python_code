import http.service, os

os.chdir("/home/pi")
httpd = http.sercer.HTTPServer(('127.0.0.1', 8000),
        http.sercer.SimpleHTTPRequestHandler)
httpd.serve_forever()

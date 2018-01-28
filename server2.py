__author__ = 'shy'
__date__ = '2018/1/28 12:59'

from wsgiref.simple_server import make_server


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ['PATH_INFO'])
    path = environ['PATH_INFO']
    if path == '/book':
        return [b'<h1>Hello, book!</h1>']
    elif path == '/web':
        return ['<h1>Hello, web!</h1>'.encode('utf8')]
    else:
        return [b'<h1>Hello, shy!</h1>']


httpd = make_server('', 8002, application)

print('Serving HTTP on port 8002...')
# 开始监听HTTP请求:
httpd.serve_forever()


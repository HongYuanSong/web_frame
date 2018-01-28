__author__ = 'shy'
__date__ = '2018/1/28 14:49'

from wsgiref.simple_server import make_server


def f1():
    f1 = open("index1.html", "rb")
    data1 = f1.read()
    return [data1]


def f2():
    f2 = open("index2.html", "rb")
    data2 = f2.read()
    return [data2]


def application(environ, start_response):
    print(environ['PATH_INFO'])
    path = environ['PATH_INFO']
    start_response('200 OK', [('Content-Type', 'text/html')])

    if path == "/index1":
        return f1()

    elif path == "/index2":
        return f2()

    else:
        return ["<h1>404</h1>".encode("utf8")]


httpd = make_server('', 8003, application)

print('Serving HTTP on port 8003...')

# 开始监听HTTP请求:
httpd.serve_forever()

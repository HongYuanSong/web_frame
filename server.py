__author__ = 'shy'
__date__ = '2018/1/28 12:25'
import socket


def handle_request(client):
    buf = client.recv(1024)
    print(buf.decode('utf8'))
    client.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf8'))
    with open('index.html', 'rb') as f:
        data = f.read()
    client.send(data)


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 8001))
    s.listen(5)

    while True:
        connection, address = s.accept()
        handle_request(connection)
        connection.close()


if __name__ == '__main__':
    main()
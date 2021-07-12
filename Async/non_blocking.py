import socket

def nonblocking_way():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('httpbin.org', 80))
    except BlockingIOError:
        pass
    request = 'GET /HTTP/1.0\rnHost: httpbin.org\r\n\r\n'
    data = request.encode('ascii')
    while True:
        try:
            sock.send(data)
            break
        except OSError:
            pass

    response = b''
    while True:
        try:
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                chunk = sock.recv(4096)
            break
        except OSError:
            pass
    return response


def sync_way():
    res = list()
    for i in range(3):
        res.append(nonblocking_way())
    return res

res = sync_way()
print(len(res))
print(res[0])

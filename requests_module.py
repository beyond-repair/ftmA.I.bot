import socket


def send_request(url, method='GET', headers=None, params=None, data=None):
    host = url.split('/')[2]
    path = '/' + '/'.join(url.split('/')[3:])
    if method == 'GET':
        request = f'GET {path} HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n'
    elif method == 'POST':
        content_length = len(data) if data else 0
        request = f'POST {path} HTTP/1.1\r\nHost: {host}\r\nContent-Type: application/json\r\nContent-Length: {content_length}\r\nConnection: close\r\n\r\n'
        if data:
            request += data
    else:
        raise ValueError('Invalid HTTP method')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, 80))
        s.sendall(request.encode())
        response = b''
        while True:
            data = s.recv(1024)
            if not data:
                break
            response += data
    return response.decode()

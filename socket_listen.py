import socket
import os
import re

from http import HTTPStatus


def get_open_port():
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.bind(('', 0))
        s.listen(1)
        port = s.getsockname()[1]
    return port


with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as serv_sock:
    HOST = ''  # Symbolic name meaning all available interfaces
    PORT = get_open_port()
    server_addr = (HOST, PORT)
    print(f'starting on {server_addr}, pid: {os.getpid()}')

    serv_sock.bind(server_addr)
    print(serv_sock)
    serv_sock.listen(1)

    while True:
        print('waiting for a connection')
        conn, remote_addr = serv_sock.accept()
        print(conn)
        print('connection from', remote_addr)

        while True:
            client_data = conn.recv(1024)
            if not client_data:
                print(f'no data from {remote_addr}')
                conn.close()
                break
            text = client_data.decode('utf-8')
            print(f'Message received:\n"{repr(text)}"')

            fetch_method_headers = text.rstrip("\r\n\r\n").split(sep="\r\n", maxsplit=1)
            request_method = fetch_method_headers[0].split()[0]
            request_url = fetch_method_headers[0].split()[1]
            request_headers = fetch_method_headers[1]

            search_status_code_parameter = re.search(r"status=(\d{3})", request_url)
            try:
                if search_status_code_parameter is not None:
                    status_code_parameter = search_status_code_parameter.group(1)
                    http_status_code = HTTPStatus(int(status_code_parameter))
                else:
                    raise ValueError
            except ValueError:
                http_status_code = HTTPStatus(200)

            print(http_status_code)

            # https://developer.mozilla.org/ru/docs/Web/HTTP/Messages
            # http://httpbin.org/#/HTTP_Methods
            status_line = f"HTTP/1.1 {http_status_code.value} {http_status_code.name}"
            body = "<h1>Hey OTUS!</h1>" \
                   f"<h5>Request Method: {request_method}<br>" \
                   f"Request Source: {remote_addr}<br>" \
                   f"Response Status: {http_status_code.value} {http_status_code.name}</h5>" \
                   f"<pre>{request_headers}</pre>"

            headers = "\r\n".join([
                status_line,
                f"Content-Length: {len(body)}",
                request_headers
            ])

            server_response = '\r\n\r\n'.join([
                headers,
                body
            ])

            sent_bytes = conn.send(server_response.encode('utf-8'))
            print(f'{sent_bytes} bytes sent')

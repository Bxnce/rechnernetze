import socket
import struct
import threading
from functools import reduce
from operator import mul

socket.setdefaulttimeout(300)

My_PORT = 50000


def main(My_IP):
    print('Starting Server')
    start_server(My_IP)


def send_response(sock, message):
    sock.send(message.encode('utf-8'))
    try:
        msg = sock.recv(1024).decode('utf-8')
        print(msg)
    except socket.timeout:
        pass
    sock.close()


def start_server(My_IP):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((My_IP, My_PORT))
    sock.listen(1)
    while True:
        try:
            new_socket, addr = sock.accept()
            msg = new_socket.recv(1024)
            try:
                thread = threading.Thread(target=calculate_and_respond, args=(new_socket, msg))
                thread.start()
            except Exception:
                print('Error while calculating')

        except socket.timeout:
            sock.close()
            exit(1)


def calculate_and_respond(sock, request):
    request_id = struct.unpack('I', request[:4])[0]
    operation = request[4:7].decode('utf-8')
    n = struct.unpack('B', request[7:8])[0]
    numbers = struct.unpack(f'{n}i', request[8:])

    match operation:
        case 'Sum':
            res = sum(numbers)
        case 'Pro':
            res = reduce(mul, numbers, 1)
        case 'Max':
            res = max(numbers)
        case 'Min':
            res = min(numbers)
        case _:
            res = None

    response_id = struct.pack('I', request_id)
    response = struct.pack('i', res)

    res = response_id + response
    sock.sendall(res)
    sock.close()


if __name__ == '__main__':
    # main(sys.argv[1], sys.argv[2])
    main('127.0.0.1')

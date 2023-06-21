import socket
import threading
from functools import reduce
from operator import mul
from time import sleep

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
            msg = new_socket.recv(1024).decode('utf-8')
            try:
                thread = threading.Thread(target=calculate_and_respond, args=(new_socket, msg))
                thread.start()
            except Exception:
                print('Error while calculating')

        except socket.timeout:
            sock.close()
            exit(1)


def calculate_and_respond(sock, strTang):
    print('Calculating')
    sleep(5)
    strList = strTang.split(',')
    id = strList[0]
    operation = strList[1]
    num_list = strList[2:]
    res = 'error'
    for i in range(0, len(num_list)):
        num_list[i] = int(num_list[i])
    match operation:
        case 'Sum':
            res = str(sum(num_list))
        case 'Pro':
            res = str(reduce(mul, num_list, 1))
        case 'Max':
            res = str(max(num_list))
        case 'Min':
            res = str(min(num_list))
    res = f'{id}: {res}'
    sock.send(res.encode('utf-8'))
    sock.close()


if __name__ == '__main__':
    # main(sys.argv[1], sys.argv[2])
    main('127.0.0.1')

# request format:
# ID,Operation,z1,...,zN
# response format:
# ID: Result

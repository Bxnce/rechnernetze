import socket
import sys

socket.setdefaulttimeout(30)

Remote_PORT = 50000


def main(Remote_IP, string):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((Remote_IP, Remote_PORT))
        print(f'Name of the Socket: {sock.getsockname()}')
        start_task(sock, string)
    except socket.error:
        print('Server not reachable')


def start_task(sock, message):
    sock.send(message.encode('utf-8'))
    try:
        msg = sock.recv(1024).decode('utf-8')
        print(msg)
    except socket.timeout:
        pass
    sock.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
    # main('127.0.0.1')

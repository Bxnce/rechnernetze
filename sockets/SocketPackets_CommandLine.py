import socket
import sys

socket.setdefaulttimeout(30)

My_PORT = 50000
Remote_PORT = 50000


def main(My_IP, Remote_IP):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((Remote_IP, Remote_PORT))
        start_task(sock, "Thx for accepting!!!");
    except socket.error:
        print('Starting Server')
        start_server(My_IP)
        print('Started Server')


def start_task(sock, message):
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
    print('before listen')
    sock.listen(1)
    print('after listen')
    try:
        conn, addr = sock.accept()
        print(addr)
        start_task(conn, "Thx for connecting!!!")
    except socket.timeout:
        sock.close()


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

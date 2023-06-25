import socket
import struct

socket.setdefaulttimeout(30)
req_id = 1
Remote_PORT = 50000


def main(Remote_IP):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((Remote_IP, Remote_PORT))
        print(f'Name of the Socket: {sock.getsockname()}')
        start_task(sock)
    except socket.error:
        print('Server not reachable')


def start_task(sock):
    # Build request
    # Add request id
    req = struct.pack('I', req_id)
    # Add calculation operation
    req += b'Max'
    # Add number count
    req += struct.pack('B', 3)
    # Add numbers
    req += struct.pack('i', 1)
    req += struct.pack('i', 4)
    req += struct.pack('i', 3)

    sock.send(req)
    try:
        res = sock.recv(1024)
        response_id = struct.unpack('I', res[:4])[0]
        result = struct.unpack('i', res[4:])[0]

        print(result)
    except socket.timeout:
        pass
    sock.close()


if __name__ == '__main__':
    # main(sys.argv[1])
    main('127.0.0.1')

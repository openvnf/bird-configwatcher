import socket
class BirdControl:

    def __init__(self, socket_path):
        self.path = socket_path

    def read_lines(self, count, sock):
        data = b''
        while not data.count(b'\n') == count:
            data += sock.recv(1024)
        return data

    def reconfigure_check(self, config_path):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(self.path)
        message = bytes(f'configure check "{config_path}" \n','utf-8')
        print(f'send message: {message}')
        sock.send(message)
        reply = self.read_lines(3, sock)
        print(f'get reply: {reply}')
        sock.close()
        sock = None
        return b'Configuration OK' in reply

    def reconfigure(self, config_path):
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.connect(self.path)
        message = bytes(f'configure "{config_path}" \n','utf-8')
        print(f'send message: {message}')
        sock.send(message)
        reply = self.read_lines(3, sock)
        print(f'get reply: {reply}')
        sock.close()
        return b'Reconfigured' in reply




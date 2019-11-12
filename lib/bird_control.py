import socket
class BirdControl:

    def __init__(self, socket_path):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.path = socket_path

    def reconfigure_check(self, config_path):
        self.sock.connect(self.path)
        message = bytes(f'configure check "{config_path}" \n','utf-8')
        print(f'send message: {message}')
        self.sock.sendall(message)
        reply = self.sock.recv(1024)
        print(f'get reply: {reply}')
        self.sock.close()
        return b'Configuration OK' in reply

    def reconfigure(self, config_path):
        self.sock.connect(self.path)
        message = bytes(f'configure "{config_path}" \n','utf-8')
        print(f'send message: {message}')
        self.sock.sendall(message)
        reply = self.sock.recv(1024)
        print(f'get reply: {reply}')
        self.sock.close()
        return b'Reconfigured' in reply




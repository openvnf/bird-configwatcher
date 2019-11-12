import socket
class BirdControl:

    def __init__(self, socket_path):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.path = socket_path

    def reconfigure_check(self, config_path):
        self.sock.connect(self.path)
        message = f'reconfigure check "{config_path}" \n'
        self.sock.sendall(bytes(message,'utf-8'))
        reply = self.sock.recv(1024)
        self.sock.close()
        return b'Configuration OK' in reply

    def reconfigure(self, config_path):
        self.sock.connect(self.path)
        message = f'reconfigure "{config_path}" \n'
        self.sock.sendall(bytes(message,'utf-8'))
        reply = self.sock.recv(1024)
        self.sock.close()
        return b'Reconfigured' in reply




import socket
class BirdControl:

    def __init__(self, socket_path):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(socket_path)

    def reconfigure_check(self, config_path):
        message = f'reconfigure check "{config_path}" \n'
        self.sock.sendall(message)
        reply = self.sock.recv(1024)
        return "Configuration OK" in reply

    def reconfigure(self, config_path):
        message = f'reconfigure "{config_path}" \n'
        self.sock.sendall(message)
        reply = self.sock.recv(1024)
        return "Reconfigured" in reply




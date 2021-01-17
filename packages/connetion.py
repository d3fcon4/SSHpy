import paramiko
import socket


class Connection:

    def __init__(self, hostname, username, password, port):
        self.host = hostname
        self.user = username
        self.pass_ = password
        self.port_ = port
        self.ssh_client = paramiko.SSHClient()

    def connect(self):
        try:
            self.ssh_client.set_missing_host_key_policy(
                paramiko.AutoAddPolicy())
            self.ssh_client.connect(
                self.host,
                self.port_,
                self.user,
                self.pass_
            )
        except (paramiko.SSHException,
                paramiko.AuthenticationException,
                paramiko.BadAuthenticationType,
                paramiko.BadHostKeyException,
                socket.error):
            print(f'Connection Error!')

    def command_line(self, cmd):
        try:
            stdin, stdout, stderr = self.ssh_client.exec_command(cmd)
            stdout.channel.recv_exit_status()
            output = stdout.readlines()
            for lines in output:
                print(lines)
            self.ssh_client.close()

        except paramiko.SSHException:
            return -1

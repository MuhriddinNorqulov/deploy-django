import os


def make_socket(name):
    socket_file_path = f'/etc/systemd/system/{name}.socket'
    command = f'sudo touch {socket_file_path}'
    os.system(command)

    body = f"""
[Unit]
Description={name} socket

[Socket]
ListenStream=/run/{name}.sock

[Install]
WantedBy=sockets.target
    """

    with open(socket_file_path, 'w') as f:
        f.write(body)



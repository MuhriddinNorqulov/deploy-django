import os


def start_socket(name):
    os.system(f'sudo systemctl start {name}.socket')
    os.system(f'sudo systemctl enable {name}.socket')
    os.system(f'curl --unix-socket /run/{name}.sock localhost')
    os.system('sudo systemctl daemon-reload')
    os.system(f'sudo systemctl restart {name}')
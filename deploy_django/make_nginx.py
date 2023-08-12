from string import Template
import os


def make_nginx(domain, root_dir, name):
    nginx_file_path = f'/etc/nginx/sites-available/{name}'
    command = f'sudo touch {nginx_file_path}'
    os.system(command)

    body = Template("""
server {
    listen 80;
    server_name $_domain;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root $_root_dir;
    }
    location /media/ {
        root $_root_dir;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/$_socket_name.sock;
    }
}
    """
                    ).substitute(_domain=domain, _root_dir=root_dir, _socket_name=name)

    with open(nginx_file_path, 'w') as f:
        f.write(body)


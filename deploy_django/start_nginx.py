import os


def start_nginx(name):
    os.system(f'sudo ln -s /etc/nginx/sites-available/{name} /etc/nginx/sites-enabled')
    os.system('sudo nginx -t')
    os.system('sudo systemctl restart nginx')
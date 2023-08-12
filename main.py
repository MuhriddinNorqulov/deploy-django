#!/usr/bin/env python3
import os
import getpass
from deploy_django import (
    make_socket,
    make_nginx,
    make_service,
    start_nginx,
    start_socket,
    test,
    find_config
)

root_dir = os.getcwd()
username = getpass.getuser()
config_path = find_config.get_config_dir_path(root_dir)
name = input("name: ")
domain = input("domain (sub.domain.com):")

if __name__ == '__main__':

    make_socket.make_socket(name)
    make_service.make_service(name, username, f'{root_dir}/venv', config_path)

    start_socket.start_socket(name)

    make_nginx.make_nginx(domain, root_dir, name)
    start_nginx.start_nginx(name)
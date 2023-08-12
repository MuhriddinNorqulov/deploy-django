import os


def make_service(name, username, project_dir_path, venv_path, config_dir_path):
    service_file_path = f'/etc/systemd/system/{name}.service'
    command = f'sudo touch {service_file_path}'
    os.system(command)

    body = f"""
[Unit]
Description={name} daemon
Requires={name}.socket
After=network.target

[Service]
User={username}
Group=www-data
WorkingDirectory={project_dir_path}
ExecStart={venv_path}/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/{name}.sock \
          {config_dir_path}.wsgi:application
    """

    with open(service_file_path, 'w') as f:
        f.write(body)

import os


def get_config_dir_path(root_dir):
    p = os.path
    j = p.join
    for folder_name in os.listdir(root_dir):
        if p.isdir(j(root_dir, folder_name)):
            if p.isfile(j(folder_name, "wsgi.py")):
                return folder_name


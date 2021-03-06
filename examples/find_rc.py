import os

'''This will look for environment variable and searches for .rc file from the current working directory and searches in home directory'''

def find_rc(rc_name=".examplerc"):
    # CHECK FOR ENV VARIABLE
    var_name = "EXAMPLERC_DIR"
    if var_name in os.environ:
        var_path = os.path.join(f"${var_name}", rc_name)
        config_path = os.path.expandvars(var_path)
        print(f"Checking {config_path}")
        if os.path.exists(config_path):
            return config_path

    # Check the current working directory

    config_path = os.path.join(os.getcwd(), rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # Check user home directory
    home_dir = os.path.expanduser("~/")
    config_path = os.path.join(home_dir, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path

    # Check Directory of the This File
    file_path = os.path.abspath(_file_)
    parent_path = os.path.dirname(file_path)
    config_path = os.path.join(parent_path, rc_name)
    print(f"Checking {config_path}")
    if os.path.exists(config_path):
        return config_path
    print(f" File {rc_name} has not been found")


if __name__ == __main()__:
    find_rc()
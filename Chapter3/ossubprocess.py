import subprocess
import os

os.environ.get('LOGLEVEL')
os.environ['LOGLEVEL'] = 'DEBUG'
os.environ.get('LOGLEVEL')

cp = subprocess.run(['ls', '-l'],
                    capture_output=True,
                    universal_newlines=True)

cp.stdout

cp = subprocess.run(['ls', '/doesnotexist'],
                    capture_output=True,
                    universal_newlines=True,
                    check=True)

cp.stderr

#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import numpy as np
os.system('cls')
os.system("color {}".format(("02","03","04","05","06","07","08","0a","0b","0c","0d","0e","0f")[np.random.randint(0,13)]))
def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CryptoCoin.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

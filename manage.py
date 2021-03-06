#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.
   manage.py 
   project name: creation of Cryptocurrency
   @ Author  Kuntal & Himalaya
   @ version  0.1
   @date      05/09/2019
   """
import os
import sys
import numpy as np
try:
    os.system('cls')
except:
    os.system("clear")
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

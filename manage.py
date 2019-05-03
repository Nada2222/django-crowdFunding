#!/usr/bin/env python
import os
import sys

<<<<<<< HEAD
if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "crowdFunding08.settings")
=======
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crowdFunding.settings')
>>>>>>> d36c4b517eab3c21da3097626b93ef170b2a126d
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
